-- 코드를 입력하세요
SELECT a.PRODUCT_ID,a.PRODUCT_NAME, sum(a.price*b.amount) as total_sales
from FOOD_PRODUCT as a join (select PRODUCT_ID, PRODUCE_DATE, amount
                             from FOOD_ORDER where PRODUCE_DATE like '2022-05%') as b
                             on a.PRODUCT_ID=b.PRODUCT_ID 
group by a.product_id 
order by total_sales desc, product_id
