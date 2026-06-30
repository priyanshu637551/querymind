SELECT COUNT(*) FROM customers;

SELECT COUNT(*) FROM products;

SELECT COUNT(*) FROM orders;

SELECT COUNT(*) FROM reviews;

CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_orders_product
ON orders(product_id);

CREATE INDEX idx_orders_date
ON orders(order_date);

CREATE INDEX idx_reviews_product
ON reviews(product_id);

CREATE INDEX idx_products_category
ON products(category);


SELECT
    p.category,
    SUM(o.quantity * p.unit_price) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;