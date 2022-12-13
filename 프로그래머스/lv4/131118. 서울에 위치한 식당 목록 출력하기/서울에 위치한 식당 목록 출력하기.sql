-- 코드를 입력하세요
SELECT a.REST_ID,	a.REST_NAME,	a.FOOD_TYPE,a.FAVORITES,	a.ADDRESS,round(avg(review_score),2)
from rest_info a inner join rest_review b on a.rest_id=b.rest_id
where a.address like '서울%'
group by rest_name
order by round(sum(review_score)/count(review_score),2) desc, favorites desc