#Инициализируем список покупок
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    """В функции рассчитывается и 
    возвращается общая выручка (цена * количество для всех записей)"""
    result = sum([element['price']* element['quantity'] for element in purchases])
    return result 



def items_by_category(purchases):
    """В функции возвращается словарь, где ключ — категория, 
    а значение — список уникальных товаров в этой категории."""
    unique_elements = {}
    for element in purchases:
        unique_elements[element['category']] = unique_elements.get(element['category'],[]) + [element['item']]
    return unique_elements


def expensive_purchases(purchases, min_price):
    """В функции выводятся все покупки, 
    где цена товара больше или равна min_price."""
    purchases = list(filter(lambda x:x['price'] >= min_price,purchases))
    return purchases


def average_price_by_category(purchases):
    """В функции рассчитается средняя цена товаров по каждой категории."""
    average_price = {}
    for element in purchases:
        average_price[element['category']] = average_price.get(element['category'],[]) + [element['price']]
    
    average_price = {key:sum(value) / len(value) for key,value in average_price.items()}
    return average_price


def most_frequent_category(purchases):
    """В функции возвращается категория, в которой куплено больше всего единиц товаров 
    (учитывается поле quantity)."""
    most_common_category = {}
    for element in purchases:
        most_common_category[element['category']] = most_common_category.get(element['category'],[]) + [element['quantity']]
    most_common_category = {key:sum(value) for key,value in most_common_category.items()}
    #инициализируем переменную максимума
    maximum = -1
    #инициализируется категория соответствующая максимальному количеству 
    category = None
    for key in most_common_category:
        if maximum < most_common_category[key]:
            maximum = most_common_category[key]
            category = key
    return category
               
print(f'Общая выручка: {total_revenue(purchases)}') 
print(f'Товары по категориям:{items_by_category(purchases)}') 
print(f'Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')
    
        