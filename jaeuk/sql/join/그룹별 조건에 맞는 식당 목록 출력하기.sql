select mp.member_name, rr.review_text, date_format(rr.review_date, '%Y-%m-%d') as review_date
from member_profile mp
join rest_review rr on mp.member_id = rr.member_id
where mp.member_id = (
    select member_id
    from rest_review
    group by member_id
    order by count(review_score) desc
    limit 1    
    )
order by review_date, review_text