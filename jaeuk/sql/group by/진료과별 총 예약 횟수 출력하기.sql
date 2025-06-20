select mcdp_cd as '진료과코드', count(apnt_no) as '5월예약건수'
from appointment
where APNT_YMD >= '2022-05-01' and APNT_YMD <= '2022-05-31'
group by mcdp_cd
order by count(apnt_no), mcdp_cd