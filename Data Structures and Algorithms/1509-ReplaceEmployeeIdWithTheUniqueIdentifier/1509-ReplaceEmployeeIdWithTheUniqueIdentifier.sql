-- Last updated: 6/7/2026, 11:25:43 PM
# Write your MySQL query statement below
SELECT unique_id , name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;