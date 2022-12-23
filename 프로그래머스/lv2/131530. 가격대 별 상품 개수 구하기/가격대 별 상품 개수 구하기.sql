-- 코드를 입력하세요
SELECT truncate(price,-4) price_group, count(product_id)
from PRODUCT
group by price_group
order by price_group