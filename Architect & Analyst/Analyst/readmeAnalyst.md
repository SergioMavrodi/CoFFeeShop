# DB Analyst – README

## Role Overview

In this stage of the project, I worked in the role of **Database Analyst (DB Analyst)**. After reviewing the database architecture created by the **Database Architect**, I focused on validating the relational model, defining table relationships, and ensuring that the database structure supports analytical and business requirements.

The work was based on the finalized **ER diagram**, which represents a coffee shop transactional system.

---

## ER Diagram Description

The ER diagram consists of the following core entities:

- **customers** – stores customer personal data and loyalty level
- **orders** – represents customer orders and links customers with staff
- **order_items** – resolves the many-to-many relationship between orders and products
- **products** – contains product details and pricing
- **staff** – stores employee information
- **payments** – records payment information for each order

This structure follows a normalized relational model suitable for transactional and analytical workloads.

---

## Defined Relationships

Based on the ER diagram, the following relationships were created and validated:

1. **Customers → Orders (One-to-Many)**  
   One customer can place multiple orders, but each order belongs to exactly one customer.

2. **Staff → Orders (One-to-Many)**  
   One staff member can handle many orders, while each order is processed by one staff member.

3. **Orders → Order_Items (One-to-Many)**  
   Each order can contain multiple order items.

4. **Products → Order_Items (One-to-Many)**  
   Each product can appear in multiple order items.

5. **Orders → Payments (One-to-One / One-to-Many)**  
   Each order is linked to its payment record(s), allowing flexibility for different payment scenarios.

Foreign keys were defined to enforce referential integrity between all related tables.

---

## Relational Model Validation

Throughout the project delivery, the relational model was continuously reviewed to ensure:

- Correct use of **primary keys** and **foreign keys**
- Logical consistency between entities
- Elimination of redundant data
- Support for common analytical queries (sales, customers, staff, products)

The model follows normalization principles (up to **3NF**), reducing data anomalies and improving maintainability.

---

## Analytical Readiness

The validated schema enables efficient analysis of key business questions, including:

- Sales performance by time and day
- Customer retention and loyalty behavior
- Staff productivity and revenue contribution
- Product popularity and menu optimization

This confirms that the database structure is well-suited for further SQL analysis and business intelligence tasks.

---

## Conclusion

By validating the ER diagram and enforcing proper relationships between tables, the DB Analyst role ensured that the database is reliable, scalable, and analytically sound. This step bridges the gap between database design and practical data analysis for real-world business use cases.
