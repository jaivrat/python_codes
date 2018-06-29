
#Generate some sample logistic regression data
intercept = 0.4
theta1 = 1
theta2 = -2
theta3 = 3
theta4 = 0.00001
set.seed(144)
N = 10000
X <- matrix(runif(4*N), ncol = 4)
X <- cbind(rep(1,N), X)
head(X)

THETA <- matrix(c(intercept, theta1, theta2, theta3, theta4), ncol = 1)
THETA
Z     <- X %*% THETA + 0.2*matrix(rnorm(N), ncol = 1)
hist(Z)
Y     <- rep(1, length(Z))
Y[Z < mean(Z)] <- 0
table(Y)
#Put some values blurr at mean(Z)
lower = mean(Z) - sd(Z)
upper = mean(Z) + sd(Z)
Y[sample(which(Z < mean(Z) & Z > lower),50,replace = TRUE)] <- 1
Y[sample(which(Z >= mean(Z) & Z < upper),50,replace = TRUE)] <- 0
table(Y)
dat.prep <- (data.frame(Y=Y, as.data.frame(X)[,-1]))
#dat.prep[["Y"]] <- as.factor(dat.prep[["Y"]])
write.csv(dat.prep,file = "dat.prep.csv", row.names = FALSE)



#-- Do logistic in R
datf <- read.csv("dat.prep.csv", stringsAsFactors = FALSE)
dim(datf)
head(datf)
library(caTools)
model.reg    <- glm(Y ~ ., data = datf, family = binomial)
summary(model.reg)
predictTrain = predict(model.reg, newdata = datf, type = "response")
#Train Accrracy
tab <- table(datf$Y, predictTrain>= 0.5)
tab
sum(diag(tab))/sum(tab)



library(ROCR)
#Train
ROCRpred = prediction(predictTrain, datf$Y)
perf     = performance(ROCRpred, "tpr", "fpr")
plot(perf)
as.numeric(performance(ROCRpred, "auc")@y.values)


#dropping last one with insignificat 
summary(glm(Y ~ ., data = datf[,-5], family = binomial))
