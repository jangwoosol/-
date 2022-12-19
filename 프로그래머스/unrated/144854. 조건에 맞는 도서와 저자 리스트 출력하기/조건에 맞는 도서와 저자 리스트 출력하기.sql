-- 코드를 입력하세요
SELECT BOOK_ID,	AUTHOR_NAME,	date_format(PUBLISHED_DATE,'%Y-%m-%d')
from book a join author b on a.AUTHOR_ID=b.AUTHOR_ID
where a.category ='경제'
order by PUBLISHED_DATE