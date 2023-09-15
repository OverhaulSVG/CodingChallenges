select 
    C.company_code,
    C.founder,
    count(distinct(L.lead_manager_code)),
    count(distinct(S.senior_manager_code)),
    count(distinct(M.manager_code)),
    count(distinct(E.employee_code))
from employee E
inner join manager M
    on E.manager_code = M.manager_code
inner join senior_manager S
    on E.senior_manager_code = S.senior_manager_code
inner join lead_manager L
    on E.lead_manager_code = L.lead_manager_code
inner join company C
    on L.company_code = C.company_code
group by
    C.company_code, C.founder
order by C.company_code asc
