--query to retrieve
SELECT checkNumber, paymentDate, amount
FROM payments;

--query to retrive and sort
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

--query to display selected and sort
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

--query to retrieve all
SELECT *
FROM offices;

--query to fetch with limits
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;