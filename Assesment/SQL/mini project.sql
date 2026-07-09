create database miniproject;
use miniproject;

--try 1

SELECT category, AVG(discount), AVG(profit)
FROM superstore GROUP BY category;

-- try 2
SELECT category, SUM(profit)
FROM superstore GROUP BY category
HAVING SUM(profit) < 100;

-- try 3
SELECT * FROM superstore
	WHERE discount > 0.50 AND profit < 0
    LIMIT 5 ;

-- total sale and profit
SELECT region, SUM(Sales), SUM(Profit)
FROM superstore GROUP BY region
ORDER BY Total_Profit DESC;

-- category performance
SELECT	category, SUM(Sales), SUM(Profit)
FROM superstore GROUP BY category;

--loss making transactions
SELECT	Order_ID , Product_Name, category, region, 
    sales, discount, profit
    FROM superstore
    WHERE profit < 0
    ORDER BY profit
    LIMIT 10;