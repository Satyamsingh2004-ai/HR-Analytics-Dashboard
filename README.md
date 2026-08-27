# 📊 HR Analytics Dashboard

# 👨‍💻 Author

**Satyam Singh**


## 📌 Project Overview

The **HR Analytics Dashboard** is an interactive data analytics project designed to help organizations understand and monitor their workforce, recruitment, attendance, performance, and payroll-related information.

The project combines **Python , SQL, and Power BI** to transform raw HR data into meaningful insights through data cleaning, analysis, and interactive dashboards.

The dashboard provides management with a clear view of employee trends and helps support **data-driven HR decision-making**.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Analyze employee demographics and workforce distribution.
* Understand employee experience and age groups.
* Analyze recruitment and hiring trends.
* Monitor employee attendance and leave patterns.
* Evaluate employee performance.
* Analyze payroll and salary-related information.
* Track important HR KPIs.
* Provide actionable insights through interactive Power BI dashboards.

---

## 🛠️ Tools & Technologies

| Tool / Technology | Purpose                                   |
| ----------------- | ----------------------------------------- |
| **Python**        | Data cleaning and processing           |
| **Pandas**        | Data manipulation and transformation      |
| **MySQL**         | Database management and SQL analysis      |
| **SQL**           | Data analysis and business queries        |
| **Power BI**      | Interactive dashboard and visualization   |
| **GitHub**        | Project documentation and version control |

---

## 📂 Dataset

The project uses multiple HR-related datasets:

* `Employee.csv`
* `Attendance.csv`
* `Department.csv`
* `Job Application.csv`
* `Leave.csv`
* `Payroll.csv`
* `Performance Review.csv`

These datasets contain information related to employees, departments, recruitment, attendance, leave, payroll, and performance.

---

# 🔄 Project Workflow

```text
Raw HR Data
     ↓
Data Cleaning using Python & Pandas
     ↓
Cleaned CSV Files
     ↓
Import Data into MySQL
     ↓
SQL Data Analysis
     ↓
Power BI Data Modeling
     ↓
Interactive HR Analytics Dashboard
     ↓
Business Insights & Recommendations
```

---

# 📊 Dashboard Modules

## 1. 👥 Employee Analytics

This section provides an overview of the organization's workforce.

### Key Analysis

* Total employee headcount
* Employee demographics
* Gender distribution
* Department-wise employee count
* Employee experience bands
* Employee age-group distribution
* Employee tenure analysis

### Experience Bands

Employees are categorized into:

* 0–2 Years
* 3–5 Years
* 6–10 Years
* 10+ Years

---

## 2. 🧑‍💼 Recruitment Analytics

This section analyzes the organization's recruitment process.

### Key Analysis

* Job application trends
* Applications over time
* Shortlisted vs. applied candidates
* Hiring funnel
* Recruitment source effectiveness
* Hiring success rate
* Source-wise recruitment performance

### Recruitment Sources

Examples include:

* Naukri
* LinkedIn
* Referral
* Other recruitment sources

---

## 3. 🕒 Attendance Analytics

This module focuses on employee attendance and leave patterns.

### Key Analysis

* Daily attendance trends
* Monthly attendance summary
* Department-wise attendance
* Leave analysis
* Absenteeism rate
* Overtime hours
* Attendance patterns

---

## 4. ⭐ Performance Analytics

This section evaluates employee performance.

### Key Analysis

* Performance rating distribution
* Department-wise average performance
* Top-performing employees
* Productivity trends
* Promotion analysis
* Average performance rating

---

## 5. 💰 Payroll Analytics

This module provides insights into employee compensation.

### Key Analysis

* Salary distribution
* Average salary
* Department-wise salary analysis
* Basic salary
* HRA
* Bonus
* Deductions
* Net pay
* Payroll trends

---

## 6. 📈 Executive Dashboard

The Executive Dashboard provides a high-level summary of important HR metrics.

### Key Performance Indicators (KPIs)

* Total Employees
* Active Employees
* Total Departments
* Attrition Rate
* Average Salary
* Employee Satisfaction Score
* Hiring Rate
* Workforce Growth

The dashboard is designed to help HR managers and business leaders quickly understand the organization's workforce status.

---

# 🗄️ SQL Analysis

SQL was used to analyze the cleaned HR data stored in the **MySQL `hr_analytics` database**.

Example analyses include:

```sql
-- Total Employees

SELECT COUNT(*) AS total_employees
FROM employee;
```

