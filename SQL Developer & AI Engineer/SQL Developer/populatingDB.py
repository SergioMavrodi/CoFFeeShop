# Установка библиотек (выполняется в Jupyter Notebook или Colab)
!pip install pandas openpyxl pymysql sqlalchemy --quiet

# Подключаем необходимые библиотеки
import pandas as pd
from sqlalchemy import create_engine

# Путь к Excel-файлу и параметры подключения к MySQL
excel_file = "C:/Users/sergio/Downloads/coffee_shop.xlsx"

# Создаём подключение к базе данных CoffeeShop
# Формат: mysql+pymysql://<user>:<password>@<host>/<database>
engine = create_engine("mysql+pymysql://root:root123@localhost/CoffeeShop")

# Читаем все листы из Excel-файла
products = pd.read_excel(excel_file, sheet_name="Products")
customers = pd.read_excel(excel_file, sheet_name="Customers")
staff = pd.read_excel(excel_file, sheet_name="Staff")
orders = pd.read_excel(excel_file, sheet_name="Orders")
order_items = pd.read_excel(excel_file, sheet_name="OrderItems")
payments = pd.read_excel(excel_file, sheet_name="Payments")

# Преобразуем уровень лояльности в числовые значения
customers["loyalty_level"] = (
    customers["loyalty_level"]
    .replace({"regular": 0, "bronze": 1, "silver": 2, "gold": 3})
    .fillna(0)
    .astype(int)
)

# Преобразуем время заказа в строковый формат, подходящий для MySQL DATETIME
orders["order_time"] = pd.to_datetime(orders["order_time"])
orders["order_time"] = orders["order_time"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Загружаем данные в соответствующие таблицы
# if_exists="append" — добавляем данные (предполагаем, что таблицы уже созданы)
products.to_sql("products", con=engine, if_exists="append", index=False)
customers.to_sql("customers", con=engine, if_exists="append", index=False)
staff.to_sql("staff", con=engine, if_exists="append", index=False)
orders.to_sql("orders", con=engine, if_exists="append", index=False)
order_items.to_sql("order_items", con=engine, if_exists="append", index=False)
payments.to_sql("payments", con=engine, if_exists="append", index=False)

print("Все данные успешно загружены в базу данных CoffeeShop! ☕")
