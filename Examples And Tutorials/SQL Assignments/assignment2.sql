-- Query for Question 1 starts
CREATE TABLE hotel (
    hno NUMBER(3) PRIMARY KEY,
    name VARCHAR2(30),
    address VARCHAR2(20)
);

CREATE TABLE room (
    rno NUMBER(5) PRIMARY KEY,
    rtype VARCHAR2(20),
    hno NUMBER(3),
    price NUMBER(5) CHECK(price > 500),
    FOREIGN KEY(hno) REFERENCES hotel(hno) ON DELETE CASCADE
);

CREATE TABLE guest(
    gno NUMBER(6) PRIMARY KEY,
    gname VARCHAR2(30),
    gaddress VARCHAR2(30)
);

CREATE TABLE booking (
    hno NUMBER(4),
    gno NUMBER(6),
    rno NUMBER(5),
    FOREIGN KEY(hno) REFERENCES hotel(hno) ON DELETE CASCADE,
    FOREIGN KEY(gno) REFERENCES guest(gno) ON DELETE CASCADE,
    FOREIGN KEY(rno) REFERENCES room(rno) ON DELETE CASCADE
);
-- Question 1 ends


-- Query for Question 2 starts
INSERT INTO hotel VALUES (1, "Sea Hawks", "Mumbai");
INSERT INTO hotel VALUES (2, "Sagar Sangam", "Chennai");
INSERT INTO hotel VALUES (3, "Green View", "Kolkata");
INSERT INTO hotel VALUES (4, "Sunshine", "Delhi");
INSERT INTO hotel VALUES (5, "Taj", "Kolkata");

INSERT INTO  room VALUES (3, "3BEDNOAC", 1, 1000);
INSERT INTO  room VALUES (1, "3BEDAC", 2, 1600);
INSERT INTO  room VALUES (2, "2BEDAC", 3, 1500);
INSERT INTO  room VALUES (5, "2BEDNONAC", 4, 900);
INSERT INTO  room VALUES (4, "3BEDAC", 5, 1600);
INSERT INTO  room VALUES (6, "3BEDAC", 5, 1300);

INSERT INTO guest VALUES (1, "Akash", "ABC");
INSERT INTO guest VALUES (2, "Sagar", "DEF");
INSERT INTO guest VALUES (3, "Nadi", "GHI");
INSERT INTO guest VALUES (4, "Tusar", "JKL");
INSERT INTO guest VALUES (5, "Giri", "MNO");
INSERT INTO guest VALUES (6, "Mihir", "PQR");

INSERT INTO booking VALUES (1, 1, 3);
INSERT INTO booking VALUES (2, 2, 1);
INSERT INTO booking VALUES (3, 3, 2);
INSERT INTO booking VALUES (4, 4, 5);
INSERT INTO booking VALUES (5, 5, 1);
INSERT INTO booking VALUES (5, 6, 2);

-- Question 2 ends

-- Question 3 starts
SELECT gname FROM guest WHERE gno IN (
    SELECT gno FROM booking WHERE hno IN (
        SELECT hno FROM hotel WHERE address IN ('Kolkata', 'Chennai')
    )
);

SELECT COUNT(gno) FROM booking WHERE hno = (
    SELECT hno FROM hotel WHERE name = "Taj"
);

SELECT hno,COUNT(*) FROM room GROUP BY hno;
-- Question 3 ends

-- Question 4 starts
ALTER TABLE booking ADD date_from DATE; ALTER TABLE booking ADD date_to DATE;

DELETE FROM booking WHERE hno = 5;

UPDATE guest SET gaddress='XYZ' WHERE gno = 3;

DROP TABLE hotel; DROP TABLE room; DROP TABLE guest; DROP TABLE booking;
-- Question 4 ends
