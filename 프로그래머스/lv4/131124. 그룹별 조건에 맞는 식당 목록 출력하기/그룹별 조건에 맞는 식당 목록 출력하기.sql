
select a.MEMBER_NAME,	b.REVIEW_TEXT,	date_format(b.REVIEW_DATE,'%Y-%m-%d')
from rest_review b join
(SELECT R.MEMBER_ID, M.MEMBER_NAME, RANK() OVER(ORDER BY CNT DESC) AS RANKING
from (SELECT *, COUNT(MEMBER_ID) AS CNT
FROM REST_REVIEW
GROUP BY MEMBER_ID) as r 
join MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID) as a
on a.MEMBER_ID=b.MEMBER_ID
where a.ranking=1
order by b.review_date