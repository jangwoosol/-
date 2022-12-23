-- 코드를 입력하세요
select a.category, sum(sales)
from book a join (select *
from book_sales
where sales_date like '2022-01%') b on a.book_id=b.book_id
group by a.category
order by a.category


