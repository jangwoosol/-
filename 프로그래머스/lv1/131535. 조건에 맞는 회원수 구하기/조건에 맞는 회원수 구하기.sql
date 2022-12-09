-- 코드를 입력하세요
SELECT count(user_id) as USERS
from USER_INFO
where (age>=20 and age<= 29) and JOINED like '2021%'