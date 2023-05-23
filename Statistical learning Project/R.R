 library(readr)
 library(data.table)
 library(tidyverse)
 heart <- read_csv("heart.csv")
 library(rcompanion)
library(psych)
 library(ggplot2)
 library(ggvis)
 library(gmodels)
 library(caret)
 library(e1071)
 ###########################################
 cor(heart)
 str(heart)
 heart$cp<-as.factor(heart$cp)
 heart$output<-as.factor(heart$output)
 heart$sex<-as.factor(heart$sex)
 heart$fbs<-as.factor(heart$fbs)
 heart$restecg<-as.factor(heart$restecg)
 heart$exng<-as.factor(heart$exng)
 heart$caa<-as.factor(heart$caa)
 heart$slp<-as.factor(heart$slp)
 heart$thall<-as.factor(heart$thall)
 #############################################
 #dealing with outliers 
 
 boxplot(heart$thalachh) #there is an outline in this var
 
 heart <- subset(heart, heart$thalachh> (133.5 - 1.5*IQR(heart$thalachh)) & heart$thalachh< (166.0+ 1.5*IQR(heart$thalachh)))
 boxplot(heart$thalachh)
 view(heart)
 boxplot(heart$trtbps) #there is an outlier in this var
 summary(heart$trtbps)
 heart <- subset(heart, heart$trtbps> (120.0  - 1.5*IQR(heart$trtbps)) & heart$trtbps< (140.0+ 1.5*IQR(heart$trtbps)))
 boxplot(heart$trtbps)
 view(heart)
 boxplot(heart$chol) #there is an outlier in this var
 summary(heart$chol)
 heart <- subset(heart, heart$chol> (210.0   - 1.5*IQR(heart$chol)) & heart$chol< (273.0+ 1.5*IQR(heart$chol)))
 boxplot(heart$chol)
 boxplot(heart$oldpeak) #there is an outlier in this var
 summary(heart$oldpeak)
 heart <- subset(heart,heart$oldpeak< (1.600+ 1.5*IQR(heart$oldpeak)))
 boxplot(heart$chol)
 ######################################
 #normalization and organization 
 sum(is.na(heart))
 normalize <- function(x) {
    num <- x - min(x)
    denom <- max(x) - min(x)
    return (num/denom)
 }
 nor <-function(x) { (x -min(x))/(max(x)-min(x)) }
 
 # ##Run nomalization on first 4 coulumns of dataset because they are the predictors
 heart_norm <- as.data.frame(lapply(heart[,c(1,4,5,8,10)], nor))
 heart <- heart[ -c(1,4,5,8,10) ]
 heart<-tibble::rowid_to_column(heart, "ID")
 heart_norm<-tibble::rowid_to_column(heart_norm, "ID")
 heart <- merge(heart,heart_norm,by="ID",all.x=TRUE)
 heart <- heart[ -c(1) ]
 output<-(heart$output)
 heart <- heart[ -c(9) ]
 heart$output<-output
 ########################################################
 #descriptive stat
 describe(heart)
 summary(heart)
############################################################
 dev.off()
 ggplot(data = heart,
            mapping = aes(x = output, fill=cp))+
  geom_bar(stat="count")+
   labs(title="the correlation between Chest Pain type 
        \n and the heart attack accouring",
        x="heart attac accouring",
        y="")
 ###################################################
 ggplot(data = heart,
        mapping = aes(x = output, y=oldpeak))+
    geom_bar(stat="identity")+
    labs(title="the correlation between Chest Pain type 
        \n and the heart attack accouring",
         x="heart attac accouring",
         y="")
 
######################################################
ggplot(data = heart,
       mapping = aes(x = output, fill=exng))+
   geom_bar(stat="count")+
   labs(title="the correlation between exercise  
        \n and the heart attack accouring",
        x="heart attac accouring",
        y="")
####################################################
#machine learning 
   index <- createDataPartition(heart$output, p=0.75, list=FALSE)
   heart.training <- heart[index,]
   heart.test <- heart[-index,]
   # Train a model
   model_knn <- train(heart.training[, 1:13], heart.training[, 14], method='knn')
   model_cart <- train(heart.training[, 1:13], heart.training[,14], method='rpart2')
   model_rf <- train(heart.training[, 1:13], heart.training[, 14], method='rf')
   
   
   predictions<-predict.train(object=model_knn,heart.test[,1:13], type="raw")
   predictions_cart<-predict.train(object=model_cart,heart.test[,1:13], type="raw")
   predictions_rf<-predict.train(object=model_rf,heart.test[,1:13], type="raw")
   
   table(predictions)
   levels(predictions)
   levels(heart.test[,14])
   predictions
   
   
   confusionMatrix(predictions_rf, factor(heart.test[,14]))
   confusionMatrix(predictions, factor(heart.test[,14]))
   confusionMatrix(predictions_cart, factor(heart.test[,14]))
  

