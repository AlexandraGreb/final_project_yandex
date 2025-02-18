# Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

## Вариант решения задания №1
```sql
SELECT c.login, COUNT(o."courierId") AS order_count
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true AND o.cancelled = false AND o.finished = false
GROUP BY c.login;
```
## Вариант решения задания №2
```sql
  SELECT c.login, COUNT(o.id) AS "deliveryCount" 
  FROM "Couriers" AS c 
  LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
  WHERE o."inDelivery" = true 
  GROUP BY c.login;
```

# Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
- Если поле finished == true, то вывести статус 2.
- Если поле canсelled == true, то вывести статус -1.
- Если поле inDelivery == true, то вывести статус 1.
- Для остальных случаев вывести 0.

## Вариант решения задания №1
```sql
SELECT o.track,
       CASE
           WHEN o.finished = true THEN 2
           WHEN o.cancelled = true THEN -1
           WHEN o."inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders" o;
```
## Вариант решения задания №2
```sql
   SELECT track, 
      CASE 
    WHEN finished = true THEN 2 
    WHEN cancelled = true THEN -1 
    WHEN "inDelivery" = true THEN 1 
    ELSE 0 END AS status 
   FROM "Orders";
   ```