library(reshape2)
library(ggplot2)
library(dlm)
library(ggpubr)
library(gridExtra)

#-------------------------------------------------------------------------------
#Generate some data first - toy example
#Kalman filter/dynamic linear model in R
#-------------------------------------------------------------------------------
rm(list=ls())
set.seed(144)
SIZE = 1000

df <- data.frame(x1 = sample(seq(from = -1.0, to=1.0,  length.out = SIZE), size = SIZE, replace = FALSE),
                 x2 = sample(seq(from = -3.0, to=3.0,  length.out = SIZE), size = SIZE, replace = FALSE))

theta_base_1 <- 0.4
theta_base_2 <- 1.2
# data.frame(mapply(`*`, df, c(theta1[1], theta2[1]))) 


# Varying theta/coeff
theta_1_shocks = c(0, rnorm(nrow(df)-1 , mean = 0, sd = 0.01))
theta1_s = theta_base_1 + cumsum(theta_1_shocks)
theta_2_shocks = c(0, rnorm(nrow(df)-1 , mean = 0, sd = 0.02))
theta2_s = theta_base_2 + cumsum(theta_2_shocks)


theta_df <- data.frame(theta1_s = theta1_s, theta2_s = theta2_s)
y_shocks <- rnorm(nrow(df), mean = 0, sd = 0.05)

y <- rowSums(data.matrix(df) * data.matrix(theta_df))  + y_shocks

df[["y"]] <- y
df[["tim"]] <- 1:length(y)


View(df)


#-------------------------------------------------------------------------------
#Learn MLE from first 500
#-------------------------------------------------------------------------------

plot(df[, c("x1", "x2")])

buildFn <- function(x)
{
  ret.mod <- dlm::dlmModReg(X = as.matrix(df[1:(SIZE/2), c("x1", "x2")]),
                            dV = exp(x[1]), 
                            dW = exp(x[2:3]), 
                            addInt = FALSE)
  ret.mod
}


fit <- dlm::dlmMLE( y     = df$y[1:(SIZE/2)], 
                    build = buildFn, 
                    parm  = log(c(1e2,rep(1e2, 2))),
                    lower = log(rep(1e-5, 3)), 
                    hessian=TRUE)


mod.res <- buildFn(fit$par)
avarLog <- solve(fit$hessian)
avar    <- diag(exp(fit$par)) %*% avarLog %*% diag(exp(fit$par)) # Delta method
V(mod.res)
W(mod.res)


# We can see here that model quickly discovers states, 
# starting from (0,0) guess of theta1 to ~(0.4, 1.2)
res.filt <- dlm::dlmFilter(y = df$y[1:(SIZE/2)], mod = mod.res)
res.filt$m
names(res.filt)
View(res.filt$m)


results.df <- data.frame(res.filt$m[-1, ] , 
                         theta1 = theta1_s[1:500], 
                         theta2 = theta2_s[1:500],
                         tim = df$tim[1:500])
#X1, X2 (not confuse with x1 and x2 inputs) are filtered values of internal states.. ie theta1_s and theta2_s
head(results.df)


library(reshape2)
results.df.melt <- reshape2::melt(results.df, id.vars = "tim")     
ggplot(data = results.df.melt, aes(x = tim, y = value, group = variable, colour = variable)) + 
  geom_line() 


#-------------------------------------------------------------------------------
#Future prediction though kalman filter
#-------------------------------------------------------------------------------
names(res.filt)
tail(res.filt$m, 1)
start_row = (SIZE/2)+1
mod.fwd <- dlm::dlmModReg(X = as.matrix(df[start_row:nrow(df), c("x1", "x2")]),
                          dV = V(mod.res), 
                          dW = diag(W(mod.res)), 
                          m0 = as.numeric(tail(res.filt$m, 1)),
                          C0 = with(res.filt, dlmSvd2var(U.C[[ (SIZE/2)+1]], D.C[(SIZE/2)+1,])),
                          addInt = FALSE)

res.fwd.filt   <- dlm::dlmFilter(y = df$y[start_row:nrow(df)], mod = mod.fwd)

