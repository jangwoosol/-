-- 코드를 입력하세요
select b.USER_ID, b.NICKNAME, concat(city," ",STREET_ADDRESS1," ",STREET_ADDRESS2) as 전체주소, concat(substr(TLNO,1,3),'-',substr(TLNO,4,4),'-',substr(TLNO,8,4)) as 전화번호
from USED_GOODS_BOARD as a join USED_GOODS_USER as b on a.writer_id = b.user_id  
where writer_id in (SELECT writer_id
from USED_GOODS_BOARD 
group by writer_id 
having count(writer_id) >=3)
group by b.user_id 
order by b.user_id desc