```sql
-- Department-wise Employee Count

SELECT 
    d.department_name,
    COUNT(e.employee_id) AS total_employees
FROM employee e
JOIN department d
    ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY total_employees DESC;
```

```sql
-- Average Salary by Department

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
```

SQL analysis was used to generate meaningful business insights before visualizing the results in Power BI.

---

# 🧹 Data Cleaning

Python and Pandas were used for preprocessing the raw datasets.

Major cleaning activities included:

* Removing unnecessary whitespace.
* Standardizing text values.
* Cleaning email and phone fields.
* Handling missing values.
* Imputing missing numerical values where required.
* Formatting date columns.
* Preparing datasets for SQL and Power BI.
* Validating the cleaned datasets.

Example:

```python
import pandas as pd

df = pd.read_csv("Employee.csv")

df = df.drop_duplicates()

df["department_id"] = df["department_id"].str.strip()

df.to_csv("Employee_cleaned.csv", index=False)
```

---

# 📌 Key Insights

The dashboard can be used to identify:

* Workforce distribution across departments.
* Employee demographic patterns.
* Experience levels within the organization.
* Recruitment source effectiveness.
* Attendance and absenteeism trends.
* Employee performance patterns.
* Salary differences across departments.
* Workforce growth and attrition trends.
* Areas requiring HR intervention.

These insights can help HR teams improve **employee retention, recruitment strategies, workforce planning, and organizational performance**.

---

# 📁 Project Structure

```text
HR-Analytics-Project/
│
├── Data/
│   ├── Employee.csv
│   ├── Attendance.csv
│   ├── Department.csv
│   ├── Job Application.csv
│   ├── Leave.csv
│   ├── Payroll.csv
│   └── Performance Review.csv
│
├── Python/
│   └── cleaning.py
│
├── SQL/
│   └── hr_analytics.sql
│
├── PowerBI/
│   └── HR_Analytics_Dashboard.pbix
│
├── Screenshots/
│   ├── Executive_Dashboard.png
│   ├── Employee_Analytics.png
│   ├── Recruitment_Analytics.png
│   ├── Attendance_Analytics.png
│   ├── Performance_Analytics.png
│   └── Payroll_Analytics.png
│
└── README.md
```

---

# 🚀 How to Use This Project

### Step 1 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2 — Prepare the Data

Place the HR datasets inside the `Data` folder.

### Step 3 — Run Data Cleaning

Run the Python cleaning script:

```bash
python cleaning.py
```

### Step 4 — Import Data into MySQL

Create the database:

```sql
CREATE DATABASE hr_analytics;
```

Import the cleaned datasets into MySQL.

### Step 5 — Run SQL Analysis

Execute the SQL queries available in the `SQL` folder.

### Step 6 — Open Power BI

Open:

```text
HR_Analytics_Dashboard.pbix
```

Connect the dashboard to the required data source and refresh the data.

---

# 📊 Dashboard Preview

Screenshots of the Power BI dashboard can be added to the `Screenshots` folder and displayed here.

Example:

```markdown
![Executive Dashboard](Screenshots/Executive_Dashboard.png)
```

Additional dashboard screenshots can be added for:

* Employee Analytics
* Recruitment Analytics
* Attendance Analytics
* Performance Analytics
* Payroll Analytics

---

# 💡 Business Value

This project demonstrates how HR data can be transformed into actionable insights using modern data analytics tools.

It can help organizations:

* Make data-driven HR decisions.
* Identify workforce trends.
* Improve recruitment efficiency.
* Monitor employee performance.
* Analyze compensation.
* Understand attendance patterns.
* Support workforce planning.

---

# 🔮 Future Improvements

Potential improvements include:

* Predictive employee attrition analysis.
* Employee turnover prediction using Machine Learning.
* Automated dashboard refresh.
* Advanced recruitment forecasting.
* Employee performance prediction.
* Real-time HR analytics.
* Automated HR reports.

---

### Skills Demonstrated

* Python
* Pandas
* SQL
* MySQL
* Power BI
* Data Cleaning
* Data Analysis
* Data Visualization
* Dashboard Development

---

## ⭐ Project Summary

**HR Analytics Dashboard** demonstrates an end-to-end data analytics workflow:

**Data Cleaning → SQL Analysis → Data Modeling → Power BI Visualization → Business Insights**

This project showcases practical skills in **Data Analytics, Business Intelligence, SQL, Python, and Power BI**.
