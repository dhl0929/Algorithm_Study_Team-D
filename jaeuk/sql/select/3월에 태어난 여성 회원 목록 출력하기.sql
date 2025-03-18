select *
from MEMBER_PROFILE
where GENDER = "W" and TLNO is not null and MONTH(DATE_OF_BIRTH) = 3
order by MEMBER_ID;