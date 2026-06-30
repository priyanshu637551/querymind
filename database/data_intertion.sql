INSERT INTO customers
SELECT DISTINCT
    customer_id,
    first_name,
    last_name,
    gender,
    age_group,
    TO_DATE(signup_date,'YYYY-MM-DD'),
    country
FROM ecom;


select * from customers;




SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT order_id) AS unique_orders
FROM ecom;


INSERT INTO products
SELECT DISTINCT
    product_id,
    product_name,
    category,
    unit_price
FROM ecom;

select * from products;


INSERT INTO orders
SELECT DISTINCT
    order_id,
    customer_id,
    product_id,
    quantity,
    order_date::DATE,
    order_status,
    payment_method
FROM ecom;


select * from orders;


INSERT INTO reviews
SELECT DISTINCT
    review_id,
    customer_id,
    product_id,
    rating,
    review_text,
    review_date::DATE
FROM ecom;

select * from reviews;
