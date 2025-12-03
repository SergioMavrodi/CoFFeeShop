-- Создание базы данных CoffeeShop
CREATE DATABASE IF NOT EXISTS CoffeeShop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE CoffeeShop;

-- Таблица клиентов
CREATE TABLE customers (
    customer_id   INT AUTO_INCREMENT PRIMARY KEY,
    first_name    VARCHAR(50) NOT NULL,
    last_name     VARCHAR(50) NOT NULL,
    phone         VARCHAR(20) UNIQUE,
    loyalty_level INT DEFAULT 0
) ENGINE=InnoDB;

-- Таблица сотрудников
CREATE TABLE staff (
    staff_id   INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50) NOT NULL,
    position   VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Таблица продуктов
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    category   VARCHAR(50)  NOT NULL,
    price      DECIMAL(6,2) NOT NULL CHECK (price >= 0)
) ENGINE=InnoDB;

-- Таблица заказов
CREATE TABLE orders (
    order_id    INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NULL,
    staff_id    INT NOT NULL,
    order_time  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) 
        REFERENCES customers(customer_id) ON DELETE SET NULL,
    CONSTRAINT fk_orders_staff FOREIGN KEY (staff_id) 
        REFERENCES staff(staff_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Таблица позиций заказа
CREATE TABLE order_items (
    item_id     INT AUTO_INCREMENT PRIMARY KEY,
    order_id    INT NOT NULL,
    product_id  INT NOT NULL,
    quantity    INT NOT NULL CHECK (quantity > 0),
    
    CONSTRAINT fk_orderitems_order FOREIGN KEY (order_id) 
        REFERENCES orders(order_id) ON DELETE CASCADE,
    CONSTRAINT fk_orderitems_product FOREIGN KEY (product_id) 
        REFERENCES products(product_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Таблица платежей
CREATE TABLE payments (
    payment_id      INT AUTO_INCREMENT PRIMARY KEY,
    order_id        INT NOT NULL,
    amount          DECIMAL(8,2) NOT NULL CHECK (amount >= 0),
    payment_method  VARCHAR(20) NOT NULL,
    payment_time    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_payments_order FOREIGN KEY (order_id) 
        REFERENCES orders(order_id) ON DELETE CASCADE,
    UNIQUE KEY uq_one_payment_per_order (order_id)
) ENGINE=InnoDB;

-- Индексы для оптимизации запросов
CREATE INDEX idx_customers_phone ON customers(phone);
CREATE INDEX idx_customers_loyalty ON customers(loyalty_level);
CREATE INDEX idx_customers_name ON customers(last_name, first_name);

CREATE INDEX idx_staff_position ON staff(position);

CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_products_name ON products(name);

CREATE INDEX idx_orders_time ON orders(order_time DESC);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_staff ON orders(staff_id);
CREATE INDEX idx_orders_time_customer ON orders(order_time, customer_id);

CREATE INDEX idx_orderitems_product ON order_items(product_id);
CREATE INDEX idx_orderitems_order ON order_items(order_id);

CREATE INDEX idx_payments_method ON payments(payment_method);
CREATE INDEX idx_payments_time ON payments(payment_time);
CREATE INDEX idx_payments_amount ON payments(amount);

CREATE INDEX idx_oi_product_order ON order_items(product_id, order_id);
CREATE INDEX idx_orders_time_id ON orders(order_time, order_id);
