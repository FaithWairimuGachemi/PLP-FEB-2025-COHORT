--Question 1
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

--question 2
INSERT INTO student (id, fullName, age) 
VALUES 
(1, 'Faith ', 25),
(2, 'Mary', 35),
(3, 'Simon', 45);

--question 3
UPDATE student
SET age = 25
WHERE id = 3;