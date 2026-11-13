age = int(input("Введите возраст :"))
ticket = input("Есть ли билет? (да /нет ):").lower()
if age < 16:
  print("Вход запрёщен: фильм 16 +")
elif ticket != "да":
  print ("сначала купить билет ")
else:
  print("Приятного просмотра")
  if age < 18 or >= 60 :
    print ("У вас скидка на попкорн 20%")
  
