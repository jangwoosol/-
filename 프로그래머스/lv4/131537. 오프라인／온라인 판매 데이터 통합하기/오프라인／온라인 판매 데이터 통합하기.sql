-- 코드를 입력하세요
select date_format(sales_date,'%Y-%m-%d')as sales_date,PRODUCT_ID,	USER_ID,	SALES_AMOUNT
from online_sale
where SALES_DATE like "2022-03%"
union all
select date_format(sales_date,'%Y-%m-%d')as sales_date,PRODUCT_ID,	NULL,	SALES_AMOUNT
from offline_sale
where SALES_DATE like "2022-03%"

order by sales_date, product_id, user_id
