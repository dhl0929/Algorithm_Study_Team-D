select ceil(avg(salary) - avg(replace(salary, 0, '')))
from employees

-- ceil : 올림, 4.2 -> 5, 4.7 -> 5
-- replace
-- salary : 대상 문자
-- 0 : 어떤 걸
-- '' : 무엇으로