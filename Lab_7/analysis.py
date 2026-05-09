import pandas as pd
import matplotlib.pyplot as plt

# 1. Исследование данных
# загрузка файла
df = pd.read_csv('orders.csv')
print(df.head())

# преобразование столбца order_date в формат datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

#  проверка типов данных
print('Информация о типах данных')
df.info()

#  Количество пропущенных значений в каждом столбце
print('Пропущенные значение', df.isnull().sum())

# 2. Очистка данных
# удаляем строки, где quantity <= 0 или unit_price <= 0
df = df[(df['quantity'] > 0) & (df['unit_price'] > 0)]

# сохраняем в новой переменной только записи, где discount находится в интервале [0, 0.5]
valid_discounts_df = df[(df['discount'] >= 0) & (df['discount'] <= 0.5)].copy()

# Создаем отдельные таблицы для каждого статуса
completed_orders = df[df['status'] == 'Completed'].copy()
returned_orders = df[df['status'] == 'Returned'].copy()
canceled_orders = df[df['status'] == 'Canceled'].copy()

# Проверка результатов (вывод количества строк в каждой таблице)
print(f"Записей со статусом Completed: {len(completed_orders)}")
print(f"Записей со статусом Returned: {len(returned_orders)}")
print(f"Записей со статусом Canceled: {len(canceled_orders)}")

# 3. Добавление новых столбцов
# расчет полной стоимости без скидки (gross)
df['gross'] = df['unit_price'] * df['quantity']

# расчет стоимости с учетом скидки (net)
df['net'] = df['gross'] * (1 - df['discount'])

# создание логического флага для успешных продаж (is_valid_sale)
# значение будет True только если статус "Completed", иначе False
df['is_valid_sale'] = df['status'] == 'Completed'

# просмотр результата
print(df[['product', 'unit_price', 'quantity', 'discount', 'gross', 'net', 'is_valid_sale']].head())

# 4. Бизнес-анализ
# Общий чистый доход от корректных продаж (только Completed)
total_net_income = df[df['status'] == 'Completed']['net'].sum()
print(f"Общий чистый доход: {total_net_income:.2f}")

# Топ-5 продуктов по чистому доходу (net)
# Группируем по продукту, суммируем доход и сортируем по убыванию
top_products = df.groupby('product')['net'].sum().sort_values(ascending=False).head(5)
print("\nТоп-5 продуктов по доходу:\n", top_products)

# Анализ по категориям
category_analysis = df[df['status'] == 'Completed'].groupby('category').agg({
    'net': 'sum',
    'quantity': 'sum',
    'discount': 'mean'
})
print("\nАнализ по категориям:\n", category_analysis)

# Считаем количество завершенных и возвращенных заказов
status_counts = df.groupby(['country', 'status']).size().unstack(fill_value=0)

# Применяем формулу: Returned / (Completed + Returned)
# Используем .get(), чтобы избежать ошибок, если какого-то статуса нет в стране
status_counts['return_rate'] = status_counts.get('Returned', 0) / (status_counts.get('Completed', 0) + status_counts.get('Returned', 0))
print("\nУровень возвратов по странам:\n", status_counts['return_rate'])

# 5. Итоговый отчет
# 1. Экспорт отчета по категориям (мы создали его на прошлом шаге)
category_analysis.to_csv('report_category.csv')

# 2. Формирование и экспорт ежемесячного дохода
# Группировка по году и месяцу, суммируем net только для Completed
report_monthly = df[df['status'] == 'Completed'].resample('ME', on='order_date')['net'].sum()
report_monthly.to_csv('report_monthly.csv')

# 3. Создание сводного файла с ключевыми показателями
top_category = category_analysis['net'].idxmax()
top_return_country = status_counts['return_rate'].idxmax()

with open('summary.txt', 'w', encoding='utf-8') as f:
    f.write(f"Общий доход: {total_net_income:.2f}\n")
    f.write(f"Категория с наибольшим доходом: {top_category}\n")
    f.write(f"Страна с наибольшим уровнем возвратов: {top_return_country}\n")

# 4. Визуализация (График дохода по категориям)
category_analysis['net'].plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Чистый доход по категориям товаров')
plt.xlabel('Категория')
plt.ylabel('Доход (net)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('income_by_category.png') # Сохранение графика
plt.show()