#=== Manual verification start:
# dlmForecast(mod.fwd , nAhead = 1, method = c("plain", "svd"), sampleNew = FALSE) can be used only for constant models!
# names(mod.fwd ) => "m0"  "C0"  "FF"  "V"   "GG"  "W"   "JFF" "JV"  "JGG" "JW"  "X"  
#mod.fwd$m0 is same as res.filt$m[nrow(res.filt$m),]
#mod.fwd$C0 is same as with(res.filt, dlmSvd2var(U.C[[501]], D.C[501,]))
#G is same as mod.fwd$GG, ie states transition matrix G_t .. theta_t = G_t * theta_{t-1} + ~w_t , G is I in this case
#W is mod.fwd$W , which is diag(W(mod.res)) , Vt = V(mod.res) : both constants
m0 = mod.fwd$m0
C0 = mod.fwd$C0
G = mod.fwd$GG 
Wt = mod.fwd$W 
Vt = V(mod.res)
# one step ahead pred a_t = E(Theta_t|t-1), R_t = Var(Theta_t|t-1) ( Petris page 57)
a_1 =  G %*% m0
R_1 = (G %*% C0 %*% t(G)) + W0
R_1
# one step ahead pred Y_t = E(Y_t|t-1) = F_t * a_t, Q_t = Var(Y_t|t-1) = F_t * R_t * F_t' + V_t
F_1 = matrix(data.matrix(df)[501,c("x1", "x2")], nrow = 1)
f_1 = F_1 %*% a_1
V_1 = V(mod.res)
Q_1 = (F_1 %*% R_1 %*% t(F_1)) + Vt
Q_1
# the filtering density of theta_t|t is m_t = E(theta_t|t) = a_t + R_t * F_t' * (Q_t^-1) * e_t
# Var(theta_t|t) = R_t - R_t * F_t' * (Q_t^-1) * F_t * R_t where e_t = Y_t - f_t ie forecast error
Y_1 = data.matrix(df)[501, c("y")]
e_1 = Y_1  - f_1
m_1 = a_1  + (R_1 %*% t(F_1) %*% solve(Q_1) %*% e_1)
m_1
m_1 - res.fwd.filt$m[2,]
# so in the filter output first row is m0, ie the starting state.
# and first observation and corresponding filter state is res.fwd.filt$m[2,]
names(res.fwd.filt) 
# [1] "y"   "mod" "m"   "U.C" "D.C" "a"   "U.R" "D.R" "f"
res.fwd.filt$f[1] - f_1 
# is 0, so res.fwd.filt$f contains all predictions, one by one!
#=== Manual verification end


results.fwd.df <- data.frame(res.fwd.filt$m[-1, ] , 
                             theta1 = theta1, 
                             theta2 = theta2,
                             tim = df$tim[-(1:500)])
head(results.fwd.df)

results.fwd.df.melt <- reshape2::melt(results.fwd.df, id.vars = "tim")     
ggplot(data = results.fwd.df.melt, aes(x = tim, y = value, group = variable, colour = variable)) + 
  geom_line() + 
  ggtitle("States, ie thetas")


#plot y's and predictions
results.y.df  <- data.frame(tim = df$tim[-(1:500)], y = df$y[-(1:500)], pred = res.fwd.filt$f)
results.y.df.melt <- reshape2::melt(results.y.df, id.vars = "tim")     
ggplot(data = results.y.df.melt, aes(x = tim, y = value, group = variable, colour = variable)) + 
  geom_line() + 
  ggtitle("ys")

#Normality plot
ggqqplot(res.fwd.filt$f - df$y[-(1:500)])
plot(res.fwd.filt$f, df$y[-(1:500)])

head(residuals(res.fwd.filt, type = "raw")$res)
head(res.fwd.filt$f - df$y[-(1:500)])

head(scale(residuals(res.fwd.filt, type = "raw")$res))
head(scale(res.fwd.filt$f - df$y[-(1:500)]))

head(residuals(res.fwd.filt, type = "standardized")$res)
head((res.fwd.filt$f - df$y[-(1:500)])/sd(res.fwd.filt$f - df$y[-(1:500)]))

sd(res.fwd.filt$f - df$y[-(1:500)])
#residuals(res.fwd.filt)$sd
with(res.fwd.filt, dlmSvd2var(U.R[[500]], D.R[500,]))


#what is sd term , and how it is related to the filter above
tail(residuals(res.fwd.filt)$sd, 1)^2
#Formula Directly from algo Q_t = F_t %*% R %*% F_t' + V
tail(res.fwd.filt$mod$X, 1) %*% with(res.fwd.filt, dlmSvd2var(U.R[[500]], D.R[500,])) %*% t(tail(res.fwd.filt$mod$X, 1)) + res.fwd.filt$mod$V




