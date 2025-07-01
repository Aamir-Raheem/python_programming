#1.  How many products are "Own Brand" vs "Distribution"?
SELECT COUNT(product_type)
FROM sales.products
WHERE product_type = 'Distribution';

#2. List all markets and the zones they belong to
SELECT markets_name, zone
FROM sales.markets;

#3. Find all markets where the zone is missing (i.e., NULL).
SELECT *
FROM sales.markets
WHERE zone = '';

#4. Show all customer IDs and their corresponding product codes
SELECT product_code, customer_code
FROM sales.transactions;

#5. Join transactions with customers to show customer names and their transactions.
SELECT *
FROM sales.customers
INNER JOIN sales.transactions
 ON transactions.customer_code = customers.customer_code;

#6. Join transactions, products, and markets to show: Product type, Market name, Customer ID
SELECT products.product_type, markets.markets_name, transactions.customer_code 
FROM products
INNER JOIN transactions
 ON transactions.product_code = products.product_code
INNER JOIN markets
 ON transactions.market_code = markets.markets_code;

#7. Show each customer along with the zone they purchased from (requires joining markets).
SELECT customers.custmer_name, markets.zone 
FROM markets 
INNER JOIN transactions 
 ON markets.markets_code = transactions.market_code
INNER JOIN customers
 ON customers.customer_code = transactions.customer_code;

#8. Count the number of transactions per product.
SELECT product_code, COUNT(*) AS transaction_count
FROM sales.transactions
GROUP BY product_code;

#9. Find the top 3 most sold products.
SELECT transactions.product_code, COUNT(*) AS transactions
FROM transactions
GROUP BY product_code
ORDER BY transactions
DESC LIMIT 3;

#10. Find total number of customers in each zone.
SELECT COUNT(DISTINCT(transactions.customer_code)) AS customers, markets.zone
FROM markets
INNER JOIN transactions 
 ON transactions.market_code = markets.markets_code
GROUP BY markets.zone;

#11. Group customers by product type and count how many bought each.
SELECT COUNT(DISTINCT transactions.customer_code), products.product_type  
FROM transactions 
INNER JOIN products
 ON transactions.product_code = products.product_code
GROUP BY products.product_type;

#12. How many transactions took place per month?
SELECT date.month_name, COUNT(transactions.sales_qty) AS orders
FROM sales.date
INNER JOIN transactions
 ON transactions.order_date = date.date
GROUP BY date.month_name; 

#13. Check for missing zones in markets.
SELECT markets_name, zone
FROM markets 
WHERE zone = '';

#14. Check if any product_code in transactions doesn’t exist in products.
SELECT transactions.product_code AS TransactionsCode, products.product_code AS ProductsCode
FROM products 
RIGHT JOIN transactions 
 ON transactions.product_code = products.product_code
WHERE products.product_code IS NULL; # answer is yes

#15. Check if any market_code in transactions doesn’t exist in markets.
SELECT transactions.market_code AS TransactionsCode, markets.markets_code AS MarketsCode
FROM markets
RIGHT JOIN transactions 
 ON transactions.market_code = markets.markets_code
WHERE markets.markets_code IS NULL; #answer is no

#16. List all distinct product_type values — watch for dirty data.
SELECT DISTINCT products.product_type 
FROM products;

#17. Which product type (Own Brand vs Distribution) generates more transactions?
SELECT products.product_type, COUNT(*) AS Transactions
FROM transactions
INNER JOIN products ON transactions.product_code = products.product_code 
GROUP BY products.product_type #based on output, Own brand has more number of transactions than distribution