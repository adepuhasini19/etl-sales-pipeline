# 📊 Sales Data ETL Pipeline

A simple Python-based ETL (Extract, Transform, Load) pipeline that processes sales data from a CSV file, performs data cleaning and transformation, and saves the cleaned data to a new file.

---

## 🚀 Project Overview

This project demonstrates a basic ETL workflow:

- **Extract** → Read raw sales data from CSV
- **Transform** → Clean missing values, convert data types, create new features
- **Load** → Save processed data into a new CSV file

This project is built using Python and Pandas.

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas
- NumPy
- Git & GitHub

---

## 📂 Project Structure

```
etl_sales_project/
│
├── data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv
│
├── etl.py
├── requirements.txt
└── README.md
```



## ⚙️ How It Works

### 1️⃣ Extract
Reads raw sales data from:
    
data/sales_data.csv

### 2️⃣ Transform
- Removes missing values
- Converts date column to datetime format
- Creates a new column: `total_price = quantity × price`

### 3️⃣ Load
Saves cleaned data to:

data/cleaned_sales_data.csv


---

## ▶️ How to Run the Project

1. Clone the repository






