select 
    c.company_code, 
    c.founder, 
    count(DISTINCT e.lead_manager_code), 
    count(DISTINCT e.senior_manager_code), 
    count(DISTINCT e.manager_code), 
    count(DISTINCT e.employee_code)
from company c
join employee e on c.company_code = e.company_code
group by c.company_code, c.founder
order by c.company_code