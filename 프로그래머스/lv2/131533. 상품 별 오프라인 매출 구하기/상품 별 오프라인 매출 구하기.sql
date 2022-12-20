-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, sum(b.SALES_AMOUNT * a.price) as SALES
from PRODUCT a join offline_sale b on a.PRODUCT_ID=b.PRODUCT_ID
group by a.PRODUCT_CODE
order by sales desc, PRODUCT_CODE