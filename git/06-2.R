# 06-2.R

# filter() : 행을 추출한다 
library(dplyr)
exam <- read.csv("csv_exam.csv")
exam

out_data <- exam %>% filter(class == 1)
out_data

out_data2 <- exam %>% filter(class == 2)
out_data2

out_data <- exam %>% filter(class != 1)
out_data


out_data <- exam %>% filter(math > 50)
out_data

out_data <- exam %>% filter(english <= 80)
out_data

# 다중 조건을 필터링
exam %>% filter(class == 1 & math >= 50)
exam %>% filter(class == 2 & english >= 80)
exam %>% filter(math >= 90 | english >= 90) 
exam %>% filter(math >= 90 | english >= 90 |science >=60) 

exam %>% filter(class == 1 | class == 3 | class == 5)

exam %>% filter(class %in% c(1,3,5))

# 문제 1
library(ggplot2)

mpg_a <- mpg %>% filter(displ <= 4)  # displ 4 이하 추출
mpg_b <- mpg %>% filter(displ >= 5)  # displ 5 이상 추출

mean(mpg_a$hwy)  # displ 4 이하 hwy 평균
## [1] 25.96319
mean(mpg_b$hwy)  # displ 5 이상 hwy 평균
## [1] 18.07895


# 문제 2

mpg_audi <- mpg %>% filter(manufacturer == "audi")      # audi 추출
str(mpg_audi)
dim(mpg_audi)
dim(mpg)

mpg_toyota <- mpg %>% filter(manufacturer == "toyota")  # toyota 추출
dim(mpg_toyota)
mean(mpg_audi$cty)    # audi의 cty 평균
## [1] 17.61111
mean(mpg_toyota$cty)  # toyota의 cty 평균
## [1] 18.52941


# 문제 3
# manufacturer가 chevrolet, ford, honda에 해당하면 추출
mpg_new <- mpg %>% filter(manufacturer %in% c("chevrolet", "ford", "honda"))
View(mpg_new)
mean(mpg_new$hwy)
## [1] 22.50943

# select(컬럼이름1,컬럼이름2,...) : 열을 추출한다 
df_math <- exam %>% select(math)
str(df_math)
str(exam$math)

df_math_english_class <- exam %>% select(class,math,english)
head(df_math_english_class)

df_all <- exam %>% select(-math,-english)
head(df_all)

# filter(),select()함께 연동 :   df1 %>% ...  %>% ... %>% ...
df_result <- exam %>% filter(class==1)
df_result2 <- df_result %>% select(english)
df_result2


df_result <- exam %>% filter(class==1) %>%
                      select(english)
df_result


df_result <- exam %>% select(id,math) %>% head(5) 
df_result

# arrange() : 순서로 정렬(오름 차순,내림 차순)

df <- exam %>% arrange(math) # 오름차순 
df

df <- exam %>% arrange(desc(math)) # 내림차순 
df

df <- exam %>% arrange(class,math) # 오름차순 
df

# 문제 1 p.138
df <- mpg %>% select(class, cty)    # class, cty 변수 추출
head(df)                            # df 일부 출력
##     class cty
## 1 compact  18
## 2 compact  21
## 3 compact  20
## 4 compact  21
## 5 compact  16
## 6 compact  18

# 문제 2 p.138
df_suv <- df %>% filter(class == "suv")          # class가 suv인 행 추출
df_compact <- df %>% filter(class == "compact")  # class가 compact인 행 추출

mean(df_suv$cty)                                 # suv의 cty 평균
## [1] 13.5
mean(df_compact$cty)                             # compact의 cty 평균
## [1] 20.12766

# 문제 1 p.141
mpg %>% filter(manufacturer == "audi") %>%  # audi 추출
  arrange(desc(hwy)) %>%                    # hwy 내림차순 정렬
  head(5)                                   # 5행까지 출력
##   manufacturer      model displ year cyl      trans drv cty hwy fl   class
## 1         audi         a4   2.0 2008   4 manual(m6)   f  20  31  p compact
## 2         audi         a4   2.0 2008   4   auto(av)   f  21  30  p compact
## 3         audi         a4   1.8 1999   4   auto(l5)   f  18  29  p compact
## 4         audi         a4   1.8 1999   4 manual(m5)   f  21  29  p compact
## 5         audi a4 quattro   2.0 2008   4 manual(m6)   4  20  28  p compact



# mutate(파생 변수=..) : 파생변수를 추가한다

df <- exam %>% 
      mutate(total = math + english + science,
             mean = (math + english + science)/3 ) %>%
      arrange(desc(mean)) %>%
      head
df

df <- exam %>%
      mutate(test = ifelse(science >= 60,"pass","fail")) %>%
      head
df

df <- exam %>% 
  mutate(total = math + english + science,
         mean = (math + english + science)/3 ) %>%
  mutate(grade = ifelse(mean >= 90,"A",
                  ifelse(mean >=80,"B",
                    ifelse(mean >=70,"C",
                      ifelse(mean >= 60,"D","F"                                       ))))) %>%
  arrange(desc(mean)) %>%
  head(20)
View(df)


head(exam,10)
exam %>% head(10)

# 문제 1 p.144
mpg_new <- mpg                                    # 복사본 만들기
mpg_new <- mpg_new %>% mutate(total = cty + hwy)  # 합산 변수 만들기
View(mpg_new)

