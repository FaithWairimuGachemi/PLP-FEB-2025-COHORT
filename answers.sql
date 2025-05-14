--Question 1
SELECT paymentDate, SUM(amount) AS totalPayment
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;

--Question 2
SELECT customerName, country, AVG(creditLimit) AS averageCreditLimit
FROM customers
GROUP BY customerName, country;


--Question 3
SELECT productCode, quantityOrdered, SUM(priceEach * quantityOrdered) AS totalPrice
FROM orderdetails
GROUP BY productCode, quantityOrdered;

--Question 4
SELECT checkNumber, MAX(amount) AS highestPayment
FROM payments
GROUP BY checkNumber;