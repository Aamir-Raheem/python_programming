
#  Sales Data Analysis Using SQL

##  Objective
The purpose of this project is to explore and analyze sales-related data using SQL. The goal is to gain insights into product performance, customer behavior, and market distribution across zones.

##  Dataset Overview

- **products**  contains `product_code` and `product_type` (`Own Brand`, `Distribution`)
- **transactions**  links customers and products with quantity and order date
- **customers**  customer details like `customer_code`, `customer_name`
- **markets**  includes `markets_code`, `markets_name`, and `zone`
- **date**  structured calendar breakdown (e.g., `date`, `month_name`, etc.)

##  Key SQL Questions & Queries

### 1. How many products are "Own Brand" vs "Distribution"?
```sql
SELECT COUNT(product_type)
FROM sales.products
WHERE product_type = 'Distribution';
```

### 2. List all markets and the zones they belong to
```sql
SELECT markets_name, zone
FROM sales.markets;
```

### 3. Find all markets where the zone is missing (i.e., empty string)
```sql
SELECT *
FROM sales.markets
WHERE zone = '';
```

### 4. Show all customer IDs and their corresponding product codes
```sql
SELECT product_code, customer_code
FROM sales.transactions;
```

### 5. Join transactions with customers to show customer names and their transactions
```sql
SELECT *
FROM sales.customers
INNER JOIN sales.transactions
  ON transactions.customer_code = customers.customer_code;
```

### 6. Join transactions, products, and markets to show: product type, market name, customer ID
```sql
SELECT products.product_type, markets.markets_name, transactions.customer_code 
FROM sales.products
INNER JOIN sales.transactions
  ON transactions.product_code = products.product_code
INNER JOIN sales.markets
  ON transactions.market_code = markets.markets_code;
```

### 7. Show each customer along with the zone they purchased from
```sql
SELECT customers.customer_name, markets.zone 
FROM sales.markets 
INNER JOIN sales.transactions 
  ON markets.markets_code = transactions.market_code
INNER JOIN sales.customers
  ON customers.customer_code = transactions.customer_code;
```

### 8. Count the number of transactions per product
```sql
SELECT product_code, COUNT(*) AS transaction_count
FROM sales.transactions
GROUP BY product_code;
```

### 9. Find the top 3 most sold products
```sql
SELECT product_code, COUNT(*) AS transactions
FROM sales.transactions
GROUP BY product_code
ORDER BY transactions DESC
LIMIT 3;
```

### 10. Find the total number of customers in each zone
```sql
SELECT COUNT(DISTINCT transactions.customer_code) AS customers, markets.zone
FROM sales.markets
INNER JOIN sales.transactions 
  ON transactions.market_code = markets.markets_code
GROUP BY markets.zone;
```

### 11. Group customers by product type and count how many bought each
```sql
SELECT COUNT(DISTINCT transactions.customer_code) AS customer_count, products.product_type  
FROM sales.transactions 
INNER JOIN sales.products
  ON transactions.product_code = products.product_code
GROUP BY products.product_type;
```

### 12. How many transactions took place per month?
```sql
SELECT date.month_name, COUNT(transactions.sales_qty) AS orders
FROM sales.date
INNER JOIN sales.transactions
  ON transactions.order_date = date.date
GROUP BY date.month_name;
```

### 13. Check for missing zones in markets
```sql
SELECT markets_name, zone
FROM sales.markets 
WHERE zone = '';
```

### 14. Check if any product_code in transactions doesnt exist in products
```sql
SELECT transactions.product_code AS TransactionsCode, products.product_code AS ProductsCode
FROM sales.products 
RIGHT JOIN sales.transactions 
  ON transactions.product_code = products.product_code
WHERE products.product_code IS NULL;
-- Answer: Yes, there are mismatches
```

### 15. Check if any market_code in transactions doesnt exist in markets
```sql
SELECT transactions.market_code AS TransactionsCode, markets.markets_code AS MarketsCode
FROM sales.markets
RIGHT JOIN sales.transactions 
  ON transactions.market_code = markets.markets_code
WHERE markets.markets_code IS NULL;
-- Answer: No mismatches found
```

### 16. List all distinct product_type values  watch for dirty data
```sql
SELECT DISTINCT product_type 
FROM sales.products;
```

### 17. Which product type ("Own Brand" vs "Distribution") generates more transactions?
```sql
SELECT products.product_type, COUNT(*) AS Transactions
FROM sales.transactions
INNER JOIN sales.products 
  ON transactions.product_code = products.product_code 
GROUP BY products.product_type;
-- Based on the output, "Own Brand" has more transactions than "Distribution"
```

##  Findings

- Product type `"Own Brand"` contained a hidden carriage return  cleaned using `REPLACE()`
- Two zone values were stored as empty strings (`''`), not NULL
- Some transactions referenced invalid `product_code`s not present in the `products` table
- "Own Brand" products generated more transactions than "Distribution"

##  Conclusion
This project used SQL to perform end-to-end data analysis on sales data  including joining tables, cleaning dirty values, checking data integrity, and deriving business insights. The results could be used for better decision-making in product and market strategy.
