select 
    USER_ID, 
    NICKNAME, 
    concat(city, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소', 
    concat(substr(TLNO, 1, 3), '-', substr(TLNO, 4, 4), '-', substr(TLNO,8, 4)) as '전화번호'
from USED_GOODS_USER
where user_id in (select writer_id
                from USED_GOODS_BOARD
                group by writer_id
                having count(contents) >= 3)
order by USER_ID desc