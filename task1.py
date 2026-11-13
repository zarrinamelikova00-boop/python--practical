order_sum = float(input("Сумма заказа"))
people = int(input("Количество человек"))

if order_sum < 0 or people <= 0 :
    print("Введите правильные данные")
else:
    total = round(order_sum * 1.10, 2)
    each = round(total / people, 2)
    print("Итоги с обслуживанием :" , total)
    print("С каждого:" , each)
  
