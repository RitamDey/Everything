CREATE TABLE hotel (
    hno NUMBER(3) PRIMARY KEY,
    name VARCHAR2(30),
    address VARCHAR2(20)
);

CREATE TABLE room (
    rno NUMBER(5) PRIMARY KEY,
    rtype VARCHAR2(20),
    price NUMBER(5) CHECK(price > 500),
    hno NUMBER(3),
    FOREIGN KEY(hno) REFERENCES hotel(hno)
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
    FOREIGN KEY(hno) REFERENCES hotel(hno),
    FOREIGN KEY(gno) REFERENCES guest(gno),
    FOREIGN KEY(rno) REFERENCES room(rno)
);
