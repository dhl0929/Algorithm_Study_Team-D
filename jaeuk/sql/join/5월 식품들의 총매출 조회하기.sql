select fp.PRODUCT_ID, fp.PRODUCT_NAME, sum(amount * price) as TOTAL_SALES
from food_product fp
join food_order fo on fp.product_id = fo.product_id
where fo.produce_date >= '2022-05-01' and fo.produce_date <= '2022-05-31'
group by fp.product_id
order by TOTAL_SALES DESC, PRODUCT_ID
