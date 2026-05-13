# Student Success & Early Intervention Analytics System 🎓🚀

An end-to-end data engineering and predictive analytics ecosystem designed to transition higher education from reactive reporting to proactive student support. To consolidate scattered student performance records into a unified Data Warehouse in SQL Server. Engineer an Interactive Power BI dashboards that visualize academic trends, identifying student performance and implement predictive analytics.

---

## 📌 Business Problem
Most universities rely on **Reactive Analytics**—they identify academic struggles only *after* a student has failed a semester. This "post-mortem" approach makes it impossible to provide timely support.

**The Challenges:**
* **Delayed Insights:** Failure is identified too late for intervention.
* **Data Fragmentation:** Attendance, internal marks, and demographics are siloed.
* **Predictive Gap:** No mechanism exists to forecast a student’s final graduation honors based on early performance.

## 💡 The Solution: Proactive Intervention
This project implements an **Early Warning System (EWS)** and **Predictive Modeling** to identify at-risk students in real-time.

**Key Innovations:**
* **Early Warning System:** Automatically flags students with <75% attendance or low internal marks mid-semester.
* **Predictive Analytics:** Uses a **Linear Regression** model to forecast Final Graduation CGPA ($R^2 = 0.76$).
* **Medallion Architecture:** A professional SQL-based data pipeline (Bronze -> Silver -> Gold).
* **Persona-Driven BI:** Tailored dashboards for the **Principal**, **HOD**, and **Faculty Mentor**.

---

## 🏗️ Architecture & Methodology
The project follows an industry-standard Data Engineering lifecycle:

1. **Ingestion (Bronze):** Raw CSV/Excel files (generated via Python Faker) land in SQL Server.
2. **Cleansing (Silver):** Data validation, type casting, and anomaly detection via T-SQL.
3. **Analytical Modeling (Gold):** A Star Schema optimized for BI, featuring the `Is_At_Risk_Flag` logic.
4. **Machine Learning:** A Python script connects to the Gold Layer, trains on historical graduate data, and predicts outcomes for active students.
5. **Visualization:** Interactive Power BI reports with **Drill-Through** capabilities and **Row-Level Security (RLS)**.

##📊 Dashboard Previews

![ Principal View](https://github.com/muhammed-fazal/Student-Success-And-Early-Intervention-Analytics-System/blob/main/Power%20BI%20Dashboard/images/Principal%20View.png)


![ HOD View](https://github.com/muhammed-fazal/Student-Success-And-Early-Intervention-Analytics-System/blob/main/Power%20BI%20Dashboard/images/HOD%20View.png)


![ Mentors View](https://github.com/muhammed-fazal/Student-Success-And-Early-Intervention-Analytics-System/blob/main/Power%20BI%20Dashboard/images/Mentors%20View.png)
---
## Key Results
### Executive view: 
#### 1.Identify the Low performing department and follow structured approach or strategies
#### Some common strategies:
##### 🔍 Diagnosis
Performance audit: Review academic results, research output, student feedback, and faculty performance.

Root cause analysis: Identify whether issues stem from poor teaching quality, lack of resources, weak leadership, or low student engagement.

##### 📈 Improvement Measures
Faculty development: Training, mentoring, and workshops to improve teaching methods and research skills.

Curriculum revision: Updating outdated syllabi to align with industry needs and modern pedagogy.

Student support: Tutoring, counseling, and skill-building programs to help struggling students.

Resource allocation: Providing better labs, libraries, and technology to enhance learning.

##### ⚖️ Accountability
Performance contracts: Setting clear expectations for faculty and staff with measurable outcomes.

Regular reviews: Monitoring progress through semester or annual evaluations.

##### 🚀 Long-term Transformation
Industry partnerships: Collaborations for internships, projects, and guest lectures to make the department more relevant.

Leadership change: Appointing new heads or coordinators if current leadership is ineffective.

Culture building: Encouraging innovation, teamwork, and accountability among faculty and students.
#### Impact: 2. Identified a specific 15% "At-Risk" cohort for the current academic year, enabling mentors to start counseling sessions 6 weeks before final exams.
### Depertment View:
#### 1.Find the Subject wise performance rate, 2. Course type impact on performance, 3. Attendance impact on grades, 4. Action Centre: list of students need immediate mentor intervention
### Mentor View:(student 360)
#### 1. Student performance trend, 2. Real-time Risk Status 3. Predictability: Demonstrated that 76% of graduation success is determined by the trajectory established in the first two semesters 5. Retention Analysis

## 🛠️ Technology Stack
* **Excel:** Initial data source and synthetic data generation.
* **SQL Server:** Data Warehousing and ETL using Medallion Architecture.
* **Python (Pandas, Scikit-Learn):** Data manipulation and Predictive Modeling (Linear Regression).
* **Power BI:** Business Intelligence, DAX measures, and interactive reporting.

---

## ☕ Stay Connected

Let's stay in touch! Feel free to connect with me on the following platforms:

<p align="left"> <a href="https://github.com/muhammed-fazal" target="_blank"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/> </a> <a href="http://www.linkedin.com/in/muhammed-fazal-" target="_blank"> <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/> </a> <a href="mailto:fasalcheru@gmail.com"> <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/> </a> <a href="https://x.com/MHD_Fazal_" target="_blank"> <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white" alt="Twitter"/> </a> <a href="http://datascienceportfol.io/muhammedfazal"> <img src="https://img.shields.io/badge/Website-4E9F3D?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website"/> </a> </p>

---
## 🛡️License
This project is licensed under the [MIT Licence](LICENSE). You are free to use, modify, and share this with proper attribution.

## 🧑‍🎓 About Me
Hi there! I’m Muhammed Fazal, a Computer Science engineering graduate driven by a deep passion for data analytics, technology, and innovation.

