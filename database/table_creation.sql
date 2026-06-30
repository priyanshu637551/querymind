-- 1. Remove the old empty table structure
DROP TABLE IF EXISTS ecom;

-- 2. Create the new structured table
CREATE TABLE ecom (
    customer_id VARCHAR(50),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(20),
    age_group VARCHAR(50),
    signup_date VARCHAR(50),      -- Kept as text to safely accept DD/MM/YYYY formatting
    country VARCHAR(100),
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(100),
    quantity INT,
    unit_price NUMERIC(10, 2),
    order_id VARCHAR(50),
    order_date VARCHAR(50),       -- Kept as text to safely accept DD/MM/YYYY formatting
    order_status VARCHAR(50),
    payment_method VARCHAR(50),
    rating INT,
    review_text TEXT,
    review_id VARCHAR(50),
    review_date VARCHAR(50)       -- Kept as text to safely accept DD/MM/YYYY formatting
);



select * from ecom
limit 5;


CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(20),
    age_group VARCHAR(20),
    signup_date DATE,
    country VARCHAR(50)
);

CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    unit_price NUMERIC(10,2)
);


CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    quantity INTEGER,
    order_date DATE,
    order_status VARCHAR(30),
    payment_method VARCHAR(50),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


CREATE TABLE reviews (
    review_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    rating INTEGER,
    review_text VARCHAR(255),
    review_date DATE,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);



DROP TABLE IF EXISTS customers;