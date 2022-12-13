-- 코드를 입력하세요
# 어떤 변수에 특정 값 할당할 때 set사용, 7시부터 있기 때문에 0~6시간 지정해줘야 한다.
set @hour =-1;
SELECT (@hour := @hour +1) as hour, (select count(hour(datetime)) from animal_outs 
                                     where hour(datetime) = @hour ) as COUNT
from animal_outs
where @hour <23
