-- 코드를 입력하세요
SELECT WRITER_ID, NICKNAME, sum(price)
from USED_GOODS_BOARD as a join USED_GOODS_USER as b on a.WRITER_ID=b.user_id
where a.STATUS ="DONE" 
group by writer_id 
having sum(price)>=700000
order by sum(price)