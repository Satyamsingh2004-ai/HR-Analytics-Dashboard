USE hr_analytics;
-- Query 1: Total Employees

SELECT COUNT(*) AS total_employees
FROM employee;

-- Query 2: Department-wise Employee Count

SELECT
    department_id,
    COUNT(*) AS total_employees
FROM employee
GROUP BY department_id
ORDER BY total_employees DESC;

-- Query 3: Department Name using JOIN

SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees
FROM employee e
JOIN department d
ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY total_employees DESC;

DESCRIBE payroll;
-- QUERY 4 : AVERAGE SALARY BY DEPARTMENT

SELECT
    d.department_name,
    ROUND(AVG(p.net_pay), 2) AS average_salary
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
JOIN payroll p
    ON e.employee_id = p.employee_id
GROUP BY d.department_name
ORDER BY average_salary DESC;

-- QUERY 5 : HIGHEST PAID EMPLOYEE
SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    p.net_pay
FROM employee e
JOIN payroll p
    ON e.employee_id = p.employee_id
JOIN department d
    ON e.department_id = d.department_id
ORDER BY p.net_pay DESC
LIMIT 1;

-- QUERY 6 : LOWEST PAID EMPLOYEE

SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    p.net_pay
FROM employee e
JOIN payroll p
    ON e.employee_id = p.employee_id
JOIN department d
    ON e.department_id = d.department_id
ORDER BY p.net_pay ASC
LIMIT 1;

-- Query 7 : Gender Distribution
SELECT
    gender,
    COUNT(*) AS total_employees
FROM employee
GROUP BY gender;

DESCRIBE performance_review;

-- QUERY 8: AVERAGE PERFOMENCE RATING

SELECT
    ROUND(AVG(performance_rating), 2) AS average_performance_rating
FROM performance_review;

-- QUERY: 9 -- TOP 5  PERFORMER..


SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    pr.performance_rating,
    pr.productivity_score
FROM employee e
JOIN performance_review pr
    ON e.employee_id = pr.employee_id
JOIN department d
    ON e.department_id = d.department_id
WHERE pr.performance_rating = 5
ORDER BY pr.productivity_score DESC
LIMIT 5;

DESCRIBE attendance;

-- Query 11: Attendance Status Distribution
SELECT
    status,
    COUNT(*) AS total_records
FROM attendance
GROUP BY status;

SELECT
    ROUND(
        (SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) * 100.0)
        / COUNT(*),
        2
    ) AS attendance_percentage
FROM attendance;

-- QUERY --- OVERTIME ANALYSIS..
SELECT
    ROUND(AVG(overtime_hours), 2) AS average_overtime_hours
FROM attendance;


-- QUERY: LEAVE TYPE DISTRIBUTION..
SELECT
    leave_type,
    COUNT(*) AS total_leaves
FROM leave_data
GROUP BY leave_type
ORDER BY total_leaves DESC;

-- QUERY : LEAVE STATUS ANALYSIS..
SELECT
    status,
    COUNT(*) AS total_requests
FROM leave_data
GROUP BY status;

-- Query 16: Department-wise Leave Count

SELECT
    d.department_name,
    COUNT(l.leave_id) AS total_leaves
FROM leave_data l
JOIN employee e
    ON l.employee_id = e.employee_id
JOIN department d
    ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY total_leaves DESC;

-- Query 17: Top 10 Employees with Maximum Leave Days..
SELECT
    e.employee_id,
    e.employee_name,
    SUM(l.days_taken) AS total_leave_days
FROM leave_data l
JOIN employee e
    ON l.employee_id = e.employee_id
GROUP BY
    e.employee_id,
    e.employee_name
ORDER BY total_leave_days DESC
LIMIT 10;

