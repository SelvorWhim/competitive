SELECT Name as 'Customers' FROM Customers
WHERE Id IN
    (SELECT Customers.Id
    FROM (Customers LEFT JOIN Orders
                    ON Customers.Id = Orders.CustomerId)
    WHERE Orders.CustomerId IS NULL);
