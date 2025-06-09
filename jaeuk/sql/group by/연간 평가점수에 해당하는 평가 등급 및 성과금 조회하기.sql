with grade as (select 
                emp_no,
                case
                    when avg(score) >= 96 then 'S'
                    when avg(score) >= 90 then 'A'
                    when avg(score) >= 80 then 'B'
                    else 'C'
                end as grade   
            from HR_GRADE
            group by emp_no)

select 
    he.emp_no,
    he.emp_name,
    g.grade,
    case
        when grade = 'S' then he.sal * 0.2
        when grade = 'A' then he.sal * 0.15
        when grade = 'B' then he.sal * 0.1
        else he.sal * 0
    end as bonus
from HR_EMPLOYEES he
join grade g on he.emp_no = g.emp_no
order by he.emp_no