-- 코드를 입력하세요
SELECT MEMBER_ID,	MEMBER_NAME,	GENDER,	date_format(DATE_OF_BIRTH,'%Y-%m-%d')
from MEMBER_PROFILE
where DATE_OF_BIRTH like '%03%' and tlno is not null and GENDER='W'
order by member_id