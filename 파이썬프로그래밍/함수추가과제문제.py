# 함수추가과제문제.py

# 1번
print('{0:=^50}'.format(' 1번 '))
def calc_fat_ratio(height,weight):
    std_weight = (height  - 100) * 0.85
    fat_ratio = (weight/std_weight)*100
    if fat_ratio <= 90:
        fat_grade = '저체중'
    elif fat_ratio > 90 and fat_ratio <= 110:
        fat_grade = '정상'
    elif fat_ratio > 110 and fat_ratio <= 120:
        fat_grade = '과체중'
    else:
        fat_grade = '비만'
    return fat_ratio,fat_grade

def get_health_info():
    height = int(input('Your Height(cm):'))
    weight = int(input('Your Weight(kg):'))
    fat_ratio,fat_grade = calc_fat_ratio(height,weight)
    print('키 : {0:3}cm  몸무게: {1:3}kg'.format(height,weight))
    print('비만도 : {0:>5.1f}% ({1})'.format(fat_ratio,fat_grade))

# get_health_info()

# 2번
def get_leap_year(year):

    if (year % 4 == 0 and year % 100 !=0) \
            or (year % 400 == 0):
        return '윤년'
    return '평년'

def get_age(year,current_year):
    age = current_year - year + 1
    return age

# 12지
# 子(자/쥐) 丑(축/소) 寅(인/호랑이) 卯(묘/토끼)
# 辰(진/용) 巳(사/뱀) 午(오/말) 未(미/양)
# 申(신/원숭이) 酉(유/닭) 戌(술/개) 亥(해/돼지).
# 서기 4년  : 子(자/쥐)

def get_12_animals(year):
    animals = ['子(자/쥐)',  '丑(축/소)', '寅(인/호랑이)',
               '卯(묘/토끼)','辰(진/용)', '巳(사/뱀)',
               '午(오/말)',  '未(미/양)', '申(신/원숭이)',
               '酉(유/닭)',  '戌(술/개)', '亥(해/돼지)']
    idx = (year - 4)%12
    return animals[idx]

def get_year_info():
    while True:
        print('-'*30)
        current_year = 2019
        year = int(input('year(0 to quit):'))
        if year == 0 : break
        if year < 0 : continue
        print(year,'year :',get_leap_year(year))
        print('age :', get_age(year,current_year))
        print('animal :', get_12_animals(year))

# get_year_info()


# 3번
def get_grade(score):
    d = {'90~100':'A','80~89':'B','70~79':'C',
         '60~69':'D','0~59':'F'}
    if score >=90 and score <= 100:
        grade = d['90~100']
    elif score >=80 and score < 90:
        grade = d['80~89']
    elif score >=70 and score < 80:
        grade = d['70~79']
    elif score >=60 and score < 70:
        grade =  d['60~69']
    else:
        grade = d['0~59']
    return grade

def get_score_grade():
    while True:
        score = int(input('score(-1 to quit)='))
        if score < 0 : break
        print(score,':',get_grade(score))
# get_score_grade()

# 4번
def get_mile(meter):
    if meter < 0 :
        return
    mile = meter / 1.609
    return mile
def input_meter_to_mile():
    while True:
        meter = float(input('meter(-1 to quit)='))
        if meter < 0 : break
        print(meter,'meter:{:6.2f}'.format(get_mile(meter)),'miles')

# input_meter_to_mile()

# 5번
def get_celsius(fahrenheit):
    celsius = ( fahrenheit - 32 ) / 1.8
    return celsius

def input_fahrenheit_to_celsius():
    fahrenheit = float( input( 'Input fahrenheit : ' ) )
    celsius = get_celsius(fahrenheit)
    print( 'fahrenheit : {0:<6.2f} -> celsius : {1:<6.2f}'.format( fahrenheit, celsius ) )

# input_fahrenheit_to_celsius()

# 6번
def get_divisor(number):
    result = []
    for k in range(1,number + 1):
        remain = number % k
        if remain == 0:
            result.append(k)
    return result

def input_number_for_divisor():
    while True:
        number = int(input('number(0 to quit)='))
        if number == 0 : break
        print(number,':',get_divisor(number),
              len(get_divisor(number)),'개')

# input_number_for_divisor()

# 7번
def sum_abs(a,b):
    if a < 0 :
        a = a * -1
    if b < 0 :
        b = b * -1
    return a + b

def input_number_to_sum_abs():
    while True:
        number1 = int(input('number1(0 to quit)='))
        if number1 == 0 : break
        number2 = int(input('number20 to quit)='))
        if number2 == 0 : break
        print(number1,'and',number2,'==>',sum_abs(number1,number2))

# input_number_to_sum_abs()

# 8번
def mymap(func,var_list):
    result_list = []
    for k in var_list:
        result_list.append(func(k))
    return result_list

def multi_two(x):
    return x*2

# print(mymap(multi_two,[1,2,3,4,5,6]))