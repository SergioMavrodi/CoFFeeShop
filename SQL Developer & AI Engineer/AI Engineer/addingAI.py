import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine, text
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI

warnings.filterwarnings('ignore')

# Настройки
DB_URI = 'mysql+pymysql://root:root123@localhost/CoffeeShop'
GEMINI_API_KEY = "AIzaSyABEjIWJSKCLvZbE6ltBcusmezfX7_yYb0"

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("="*80)
print("     AI АНАЛИТИК COFFEESHOP")
print("="*80)

# Подключение к базе
try:
    db = SQLDatabase.from_uri(DB_URI)
    engine = create_engine(DB_URI)
    print(f"✅ База подключена: {DB_URI.split('/')[-1]}")
except Exception as e:
    print(f"❌ Ошибка: {e}")
    exit()

# Инициализация Gemini
use_ai = False
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        google_api_key=GEMINI_API_KEY
    )
    
    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="zero-shot-react-description",
        verbose=True,
        max_iterations=3,
        handle_parsing_errors=True
    )
    print("✅ AI агент готов")
    use_ai = True
except Exception as e:
    print(f"⚠️ AI недоступен: {e}")
    print("💡 Работаю через прямой SQL-анализ")

print("="*80 + "\n")

# Функция визуализации
def visualize(question):
    q = question.lower()
    
    try:
        if 'time' in q or 'час' in q:
            df = pd.read_sql(text("""
                SELECT HOUR(order_time) as Час, COUNT(*) as Заказов
                FROM orders GROUP BY Час ORDER BY Час
            """), engine)
            
            plt.plot(df['Час'], df['Заказов'], marker='o', linewidth=2, color='blue')
            plt.title('📊 Заказы по часам', fontsize=14, fontweight='bold')
            plt.xlabel('Час')
            plt.ylabel('Заказов')
            plt.grid(alpha=0.3)
            plt.tight_layout()
            plt.show()
            print("\n📈 Данные:")
            print(df.to_string(index=False))
            
        elif 'customer' in q or 'клиент' in q:
            df = pd.read_sql(text("""
                SELECT CONCAT(c.first_name, ' ', c.last_name) as Клиент,
                       ROUND(SUM(p.amount), 2) as Траты
                FROM customers c 
                JOIN orders o ON c.customer_id = o.customer_id
                JOIN payments p ON o.order_id = p.order_id
                GROUP BY c.customer_id 
                ORDER BY Траты DESC LIMIT 10
            """), engine)
            
            plt.barh(df['Клиент'], df['Траты'], color='gold')
            plt.title('💰 Топ клиентов', fontsize=14, fontweight='bold')
            plt.xlabel('Траты (сом)')
            plt.gca().invert_yaxis()
            plt.tight_layout()
            plt.show()
            print("\n📈 Данные:")
            print(df.to_string(index=False))
            
        elif 'staff' in q or 'сотрудник' in q:
            df = pd.read_sql(text("""
                SELECT CONCAT(s.first_name, ' ', s.last_name) as Сотрудник,
                       ROUND(SUM(p.amount), 2) as Выручка
                FROM staff s 
                JOIN orders o ON s.staff_id = o.staff_id
                JOIN payments p ON o.order_id = p.order_id
                GROUP BY s.staff_id 
                ORDER BY Выручка DESC
            """), engine)
            
            plt.bar(df['Сотрудник'], df['Выручка'], color='purple')
            plt.title('👨‍💼 Выручка сотрудников', fontsize=14, fontweight='bold')
            plt.ylabel('Выручка (сом)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            print("\n📈 Данные:")
            print(df.to_string(index=False))
            
        elif 'product' in q or 'товар' in q:
            df = pd.read_sql(text("""
                SELECT p.name as Товар, 
                       COALESCE(SUM(oi.quantity), 0) as Продано
                FROM products p
                LEFT JOIN order_items oi ON p.product_id = oi.product_id
                GROUP BY p.product_id 
                ORDER BY Продано ASC LIMIT 10
            """), engine)
            
            plt.barh(df['Товар'], df['Продано'], color='red')
            plt.title('📉 Непопулярные товары', fontsize=14, fontweight='bold')
            plt.xlabel('Продано')
            plt.gca().invert_yaxis()
            plt.tight_layout()
            plt.show()
            print("\n📈 Данные:")
            print(df.to_string(index=False))
            
    except Exception as e:
        print(f"⚠️ Ошибка графика: {e}")

# Вопросы
questions = [
    "What time do we have the most customers?",
    "Which customers spend the most money?",
    "Which staff members have the highest revenue?",
    "Which products are rarely purchased?"
]

print("🤖 Запуск анализа...\n")

for i, question in enumerate(questions, 1):
    print(f"\n{'='*80}")
    print(f"📝 ВОПРОС {i}: {question}")
    print(f"{'='*80}\n")
    
    if use_ai:
        try:
            response = agent.invoke({"input": question})
            print(f"\n✨ ОТВЕТ AI:")
            print(f"{'─'*80}")
            print(response['output'])
            print(f"{'─'*80}\n")
        except Exception as e:
            print(f"⚠️ Ошибка AI: {e}")
            print("💡 Показываю график\n")
    
    # Всегда показываем график
    visualize(question)
    print()

print("\n" + "="*80)
print("✅ Анализ завершен!")
print("="*80)
