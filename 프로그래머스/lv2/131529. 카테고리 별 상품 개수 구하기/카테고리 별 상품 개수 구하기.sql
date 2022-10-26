-- 코드를 입력하세요
SELECT substring(PRODUCT_CODE,1,2), count(product_id)
from product
group by substring(PRODUCT_CODE,1,2)

