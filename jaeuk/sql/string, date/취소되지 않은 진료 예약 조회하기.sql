select a.apnt_no, p.pt_name, p.pt_no, d.mcdp_cd, d.dr_name, a.apnt_ymd
from appointment a
left join patient p on a.pt_no = p.pt_no
left join doctor d on a.mddr_id = d.dr_id
where date_format(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13' and a.apnt_cncl_yn = 'N' and d.mcdp_cd = 'cs'
order by a.APNT_YMD