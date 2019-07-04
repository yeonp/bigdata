# 02장 연습문제풀이.py

# Q1
a = 80
b = 75
c = 55
avg = (a+b+c)/3
print(avg)

# Q2
num = 13
even_odd = ['짝수','홀수']
print("%d : %s"%(num,even_odd[num % 2]))

# Q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)  # 881120 출력
print(num)       # 1068234 출력

# Q4
gender = [ '남자', '여자']
pin = "881120-1068234"
print(gender[int(pin[7]) - 1] )
# 1이면 남자, 2이면 여자

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort( )
a.reverse( )
print(a)       # [5, 4, 3, 2, 1] 출력

# Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# Q8
a = (1, 2, 3)
a = a + (4,)
print(a)       # (1, 2, 3, 4) 출력

# Q9
a = dict()

a['name'] = 'python'
a[('a')] = 'python'
#a[[1]] = 'python' # TypeError: unhashable type: 'list'
a[250] = 'python'

# Q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)            # {'A':90, 'C':70} 출력
print(result)       # 80 출력

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     # a 리스트를 집합자료형으로 변환
b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
print(b)          # [1,2,3,4,5] 출력

# Q12
a = b = [ 1,2,3 ]
a[1] = 4
print(b)  # [1, 4, 3]
print(id(a) == id(b)) # 객체의 참조주소가 서로 같다
print(hex(id(a)),hex(id(b)))
