
pip install numpy pandas matplotlib scipy seaborn sklearn

-------------------------------------------------
한국지도에 대해 json 파일:

https://github.com/southkorea/southkorea-maps


대한민국 시군 지역별 위도와 경도
http://blog.daum.net/fecjf/56

===================================

- 파이썬을 이용한 데이터분석 교재 예제 소스:

Python-Data-Analysis-Second-Edition-master_translation.zip


- matplotlib와 pandas 플로팅 기본 예제:

matplot_pandas.zip


- Folium/Seaborn 시각화 예제:

DataScience-master.zip

===================================

- UCI Machine Learning Repository
    
    https://archive.ics.uci.edu/ml/index.php



=================================
- merge() 예제 리스트 데이터셋

employee = [{'empno':1, 'ename':'kim', 'dept':1}, 

            {'empno':2, 'ename':'lee', 'dept':2}, 
            {'empno':3, 'ename':'park', 'dept':1}, 
            {'empno':4, 'ename':'song', 'dept':3},
            {'empno':5, 'ename':'min', 'dept':2} ]
            

dept=[{'dept':1, 'deptname':'관리직'}, 

      {'dept':2, 'deptname':'영업직'},
      {'dept':3, 'deptname':'개발직'} ]

info =[{'empno':1, 'addr':'서울시','phone':'010-1111-1111'},

       {'empno':3, 'addr':'부산시','phone':'010-2222-2222'}, 
       {'empno':2, 'addr':'광주시','phone':'010-3333-3333'}, 
       {'empno':5, 'addr':'광주시','phone':'010-4444-4444'},
       {'empno':4, 'addr':'광주시','phone':'010-5555-5555'} ]
       
=================================
- grouby() 와 pivot_table() 예제 데이터셋

from numpy.random import seed

from numpy.random import ran

from numpy.random import randint

seed(42)

df = pd.DataFrame({
   'Weather' : ['cold', 'hot', 'cold', 'hot',
   'cold', 'hot', 'cold'],
   
   'Food' : ['soup', 'soup', 'icecream', 'chocolate',
   'icecream', 'icecream', 'soup'],
   
   'Price' : 10 * rand(7), 'Number' : randint(1, 9, 7)})
