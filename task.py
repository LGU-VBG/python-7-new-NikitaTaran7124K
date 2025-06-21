def merge_lists_to_dict(keys,values):
    return dict(zip(keys,values))
values = [1,2,3,4]
keys = [5,6,7,8]
result = merge_lists_to_dict(keys=keys,values=values)
result2 = merge_lists_to_dict(keys,values=values)
print(result)
print(result2)

def update_car_info(brand, model, year, color, price):
    car = {}
    car['brand'] = brand
    car['model'] = model
    car['year'] = year
    car['color'] = color
    car['price'] = price  
    car['is_available'] = True
    return car
car_info = update_car_info(brand='Toyota', model='Camry', year=2021, color='blue', price=300000)
print(car_info)
