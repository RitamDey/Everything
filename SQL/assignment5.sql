-- Question 1 starts
CREATE TABLE employee (
    emp_name VARCHAR2(20) PRIMARY KEY,
    street VARCHAR2(20),
    city VARCHAR2(20)
);

CREATE TABLE company (
    co_name VARCHAR2(20) PRIMARY KEY,
    city VARCHAR2(20)
);

CREATE TABLE works (
    emp_name VARCHAR2(20),
    co_name VARCHAR2(20),
    salary NUMBER(8, 2) CHECK (salary >= 10000),
    FOREIGN KEY(emp_name) REFERENCES employee(emp_name) ON DELETE CASCADE,
    FOREIGN KEY(co_name) REFERENCES company(co_name) ON DELETE CASCADE
);
-- Question 1 ends

-- Question 2 starts
INSERT INTO employee VALUES ("X", "MG Road", "Kolkata");
INSERT INTO employee VALUES ("Susmita", "Ripon Street", "Howrah");
INSERT INTO employee VALUES ("Santanu", "Middleton Street", "Barackpore");
INSERT INTO employee VALUES ("Swaswati", "SP Street", "Asansol");
INSERT INTO employee VALUES ("Manpreet", "AJC Bose Road", "Kolkata");
INSERT INTO employee VALUES ("Tia", "Club Road", "Darjeeling");

INSERT INTO company VALUES ("XYZ", "Kolkata");
INSERT INTO company VALUES ("TCS", "Kolkata");
INSERT INTO company VALUES ("IBM", "Kolkata");

INSERT INTO works VALUES ("X", "XYZ", 25000);
INSERT INTO works VALUES ("Susmita", "IBM", 23000);
INSERT INTO works VALUES ("Santanu", "IBM", 10000);
INSERT INTO works VALUES ("Swaswati", "TCS", 21000);
INSERT INTO works VALUES ("Manpreet", "TCS", 12000);
INSERT INTO works VALUES ("Tia", "XYZ", 21000);

-- Question 3 starts
SELECT e.emp_name FROM employee e, company c WHERE e.city = c.city;
SELECT city FROM company WHERE co_name = (SELECT co_name FROM works WHERE emp_name = "X");
SELECT emp_name, city FROM employee WHERE emp_name IN (SELECT emp_name FROM works WHERE co_name = "XYZ");
SELECT emp_name FROM works WHERE salary IN (25000, 23000, 21000);
SELECT emp_name FROM employee WHERE LENGTH(emp_name) = 7 AND emp_name LIKE "__S%";
-- Question 3 ends

-- Question 4 starts
ALTER TABLE company ADD company_owner VARCHAR2(20);
DELETE FROM company WHERE co_name = "XYZ";
UPDATE employee SET city = "Hoogly" WHERE emp_name = "X";
DROP TABLE company; DROP TABLE employee; DROP TABLE works;
-- Question 4 ends
