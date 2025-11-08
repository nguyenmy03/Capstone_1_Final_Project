# Midterm Analysis Write-up

## 🧭 Problem Framing & Goals
The goal of this midterm project was to build an end-to-end data analytics pipeline using California’s public **School Sites 2024–25** dataset.  
The purpose was to visualize trends in school enrollment, geographic distribution, and operational activity across districts.  
This dashboard helps identify which school types serve the most students, which counties have the highest total enrollment, and when schools were most actively established.

---

## 🗂️ Data Overview
The dataset was sourced from the **California Open Data Portal**, containing public K-12 school information for the 2024–25 academic year.  

**Fields kept:**  
`academic_year`, `county_name`, `district_name`, `school_name`, `school_type`, `status`, `open_date`, `city`, `zip`, `latitude`, `longitude`, and key enrollment metrics (`enroll_total`, `african_american`, `hispanic`, `asian`).  

**Fields dropped:**  
Administrative IDs and columns with incomplete or redundant data.  

**Assumptions:**  
Only **active schools** were analyzed, and missing coordinates or null enrollments were excluded to maintain accuracy.

---

## ⚙️ Methods
- Data uploaded and cleaned in **BigQuery** under `MIDTERM.nms_midterm_PUB`.  
- SQL queries aggregated total enrollment by `school_type` and `county_name`, filtered by `status = 'Active'`.  
- Time-based parsing of `open_date` fields allowed trend analysis of schools opened per decade.  
- Visualization tools: **Grafana panels** (Pie chart, Bar chart, Stat panel, Time-series line chart, and Table).  

---

## 📊 Findings
- **Pie Chart:** *Enrollment Distribution by School Type (Top 5)* shows that **elementary and high schools** account for most of California’s total student enrollment, while charter and alternative schools serve smaller segments.  
- **Bar Chart:** *Enrollment by County* highlights **Los Angeles** as the county with the highest student population (~10,000), followed by **San Diego** and **Orange** counties.  
- **Stat Panel:** Displays the **total number of active schools (99)** in the dataset.  
- **Time-Series Chart:** *Schools Opened Per Month* shows a large spike around the **1980s**, reflecting a period of strong educational infrastructure expansion.  
- **Table Panel:** Lists active schools by enrollment, offering details on district, city, and status for quick lookup.

---

## ⚠️ Limitations & Next Steps
Some records lacked demographic details (e.g., ethnicity percentages), which limited deeper equity analysis.  
The dataset also contains inconsistent date formatting for `open_date`.  

**Next steps:**  
Integrate a demographic breakdown panel, map schools geographically using **latitude/longitude**, and connect external datasets for performance or funding correlations.
