# SQL Developer – README

## Role Summary

During this phase, I acted as the **SQL Developer**, responsible for translating the approved logical and relational models into a **production-ready MySQL implementation**. The scope covered physical schema creation, integrity enforcement, performance optimization via indexing, and reliable data population using a reproducible ETL workflow.

**Tools used:** MySQL Workbench, MySQL Server (InnoDB), Jupyter Notebook, Python (pandas, SQLAlchemy, PyMySQL).

---

## Objectives

- Implement the physical database schema in MySQL
- Enforce referential integrity and business rules
- Optimize read-heavy analytical queries using indexes
- Populate the database from Excel in a repeatable and auditable way

---

## Database Initialization

The database **CoffeeShop** was created in **MySQL Workbench** with full Unicode support to ensure compatibility with international text data.

Key decisions:
- `utf8mb4` character set and `utf8mb4_unicode_ci` collation
- InnoDB storage engine for transactions and foreign keys

---

## Physical Schema Implementation

All tables were created strictly according to the finalized ER diagram and validated relational model.

### Implemented Tables

- **customers** – customer identity, contact data, loyalty level
- **staff** – employee records and job positions
- **products** – product catalog with categories and pricing
- **orders** – transactional order header data
- **order_items** – junction table between orders and products
- **payments** – financial records per order

### Data Integrity Measures

The schema includes:

- **Primary keys** on all entities
- **Foreign keys** enforcing relationships between tables
- **CHECK constraints** for numeric validity (price, quantity, amount)
- **UNIQUE constraints** (e.g., phone numbers, one payment per order)
- **Default values** for timestamps and loyalty levels

These measures prevent inconsistent or invalid data from entering the system.

---

## Referential Actions

Foreign key actions were selected intentionally based on business logic:

- `ON DELETE SET NULL` for optional customer references in orders
- `ON DELETE RESTRICT` to prevent deletion of active staff or products
- `ON DELETE CASCADE` for dependent entities (order_items, payments)

This ensures data consistency while preserving historical transaction records.

---

## Indexing and Performance Optimization

An indexing strategy was designed based on **expected analytical and operational query patterns**, not arbitrarily.

### Index Design Rationale

- **Customers**: fast lookup by phone, loyalty segmentation, name search
- **Products**: category analysis, price filtering, name search
- **Orders**: time-based analysis, customer and staff joins
- **Order Items**: product-level sales aggregation
- **Payments**: payment method analysis, time-based reporting

Composite indexes (e.g., `(order_time, customer_id)`) were introduced to support frequent multi-column filters and joins.

The result is improved query performance for reporting, dashboards, and ad-hoc analysis.

---

## Data Population (ETL Process)

Data loading was implemented using a **Python-based ETL pipeline** executed in **Jupyter Notebook**.

### Source

- Excel file (`.xlsx`) containing multiple sheets:
  - Products
  - Customers
  - Staff
  - Orders
  - OrderItems
  - Payments

### Transformation Steps

- Converted textual loyalty levels into numeric values
- Standardized datetime formats for MySQL compatibility
- Ensured column alignment with database schema

### Load Strategy

- Used SQLAlchemy engine with PyMySQL driver
- Inserted data using `to_sql()` in `append` mode
- Preserved foreign key order to avoid constraint violations

This approach guarantees a **repeatable, automated, and transparent** data loading process.

---

## Validation and Testing

After population, the following checks were performed:

- Row counts per table
- Foreign key integrity validation
- Sample analytical queries (sales by time, staff revenue, product popularity)
- Index usage verification via query execution plans

---

## Outcome

As a result of the SQL Developer phase:

- A fully operational **MySQL CoffeeShop database** was delivered
- Data integrity is enforced at the database level
- Query performance is optimized for analytical workloads
- The system is ready for SQL analysis, reporting, and BI integration

This implementation completes the transition from database design to a robust, analysis-ready data platform.