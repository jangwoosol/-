-- 코드를 입력하세요
SELECT MEMBER_ID,	MEMBER_NAME,	GENDER, date_format(date_of_birth,'%Y-%m-%d') 	
from member_profile
where TLNO is not null and month(date_of_birth)=3 and Gender ="W"
order by member_id