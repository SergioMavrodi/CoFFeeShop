# AI Engineer – README

## Role Summary

In the final stage of the project, I worked in the role of **AI Engineer**, focusing on adding an **AI-driven analytical layer** on top of the existing CoffeeShop database. This role builds upon the work completed by the Database Architect, DB Analyst, and SQL Developer, using a clean, normalized, and optimized MySQL database as a reliable data source.

The main goal of this phase was to combine **SQL analytics, data visualization, and a Large Language Model (Google Gemini)** to automatically answer business questions and support decision-making for a coffee shop.

---

## Objectives

- Integrate an LLM (Google Gemini) with the MySQL database
- Enable natural-language questions over structured SQL data
- Generate analytical insights and visualizations
- Translate raw transactional data into actionable business insights

---

## Technology Stack

- **Python** (Jupyter Notebook)
- **MySQL** (CoffeeShop database)
- **Google Gemini (LLM)**
- **LangChain** (SQL Agent)
- **pandas** (data processing)
- **matplotlib / seaborn** (data visualization)
- **SQLAlchemy & PyMySQL** (database connectivity)

---

## AI Integration Overview

The AI component was implemented in **Jupyter Notebook** by connecting Google Gemini to the MySQL database through **LangChain’s SQL Agent**. This setup allows the AI model to:

- Understand natural-language business questions
- Automatically generate SQL queries
- Execute queries on the CoffeeShop database
- Return human-readable analytical answers

The Gemini model used in this project:

- `gemini-2.0-flash`
- Temperature set to `0` for deterministic and factual responses

---

## Hybrid Analysis Approach

To ensure reliability and correctness, a **hybrid approach** was used:

- **AI-driven analysis**: Gemini interprets questions and generates SQL-based answers.
- **Deterministic SQL analysis**: Predefined SQL queries are executed directly to build charts and validate AI outputs.

If the AI agent is unavailable or fails to parse a query, the system automatically falls back to direct SQL analysis. This design improves robustness and guarantees results.

---

## Business Questions Addressed

The AI-powered system was designed to answer the following key business questions:

1. **Time and Day Optimization**  
   *What time do we have the most customers?*

2. **Customer Retention**  
   *Which customers spend the most money?*

3. **Staff Performance**  
   *Which staff members generate the highest revenue?*

4. **Menu Optimization**  
   *Which products are rarely purchased?*

These questions align directly with real operational and strategic needs of a coffee shop business.

---

## Data Visualization

For each business question, custom visualizations were generated using **matplotlib** and **seaborn**:

- Line charts for order distribution by hour
- Horizontal bar charts for top customers and least popular products
- Bar charts for staff revenue comparison

The visualization logic was implemented manually to ensure:

- Clear and interpretable charts
- Correct aggregation logic
- Full control over labels, axes, and formatting

This step was necessary because LLMs alone cannot reliably generate production-quality visualizations without explicit control.

---

## Challenges and Solutions

During this phase, several challenges were addressed:

- **LLM reliability**: AI-generated SQL may be inconsistent. This was mitigated by limiting iterations and validating results with direct SQL queries.
- **Visualization accuracy**: Graphs were generated using explicit SQL queries instead of relying solely on AI output.
- **Error handling**: A fallback mechanism was implemented to continue analysis even if the AI agent fails.

These decisions ensured stability and analytical correctness.

---

## Outcome and Business Value

As a result of the AI Engineer phase:

- The database was transformed into an **AI-powered analytical system**
- Business users can ask questions in natural language
- Insights are supported by both AI explanations and visual evidence
- The solution demonstrates how AI can augment traditional SQL analytics

This final layer completes the end-to-end pipeline, turning raw transactional data into **intelligent, decision-ready insights** for a coffee shop business.

