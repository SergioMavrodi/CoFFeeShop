 # Coffee Shop Management System

## 📋 Project Overview
A comprehensive database system for managing operations of a coffee shop in Kyrgyzstan. The system tracks customers, orders, products, staff, and payments to enable data-driven business decisions.

## 🏪 Business Description
"Кофе По-Кыргызски" is a modern coffee shop located in Bishkek, offering:
- Traditional coffee beverages ☕️
- Local teas and drinks 🍵
- Fresh desserts and pastries 🍰
- Light snacks and sandwiches 🥪

The coffee shop serves both local residents and tourists, focusing on quality service and customer experience.

## 📊 Database Structure

### Core Tables
- **Customers** - Customer information and loyalty program
- **Products** - Menu items with categories and pricing
- **Orders** - Order headers with timestamps
- **OrderItems** - Detailed order line items
- **Payments** - Payment transactions
- **Staff** - Employee management

## 🎯 Business Problems Solved

### 1. Profit Optimization
- Identify best-selling products
- Analyze revenue by category
- Optimize pricing strategy

### 2. Customer Retention
- Track customer visit frequency
- Monitor loyalty program effectiveness
- Personalize marketing campaigns

### 3. Staff Performance
- Measure order processing efficiency
- Analyze sales per employee
- Optimize staff scheduling

### 4. Menu Management
- Identify underperforming products
- Analyze product combinations
- Seasonal menu planning

## 🔗 Key Relationships

### Primary Business Flow:
 Customer → Places → Order → Contains → OrderItems → References → Products
↓ ↓ ↓
Loyalty Staff Payment
Program Servicing Processing
 
### Data Connections:
- One customer can place multiple orders
- One order can contain multiple products
- Each order is served by one staff member
- Each order has one corresponding payment

## 💾 Technical Specifications

### Database Normalization
- **1NF**: All data atomic, no repeating groups
- **2NF**: No partial dependencies
- **3NF**: No transitive dependencies

### Key Features
- Multi-language support (Russian/Kyrgyz/English)
- Local currency (KGS) handling
- Phone number formatting for Kyrgyzstan
- Loyalty program integration

## 👥 Target Users

### Internal Users:
- Baristas and cashiers
- Shift managers
- Business owners
- Marketing team

### External Beneficiaries:
- Regular customers (via loyalty program)
- Suppliers (via inventory insights)

## 📈 Expected Outcomes

### Short-term:
- 20% improvement in order tracking
- 15% better staff performance monitoring
- Reduced manual reporting time

### Long-term:
- Data-driven menu optimization
- Enhanced customer retention
- Increased operational efficiency

## 🌍 Local Context
The system is specifically designed for the Kyrgyz market with:
- Local name and surname handling
- Kyrgyz phone number formats (+996)
- Cultural preferences in product categories
- Local payment methods (cash, card, QR)

---

