select 
    year(SALES_DATE) as year, 
    month(SALES_DATE) as month, 
    ui.gender, 
    count(distinct os.USER_ID) as users
from user_info ui
join online_sale os on ui.user_id = os.user_id
where gender in (0, 1)
group by year(SALES_DATE), month(SALES_DATE), ui.gender
order by year, month, gender