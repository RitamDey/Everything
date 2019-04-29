-- Part 1 starts
CREATE TABLE dept (
        deptno NUMBER(2) PRIMARY KEY,
        deptname VARCHAR2(14)
);

CREATE TABLE emp (
        empno NUMBER(4) PRIMARY KEY,
        empname VARCHAR2(10),
        city VARCHAR2(20),
        sal NUMBER(7, 2) CHECK (sal > 10000),
        deptno NUMBER(2),
        FOREIGN KEY(deptno) REFERENCES dept(deptno) ON DELETE CASCADE
);
--Part 1 ends

-- Part 2 starts
INSERT INTO dept VALUES (10, "Accounting");
INSERT INTO dept VALUES (20,  "Research");
INSERT INTO dept VALUES (30, "Sales");
INSERT INTO dept VALUES (40, "Operations");

INSERT INTO emp VALUES (7369, "SMITH", "NEW YORK", 18000, 20);
INSERT INTO emp VALUES (7499, "ALLEN", "CHICAGO", 16000, 30);
INSERT INTO emp VALUES (7521, "WARD", "DALLAS", 12500, 30);
INSERT INTO emp VALUES (7566, "JONES", "NEW YORK", 29750, 20);
INSERT INTO emp VALUES (7654, "MARTIN", "DALLAS", 14000, 30);
INSERT INTO emp VALUES (7698, "BLAKE", "CHICAGO", 28500, 30);
INSERT INTO emp VALUES (7782, "CLARK", "NEW YORK", 24500, 10);
INSERT INTO emp VALUES (7788, "SCOTT", "CHICAGO", 30000, 20);
INSERT INTO emp VALUES (7839, "KING", "BOSTON", 50000, 10);
INSERT INTO emp VALUES (7844, "TURNER", "CHICAGO", 15000, 20);
INSERT INTO emp VALUES (7876, "ADAMS", "NEW YORK", 11000, 20);
INSERT INTO emp VALUES (7900, "JAMES", "DALLAS", 19500, 30);
INSERT INTO emp VALUES (7902, "FORD", "DALLAS", 30000, 20);
INSERT INTO emp VALUES (7934, "MILLER", "NEW YORK", 13000, 10);
-- Part 2 ends

-- Part 3 starts
SELECT city FROM emp WHERE deptno = (SELECT deptno FROM dept WHERE deptname="Research");
SELECT COUNT(*) FROM emp GROUP BY deptno;
SELECT empname FROM emp WHERE sal=(SELECT MAX(sal) FROM emp);
SELECT empname FROM emp WHERE empname LIKE "S%" OR empname LIKE "%S";
SELECT empname FROM emp WHERE deptno = 20;
-- Part 3 ends

-- Part 4 starts
UPDATE emp SET city = "New York" WHERE empno = 7499;
DELETE FROM emp WHERE sal > 25000;
ALTER TABLE dept ADD manager NUMBER(4);
DROP TABLE emp;
DROP TABLE dept;
-- Part 4 ends
