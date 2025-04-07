select 
    rr.REST_ID, 
    ri.REST_NAME, 
    ri.FOOD_TYPE, 
    ri.FAVORITES, 
    ri.ADDRESS, 
    round(avg(rr.review_score), 2) as SCORE
from rest_info ri
join rest_review rr on ri.rest_id = rr.rest_id
where ri.address like "서울%"
group by ri.rest_id
order by score desc, ri.favorites desc