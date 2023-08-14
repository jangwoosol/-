-- 코드를 입력하세요
SELECT category, price as max_price, PRODUCT_NAME
from food_product
where price in (select max(price) from food_product group by category) and category in ("과자", "국", "김치", "식용유")
order by price desc