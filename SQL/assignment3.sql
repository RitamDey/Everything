-- Question 1 starts
CREATE TABLE team (
    jersy_no NUMBER(2),
    player_name VARCHAR2(20) PRIMARY KEY,
    team VARCHAR2(20)
);

CREATE TABLE run (
    player_name VARCHAR2(20),
    against VARCHAR2(20),
    run NUMBER(2) CHECK (run >= 0),
    FOREIGN KEY (player_name) REFERENCES team(player_name) ON DELETE CASCADE
);
-- Question 1 ends

-- Question 2 starts
INSERT INTO team VALUES (11, "Tendulkar", "India");
INSERT INTO team VALUES (23, "Mendis", "Sri Lanka");
INSERT INTO team VALUES (15, "Akram", "Pakistan");

INSERT INTO run VALUES ("Tendulkar", "Sri Lanka", 89);
INSERT INTO run VALUES ("Mendis", "India", 58);
INSERT INTO run VALUES ("Tendulkar", "Pakistan", 80);
INSERT INTO run VALUES ("Akram", "India", 58);
INSERT INTO run VALUES ("Akram", "Sri Lanka", 38);
INSERT INTO run VALUES ("Mendis", "Pakistan", 38);
-- Question 2 ends

-- Question 3 starts
SELECT player_name FROM team WHERE player_name LIKE "_e%";
SELECT SUM(run) FROM run WHERE player_name = "Tendulkar";
SELECT jersy_no, player_name, team FROM team ORDER BY jersy_no;
SELECT player_name, run FROM run WHERE run = (SELECT MAX(run) FROM run WHERE against = "India");
SELECT player_name, MAX(run) FROM run WHERE player_name IN (SELECT player_name FROM run WHERE against = "India" INTERSECT SELECT player_name FROM run WHERE against = "Sri Lanka");
SELECT SUM(run) FROM run WHERE against = "India";
SELECT player_name FROM run WHERE against = "India";
-- Question 3 ends

-- Question 4 starts
ALTER TABLE team ADD age NUMBER(2);
DELETE FROM run WHERE against = "India";
UPDATE team SET jersy_no = 24 WHERE player_name = "Mendis";
DROP TABLE team; DROP TABLE run;
-- Question 4 ends