# 문제 2 p.144
mpg_new <- mpg_new %>% mutate(mean = total/2)     # 평균 변수 만들기
View(mpg_new)

# 문제 3 p.144
df <- mpg_new %>%
  arrange(desc(mean)) %>%  # 내림차순 정렬
  head(3)                  # 상위 3행 출력
View(df)

# 문제 4 p.144
mpg_new <- mpg %>%
  mutate(total = cty + hwy,   # 합산 변수 만들기
         mean = total/2) %>%  # 평균 변수 만들기
  arrange(desc(mean)) %>%     # 내림차순 정렬
  head(3)                     # 상위 3행 출력
mpg_new


# summarise() : 통계함수를 사용한 변수를 할당
result <- exam %>% summarise(mean_math = mean(math))
str(result)
dim(result)

# group_by() : 항목별로 데이터를 분리
df <- exam %>% 
  group_by(class) %>%
  summarise(mean_math=mean(math))
df

df <- exam %>% 
  group_by(class) %>%
  summarise(mean_math=mean(math),
            sum_math = sum(math),
            n  = n())
df

df <- mpg %>%
  group_by(manufacturer, drv) %>%
  summarise(mean_cty = mean(cty)) 
View(df)

# dplyr 조합 하기
df <- mpg %>%
        group_by(manufacturer) %>% # 제조업체별로 분리 
        filter(class=="suv") %>% # suv 만 추출
        mutate(tot = (cty+hwy)/2) %>%
        summarise(mean_tot=mean(tot)) %>%
        arrange(desc(mean_tot)) %>%
        head(5)
df
  
# <1>
df <- mpg %>%
  group_by(manufacturer) %>% # 제조업체별로 분리 
  filter(class=="suv")  # suv 만 추출
View(df  )
        
# <2>
df <- df %>% mutate(tot = (cty+hwy)/2) 
View(df )  

# <3>
df <- df %>% summarise(mean_tot=mean(tot)) 
df  

# <4>
df <- df %>% arrange(desc(mean_tot)) %>%
      head(5)
df

# 문제 1  p.150
mpg %>%
  group_by(class) %>%               # class별 분리
  summarise(mean_cty = mean(cty))   # cty 평균 구하기


# 문제 2  p.150
mpg %>%
  group_by(class) %>%                  # class별 분리
  summarise(mean_cty = mean(cty)) %>%  # cty 평균 구하기
  arrange(desc(mean_cty))              # 내림차순 정렬하기

# 문제 3  p.150
mpg %>%
  group_by(manufacturer) %>%           # manufacturer별 분리
  summarise(mean_hwy = mean(hwy)) %>%  # hwy 평균 구하기
  arrange(desc(mean_hwy)) %>%          # 내림차순 정렬하기
  head(3)                              # 상위 3행 출력

# 문제 4  p.150
mpg %>%
  group_by(manufacturer) %>%      # manufacturer별 분리
  filter(class == "compact") %>%  # compact 추출
  summarise(count = n()) %>%      # 빈도 구하기
  arrange(desc(count))            # 내림차순 정렬


# 데이터 합치기(join,merge,bind)

# (1) 가로=수평=열(column)로 합치기 
# left_join()
test1 <- data_frame(id=c(1,2,2,4,1),
               midterm = c(60,80,70,90,85))
test1

test2 <- data_frame(id=c(1,2,2,4,5),
                   final = c(70,83,65,95,80))
test2


total <- left_join(test1,test2, by='id' )
total

name <- data.frame(class=c(1,2,3,4,5),
  teacher=c("kim","lee","park","choi","jung"))
name

exam_new <- left_join(exam,name,by="class")
exam_new

# (2) 세로=수직=행(row)로 합치기 
# bind_rows()
group_a <- data.frame(id = c(1,2,3,4,5),
                     test=c(60,80,70,90,85))
group_a
group_b <- data.frame(id = c(6,7,8,9,10,11),
                     test=c(70,83,65,95,80,90))
group_b

group_all <- bind_rows(group_a,group_b)
group_all

# 문제 1

fuel <- data.frame(fl = c("c", "d", "e", "p", "r"),        price_fl = c(2.35, 2.38, 2.11, 2.76, 2.22),        stringsAsFactors = F)
fuel

mpg_new <- left_join(mpg,fuel,by = "fl" )
View(mpg_new)

# 문제 2
mpg_new %>%
  select(model,fl,price_fl) %>%
  head(5)

# 분석 도전   P 160

# 문제 1
# midwest에 백분율 변수 추가
midwest <- midwest %>%
  mutate(ratio_child = (poptotal-popadults)/poptotal*100)

# 문제 2
midwest %>%
  arrange(desc(ratio_child)) %>%   # ratio_child 내림차순 정렬
  select(county, ratio_child) %>%  # county, ratio_child 추출
  head(5)                          # 상위 5행 출력

# 문제 3
# midwest에 grade 변수 추가
midwest <- midwest %>%
  mutate(grade = ifelse(ratio_child >= 40, "large",
                    ifelse(ratio_child >= 30, "middle", "small")))

# 미성년 비율 등급 빈도표
table(midwest$grade)

# 문제 4
midwest %>%
  mutate(ratio_asian = (popasian/poptotal)*100) %>%  # 백분율 변수 추가
  arrange(ratio_asian) %>%                           # 오름차순 정렬
  select(state, county, ratio_asian) %>%             # 변수 추출
  head(10)                                           # 상위 10행 출력 


