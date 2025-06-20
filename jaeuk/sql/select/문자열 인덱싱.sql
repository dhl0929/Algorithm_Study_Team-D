select city
from station
where lower(substr(city,1,1)) in ('a', 'e', 'i', 'o', 'u')

-- city: 대상 문자열
-- 1: 시작 위치
-- 1: 추출한 문자 개수