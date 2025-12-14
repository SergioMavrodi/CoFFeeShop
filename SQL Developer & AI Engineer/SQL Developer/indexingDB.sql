-- Индексы для оптимизации запросов в базе данных CoffeeShop

-- Клиенты
CREATE INDEX idx_customers_phone ON customers(phone);
CREATE INDEX idx_customers_loyalty ON customers(loyalty_level);
CREATE INDEX idx_customers_name ON customers(last_name, first_name);  -- Для поиска по фамилии и имени

-- Сотрудники
CREATE INDEX idx_staff_position ON staff(position);

-- Продукты
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_products_name ON products(name);

-- Заказы
CREATE INDEX idx_orders_time ON orders(order_time DESC);               -- Для сортировки по времени (новые сначала)
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_staff ON orders(staff_id);
CREATE INDEX idx_orders_time_customer ON orders(order_time, customer_id);  -- Составной для отчётов по клиентам во времени
CREATE INDEX idx_orders_time_id ON orders(order_time, order_id);       -- Полезен для пагинации по времени

-- Позиции заказа
CREATE INDEX idx_orderitems_product ON order_items(product_id);
CREATE INDEX idx_orderitems_order ON order_items(order_id);             -- Уже частично покрывается FK, но полезен для JOIN
CREATE INDEX idx_oi_product_order ON order_items(product_id, order_id); -- Для запросов популярности продуктов в заказах

-- Платежи
CREATE INDEX idx_payments_method ON payments(payment_method);
CREATE INDEX idx_payments_time ON payments(payment_time);
CREATE INDEX idx_payments_amount ON payments(amount);
