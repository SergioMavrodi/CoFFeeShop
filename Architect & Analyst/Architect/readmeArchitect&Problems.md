# Project README

## Overview

For this project, I was unable to find a suitable dataset on **Kaggle.com** that met the project requirements. As a result, I decided to **create my own custom database**.

The dataset was generated in **Excel** using **synthetic data**, which was produced with the help of the **Faker library in Python**. This approach allowed me to fully control the data structure, ensure consistency, and tailor the dataset specifically to the goals of the project.

---

## Dataset Creation Process

1. Used **Python** with the **Faker** library to generate realistic fake data (e.g., names, categories, products, prices, dates, etc.).
2. Exported the generated data into an **Excel (.xlsx) file**.
3. Manually reviewed and adjusted the data to ensure logical consistency.
4. Used this Excel file as the primary source for building and populating the database.

This method ensured that the dataset is reproducible, scalable, and aligned with the project logic.

---

## Business Problems and Optimization Goals

The dataset was designed to support analysis of real-world business challenges commonly faced in the coffee shop industry. The following key problems and improvement areas were identified:

1. **Time and Day Optimization**  
   Understanding customer traffic patterns to answer the question: *At what times of day and on which days do we have the highest number of customers?*  
   This insight can be used to optimize opening hours, staffing levels, and promotional timing.

2. **Customer Retention**  
   Identifying which customers return most frequently and generate the highest total spending.  
   This helps in designing loyalty programs, personalized offers, and retention strategies.

3. **Staff Performance**  
   Analyzing which staff members complete the most orders and contribute the highest revenue.  
   This information can support performance evaluation, training decisions, and incentive programs.

4. **Menu Optimization**  
   Determining which products are rarely purchased and should either be removed from the menu or actively promoted.  
   This allows the business to reduce waste, simplify the menu, and increase overall profitability.

---


## Business Value

Analyzing the identified problems provides direct and measurable value to the coffee business by supporting data-driven decision-making:

- **Increased Revenue**  
  Understanding peak hours and high-performing products allows the business to focus promotions, pricing strategies, and upselling efforts when customer demand is highest.

- **Cost Optimization**  
  Time and day optimization helps reduce unnecessary labor costs by aligning staff schedules with real customer traffic patterns.

- **Improved Customer Loyalty**  
  Customer retention analysis enables the creation of targeted loyalty programs, discounts, and personalized offers, increasing repeat visits and lifetime customer value.

- **Higher Staff Productivity**  
  Staff performance insights support fair performance evaluation, training improvements, and incentive systems that motivate employees to increase efficiency and sales.

- **Menu Efficiency and Waste Reduction**  
  Menu optimization helps eliminate low-performing items, reduce ingredient waste, and focus on products with the highest profitability.

Overall, these insights help transform raw transaction data into actionable strategies that improve operational efficiency, customer satisfaction, and long-term profitability.

---

## Conclusion

Despite these challenges, creating a custom dataset provided full flexibility and ensured that the database accurately supports the objectives of the project. This approach also demonstrates practical skills in **data generation**, **data preparation**, and **database design**.

---


## Technologies Used

- Python
- Faker library
- Microsoft Excel
- SQL (for database creation and data insertion)

