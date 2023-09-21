-- 코드를 입력하세요
select year(SALES_DATE) as year, month(SALES_DATE) as month ,gender,count(distinct a.user_id) as users
from (SELECT *
from user_info
where gender in (0,1)) a join online_sale on a.user_id=online_sale.user_id
group by year(SALES_DATE), month(SALES_DATE),gender
order by year,month,gender