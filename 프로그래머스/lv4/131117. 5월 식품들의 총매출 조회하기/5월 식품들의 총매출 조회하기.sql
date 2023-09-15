-- 코드를 입력하세요
SELECT food_product.product_id,food_product.PRODUCT_NAME,sum(food_product.price*a.amount) as TOTAL_SALES
from (select *
from food_order 
where produce_date like "2022-05%") as a join food_product on a.product_id=food_product.product_id
group by product_id
order by  TOTAL_SALES desc, product_id 
