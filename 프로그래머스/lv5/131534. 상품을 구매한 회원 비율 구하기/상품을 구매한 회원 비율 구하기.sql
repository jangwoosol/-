-- 코드를 입력하세요

# 마지막 변수를 뽑을 때 한사람이 같은 연도에 두번이상 구매할 수 있으므로 분자에서 중복을 제거해야한다. 
# 2021년에 가입한 회원 중 물건을 아예 구매하지 않은 사람도 분모에 포함되어야한다.
select date_format(b.sales_date,'%Y') year,	date_format(b.sales_date,'%m') month, count(distinct b.user_id), round((count(distinct b.user_id)/ (select count(distinct user_id) from user_info where joined like '2021%')),1)
from (SELECT * 
from USER_INFO
where joined like '2021%') a join online_sale b on a.user_id=b.user_id
group by year, month
order by year, month