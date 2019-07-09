-- Question 1 starts
CREATE TABLE shop (
    shop_no VARCHAR2(5) PRIMARY KEY,
    shop_name VARCHAR2(30),
    owner_name VARCHAR2(30)
);

CREATE TABLE customer (
    cust_no VARCHAR2(5) PRIMARY KEY,
    cust_name VARCHAR2(30),
    cust_addr VARCHAR2(50)
);

CREATE TABLE sale (
    cust_no VARCHAR2(5),
    shop_no VARCHAR2(5),
    item VARCHAR2(30),
    price NUMBER(10, 2) CHECK (price > 0),
    FOREIGN KEY(cust_no) REFERENCES customer(cust_no) ON DELETE CASCADE,
    FOREIGN KEY(shop_no) REFERENCES shop(shop_no) ON DELETE CASCADE
);
-- Question 1 ends

-- Question 2 starts
INSERT INTO shop VALUES ("S1", "Readymade Center", "Jiban Krishna Saha");
INSERT INTO shop VALUES ("S2", "Adi Readymande Center", "Narayan Chandra Saha");
INSERT INTO shop VALUES ("S3", "Sri Niketan", "Nityananda Aich");

INSERT INTO customer VALUES ("C1", "Juli", "ABC");
INSERT INTO customer VALUES ("C2", "Nisha", "DEF");
INSERT INTO customer VALUES ("C3", "Puja", "GHI");
INSERT INTO customer VALUES ("C4", "Sonia", "JKL");

INSERT INTO sale VALUES ("C1", "S2", "Sari", 10000);
INSERT INTO sale VALUES ("C1", "S3", "Frock", 5000);
INSERT INTO sale VALUES ("C2", "S3", "Pant", 2000);
INSERT INTO sale VALUES ("C2", "S3", "Shirt", 2000);
INSERT INTO sale VALUES ("C3", "S1", "Churidar", 6000);
INSERT INTO sale VALUES ("C3", "S3", "Kurti", 2000);
-- Question 2 ends

-- Question 3 starts
SELECT shop_name, owner_name FROM shop;
SELECT cust_name FROM customer WHERE cust_no IN (
    SELECT cust_no FROM sale WHERE shop_no = (
        SELECT shop_no FROM shop WHERE shop_name = "Sri Niketan"
    )
);
SELECT c.cust_name FROM customer c, sale s WHERE s.item = "Churidar" AND s.cust_no = c.cust_no;
SELECT c.cust_name, SUM(s.price) FROM customer c, sale s WHERE c.cust_no = s.cust_no GROUP BY s.cust_no;
SELECT shop_name FROM shop WHERE shop_no IN (SELECT shop_no FROM sale WHERE item = "Pant");
-- Question 3 ends

-- Question 4 starts
ALTER TABLE shop ADD shop_adress VARCHAR2(20);
DELETE FROM shop WHERE shop_name = "Sri Niketan";
UPDATE customer SET cust_addr = "XYZ" WHERE cust_no = "C1";
DROP TABLE sale; DROP TABLE customer; DROP TABLE shop;