#---------------------------------------------------------------------------------
#Let us check if MLE estimates of V and W matter
#---------------------------------------------------------------------------------
#with(res.fwd.filt, dlmSvd2var(U.R, D.R))
#with(res.fwd.filt, dlmSvd2var(U.R[[500]], D.R[500,]))
#with(res.fwd.filt, dlmSvd2var(U.R[[499]], D.R[499,]))
residuals.sd.true <- residuals(res.fwd.filt)$sd ^2

#model on some choice of dV and dW
V(mod.res)
#[1,] 0.0001028086
W(mod.res)
# > W(mod.res)
#              [,1]       [,2]
# [1,] 0.0001065652 0.00000000
# [2,] 0.0000000000 0.00038172


library(manipulate)

VisualiseChange <- function(pV.pct.inc, dW.pct.inc)
{
  ##-- all goes in function
  #conctsurct a model, based on assumed dV and dW
  dV.new <- V(mod.res) * ( 1 + pV.pct.inc/100)
  dW.new <- W(mod.res) * ( 1 + dW.pct.inc/100)
  #Use filter on first half to come up with m0 and C0 for next fwd data set.
  mod.first.half <- dlm::dlmModReg(X = as.matrix(df[1:500, c("x1", "x2")]),
                                   dV = dV.new, 
                                   dW = diag(dW.new), 
                                   m0 = rep(0, 2),
                                   C0 = diag(2) * 1e7,
                                   addInt = FALSE)
  res.first.half.filt   <- dlm::dlmFilter(y = df$y[1:500], mod = mod.first.half)
  #Create a new model with assumed dV dW and m0 C0
  m0 = tail(res.first.half.filt$m, 1)
  C0 = with(res.first.half.filt, dlmSvd2var(U.C, D.C))
  mod.second.half <- dlm::dlmModReg(X = as.matrix(df[-(1:500), c("x1", "x2")]),
                                    dV = dV.new, 
                                    dW = diag(dW.new), 
                                    m0 = m0,
                                    C0 = C0[[length(C0)]],
                                    addInt = FALSE)
  #apply filter and see results
  res.second.half.filt   <- dlm::dlmFilter(y = df$y[-(1:500)], mod = mod.second.half)
  
  
  final.df <- data.frame("tim" = df$tim[-(1:500)],
                         "actual.y" = df$y[-(1:500)],
                         "pred.y.true" = res.fwd.filt$f,
                         "pred.y.apprx" = res.second.half.filt$f)
  final.df.melt = reshape2::melt(final.df, "id.vars" = "tim")
  p1 <- ggplot(final.df.melt, aes(x = tim, y = value, group = variable, colour = variable)) + geom_point() + geom_line()
  
  
  
  
  final.df <- data.frame("tim" = df$tim[-(1:500)],
                         "pred.Q" = residuals(res.fwd.filt)$sd,
                         "pred.Q.apprx" = residuals(res.second.half.filt)$sd)
  final.df.melt = reshape2::melt(final.df, "id.vars" = "tim")
  p2 <- ggplot(final.df.melt, aes(x = tim, y = value, group = variable, colour = variable)) + geom_point() + geom_line()
  
  
  #with(res.second.half.filt, dlmSvd2var(U.R, D.R))
  
  var.mag <- data.frame(t(sapply(1:length(df$tim[-(1:500)]), function(i){
    Ft = res.fwd.filt$mod$X[i, ]
    Qt = dlmSvd2var(res.fwd.filt$U.R[[i]], res.fwd.filt$D.R[i,])
    c(Ft %*% Qt %*% Ft, res.fwd.filt$mod$V)
  })))
  colnames(var.mag) <- c("QTerm", "V")
  var.mag[["tim"]] = df$tim[-(1:500)]
  var.mag.melt = reshape2::melt(var.mag, "id.vars" = "tim")
  p3 <- ggplot(var.mag.melt, aes(x = tim, y = value, group = variable, colour = variable)) + geom_point() + geom_line() + ggtitle("Qpart & V part")
  
  library(gridExtra)
  p.final <- grid.arrange(
    p1,
    p2,
    p3,
    ncol = 1,
    top = "Title of the page"
  )
  
  ##-- all goes in function
  p.final
} 

manipulate(VisualiseChange(pV.pct.inc = pV.pct.inc, dW.pct.inc = dW.pct.inc), pV.pct.inc = slider(0, 100), dW.pct.inc = slider(0, 100))

#Seems some error in estimation of dV and dW does not matter. Kalman filter process handles it
#errors are more weightage coming out of Q matrix rather than measurement errors V


df

nrow(df)
