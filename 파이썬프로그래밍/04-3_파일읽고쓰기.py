# 04-3_파일읽고쓰기.py

# open()/read()/write()/close()

# 파일객체 = open('파일명','옵션')

# f = open('C:/Users/CPB02GameN/Desktop/file.txt','w')
             # 파일 경로는 '/' 로 표시한다

f = open('file.txt','w') # 쓰기모드, 없으면 생성
                         # 있으면 삭제(주의)
f.write('1번째 줄입니다')
f.write('2번째 줄입니다')
f.write('3번째 줄입니다')
f.close()

f = open('file.txt','r') # 읽기 모드, 쓰기 불가능
# print(type(f))
result = f.read()
print(result)
f.close()

f = open('file.txt','a') # 추가모드, 없으면 생성
                         # 있쓰면 내용을 끝에 추가
f.write('4번째 <추가> 줄입니다')
f.close()


f = open('file_line.txt','w')
for k in range(1,101):
    data = '{:>3} 번째 줄입니다\n'.format(k)
    f.write(data)
f.close()

#파일을 line 단위로 읽기 , 읽기 종료를 자동으로 처리
f = open('file_line.txt','r')
while True:
    line = f.readline()
    if not line : break
    print(line,end='')
f.close()

f = open('file_line.txt','r')
lines = f.readlines()  #모든 줄을 다 읽고 리스트로 반환
print(lines)
for line in lines:
    print(line,end='')

# for k in range(len(lines)):
#     print(lines[k],end = '')
f.close()

# with 문 사용
# with 함수() as 객체:
# with문 범위내에서만 객체가 유효
# with문 종료시 객체는 삭제됨
with open('file_line.txt','r') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line, end='')


# CoffeeshopSales.txt 실습
# with open('CoffeeshopSales.txt','r',encoding='UTF-8') as f:
#     while True :
#         line = f.readline()
#         if not line: break
#         print(line, end='')

with open('CoffeeshopSales.txt','r',encoding='UTF-8') as f:
    for line in f:
        print(line, end='')

print()
with open('CoffeeshopSales.txt','r',encoding='UTF-8') as f:
    header =  f.readline()
    # print(type(header))  # <class 'str'>
    header_list = header.split()
    data_list = []
    date = []
    espresso = []
    americano = []
    cafelatte = []
    cappucino = []
    while True:
        line = f.readline()
        if not line: break
        row = line.split()
        data_list.append(row)
        date.append(row[0])
        espresso.append(int(row[1]))
        americano.append(int(row[2]))
        cafelatte.append(int(row[3]))
        cappucino.append(int(row[4]))

    print(header_list) # ['날짜', '에스프레소', '아메리카노', '카페라테', '카푸치노']
    print('날짜:',date)
    print('에스프레소:',espresso,'판매량:',sum(espresso),
          ' 평균:', sum(espresso)/len(espresso))
    print('아메리카노:',americano,'판매량:',sum(americano),
          ' 평균:', sum(americano)/len(americano))
    print('카페라테:',cafelatte,'판매량:',sum(cafelatte),
          ' 평균:', sum(cafelatte)/len(cafelatte))
    print('카푸치노:',cappucino,'판매량:',sum(cappucino),
          ' 평균:', sum(cappucino)/len(cappucino))




