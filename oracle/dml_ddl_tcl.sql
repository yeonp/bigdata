-- DML : INSERT / UPDATE / DELETE

-- 테이블 사본을 하나 생성
CREATE TABLE DEPT_TEMP
    AS SELECT * FROM DEPT;

SELECT * FROM DEPT_TEMP;

-- INSERT INTO ~ : 테이블에 행을 추가
INSERT INTO DEPT_TEMP
        VALUES (60,'NETWORK','TAEJEON' );
        
INSERT INTO DEPT_TEMP
        VALUES (70,'SCHOOL','SEOUL' );

INSERT INTO DEPT_TEMP
        VALUES (80,NULL,NULL);

SELECT * FROM DEPT_TEMP;        

-- DELETE FROM ~: 테이블에서 행을 삭제
DELETE FROM DEPT_TEMP
    WHERE DNAME = 'NETWORK';

DELETE FROM DEPT_TEMP
    WHERE LOC = 'SEOUL';

SELECT * FROM DEPT_TEMP; 

-- UPDATE ~ SET ~: 테이블의 데이터를 수정
UPDATE  DEPT_TEMP
     SET  DNAME = 'DATABASE',
          LOC = 'SEOUL'
    WHERE DEPTNO = 60;

-- TCL
-- 트랜잭션을 모두 완료
COMMIT;

-- 트랜잭션을 모두 취소
ROLLBACK;

-- DDL  : CREATE/DROP/ALTER/TRUNCATE/RENAME

-- 테이블 생성
CREATE TABLE EMP_DDL (
    EMPNO    NUMBER(4) PRIMARY KEY, -- NN과 UNIQUE를 포함
    ENAME    VARCHAR2(10) NOT NULL,  -- NULL데이터를 사용하지 않음
    JOB      VARCHAR2(9) UNIQUE, --중복을 허용하지 않음
    HIREDATE DATE,
    SAL      NUMBER(7,2), --전체 7자리,소수점은 2자리, 12345.67
    DEPNO    NUMBER(5) DEFAULT 0
);

DESC EMP_DDL;  


-- ALTER 테이블을 변경
ALTER TABLE EMP_DDL
    ADD HP VARCHAR2(20);  -- 테이블에 새로운 열을 추가

ALTER TABLE EMP_DDL
    RENAME COLUMN HP TO TEL; -- 열이름을 변경
    
ALTER TABLE EMP_DDL
    DROP COLUMN TEL; -- 테이블에서 열을 삭제


-- 테이블에 데이터를 모두 삭제
TRUNCATE TABLE DEPT_TEMP;
SELECT * FROM DEPT_TEMP; 
  
--테이블 삭제
DROP TABLE EMP_DDL;

DESC EMP_DDL; --> 오류

-- 테이블 이름 바꾸기
RENAME DEPT_TEMP TO DEPT_RENAME;

DESC DEPT_TEMP;  

DESC DEPT_RENAME;  

