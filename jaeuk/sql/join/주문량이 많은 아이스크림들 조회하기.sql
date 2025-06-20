with tmp as 
        (select flavor, sum(total_order) as total_order
        from july j
        group by flavor)

select fh.flavor
from first_half fh
join tmp t on t.flavor = fh.flavor
order by fh.total_order + t.total_order desc
limit 3