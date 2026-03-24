# Write your MySQL query statement below
/* Write your PL/SQL query statement below */
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e, Department d
where e.departmentId = d.id
and (e.departmentId, e.salary) in (select departmentId, max(salary) from Employee group by departmentId)