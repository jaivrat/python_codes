library(ISLR)
data("Hitters")
#--

head(Hitters)
str(Hitters)
colnames(Hitters)
rownames(Hitters)

datH <- Hitters[complete.cases(Hitters), ]

x = model.matrix( Salary ~ . , data = datH)[,-1]
y = datH$Salary

library(glmnet)
#If alpha=0 then a ridge regression model is fit, and if alpha=1 then a lasso model is fit.
grid = 10^seq(10, -2, length.out = 100)
grid

#Ridge Model Fit 
ridge.mod = glmnet(x, y, alpha=0, lambda =grid)

head(coef(ridge.mod ))
dim(coef(ridge.mod ))

ridge.mod$lambda[50]
coef(ridge.mod)[,50]
sqrt(sum(coef(ridge.mod)[ -1 ,50]^2) )

ridge.mod$lambda [60]
coef(ridge.mod)[,60]
sqrt(sum(coef(ridge.mod)[ -1 ,60]^2) )


#We can use the predict() function for a number of purposes. For instance,
#we can obtain the ridge regression coefficients for a new value of lambda say 50:
predict (ridge.mod , s=50, type = "coefficients")[1:20,]

set.seed(1)
train  = sample (1: nrow(x), nrow(x)/2)
test   = (-train )
y.test = y[test]


#----------------------------------------------------------------

#Next we fit a ridge regression model on the training set, and evaluate
#its MSE on the test set, using lambda = 4.
ridge.mod  = glmnet (x[train ,],y[train],alpha =0, lambda =grid ,thresh =1e-12)
ridge.pred = predict(ridge.mod ,s=4, newx=x[test ,])
mean((ridge.pred -y.test)^2)

#if we had instead simply fit a model with just an intercept, we would have predicted each test observation using
#the mean of the training observations. In that case, we could compute the test set MSE like this:
mean(( mean(y[train ])-y.test)^2)

#We could also get the same result by fitting a ridge regression model with a very large value of lambda
ridge.pred = predict(ridge.mod, s=1e10 , newx=x[test ,])
mean(( ridge.pred -y.test)^2)

#OLS is simply linear regression with not regularization, lambda = 0
ridge.pred = predict(ridge.mod, s=0, newx=x[test ,])
mean(( ridge.pred -y.test)^2)


#In general, instead of arbitrarily choosing lambda = 4, it would be better to
#use cross-validation to choose the tuning parameter lambda. We can do this using
#the built-in cross-validation function, cv.glmnet().
set.seed(1)
cv.out = cv.glmnet(x[train ,], y[train], alpha = 0)
plot(cv.out)
bestlam = cv.out$lambda.min
bestlam

#we refit our ridge regression model on the full data set,
#using the value of lambda chosen by cross-validation, and examine the coefficient
#estimates
ridge.pred = predict(ridge.mod, s=bestlam , newx=x[test ,])
mean((ridge.pred -y.test)^2)

out=glmnet (x,y,alpha =0)
predict (out ,type="coefficients",s=bestlam )[1:20 ,]








