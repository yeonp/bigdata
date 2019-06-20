# 05-1.R
# 데이터 분석 기초

# 데이터 파악하기

exam <- read.csv("csv_exam.csv")
exam

head(exam)  # 기본 앞 6행 
head(exam,10)  # 앞 10행 까지  출력

tail(exam) # 기본 뒤 6행 
tail(exam,10)  # 뒤 10행 까지  출력

View(exam)
dim(exam)
# dim(iris3)
str(exam)
summary(exam)

quantile(exam$math)

# mpg 데이터 파악하기
# miles per gallon  , 자동차의 제원과 연비데이터
install.packages("ggplot2") # gg: Grammar of Graphic
library(ggplot2)

mpg   # 234 x 11
View(mpg)
str(mpg)
# 5가지 fuel : petrol(가솔린),diesel,electric,
#            compressed natural gas , r       
mean(mpg$cty)
mean(mpg$hwy)
summary(mpg)
hist(mpg$hwy)
qplot(mpg$cty)

# 데이터 수정 - 변수명 바꾸기
install.packages("dplyr")
library(dplyr)  # rename()함수를 지원 

df_raw <- data.frame(var1 = c(1,2,1),
                     var2 = c(2,3,2))
df_raw

df_new <- df_raw    # 그대로 복사(변경없음)
df_new

# rename : 변수명(컬럼이름)을 변경
df_new <- rename(df_raw, model=var1,fuel=var2)
df_new

# 변수(컬럼)를 추가하기 : 파생변수 
df <- data.frame(var1 = c(1,2,1),
                 var2 = c(2,3,2),
                 var3 = c(5,6,7))
df
df$var1
df$var2
df$var_sum <- df$var1 + df$var2 + df$var3
df$var_mean <- (df$var1 + df$var2 + df$var3)/3
df

mpg
mpg$total <- (mpg$cty + mpg$hwy)/2
head(mpg)
View(mpg)
summary(mpg$total)
mean(mpg$total)
hist(mpg$total)

mpg$myvar1 <- c(1:234)
mpg$myvar2 <- "대한민국"
View(mpg)

# 조건에 따른 변수의 값을 할당 
mpg$test <- ifelse(mpg$total >= 20, "pass","fail")
View(mpg)
#mpg$test <- NULL  # 컬럼 삭제 
mpg$myvar <- NULL
mpg$myvar1 <- NULL
mpg$myvar2 <- NULL

# 중첩된 조건 에 따른 변수의 값을 할당 
# 30 이상 : A
# 20 이상 : B
# 20 미만 : C

mpg$grade <- ifelse(mpg$total >= 30, "A",
                    ifelse(mpg$total >=20, "B","C"))
View(mpg)
table(mpg$test)  # 빈도표 생성
table(mpg$grade)
qplot(mpg$test)  # 막대 그래프
qplot(mpg$grade)

# 4 단계 등급 
mpg$grade2<- ifelse(mpg$total >= 30, "A",
                ifelse(mpg$total >=25, "B",
                   ifelse(mpg$total >=20,"C","D")))
View(mpg)
table(mpg$grade2)
qplot(mpg$grade2)


# 분석 도전 답안

# 문제 1
library(ggplot2) 
#midwest <- as.data.frame(ggplot2::midwest) 
midwest
head(midwest) 
tail(midwest) 
View(midwest) 
dim(midwest) 
str(midwest) 
summary(midwest)


# 문제 2
library(dplyr) 
midwest <- rename(midwest, total = poptotal) 
midwest <- rename(midwest, asian = popasian)
View(midwest)

# 문제 3
midwest$ratio <- midwest$asian/midwest$total*100 
hist(midwest$ratio)

# 문제 4 
mean(midwest$ratio) ## [1] 0.4872462 
midwest$group <- ifelse(midwest$ratio > 0.4872462, "large", "small")
View(midwest)

# 문제 5
table(midwest$group) 
# large small 
# 119 318 
qplot(midwest$group)

