# Retail Sales ETL Pipeline with Spark & Hive

## 📌 Overview
This project demonstrates a foundational **ETL (Extract, Transform, Load) pipeline** using **Apache Spark** and **Hive**.  
We use the [Superstore dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) as input, transform sales data, and store the results into **Hive partitioned tables** for optimized querying.  

This project is designed to highlight key **data engineering concepts**:
- Spark ETL with DataFrames
- Hive integration with Spark
- Internal vs. External tables
- Partitioned tables for performance optimization

---

## ⚙️ Technologies Used
- Apache Spark (PySpark)
- Hive Metastore
- Parquet format (columnar storage)
- Databricks (execution environment, but portable to any Spark + Hive setup)

---

# Customer Dimension with CDC & Slowly Changing Dimensions (SCD Type 2)

## 📌 Overview
This project demonstrates how to manage **historical changes in customer data** using **Slowly Changing Dimensions (SCD Type 2)** in **Spark + Hive (Databricks)**.  

In real-world data engineering, business entities (like customers) **change over time**:
- Customers move to new regions
- Products change categories
- Employees change departments

If we overwrite values, we **lose history**.  
Using **SCD Type 2**, we **keep the history** by storing multiple records for the same entity with validity dates.

---

## ⚙️ Technologies Used
- Apache Spark (PySpark)
- Hive Metastore
- Databricks (execution environment)

# 🛒 Superstore Sales Data Engineering Pipeline (Databricks + Delta Lake + AWS S3)

This project demonstrates the **end-to-end data engineering lifecycle** using **Databricks, Spark, Delta Lake, and AWS S3**.  

## 🚀 Steps in the Pipeline
1. **Data Ingestion** – Load Superstore CSV data into Spark.
2. **Data Transformation** – Extract Year & Month from `Order Date`.
3. **Data Storage** – Save data in **Parquet format**.
4. **Delta Table Creation** – Create `sales_flat` Delta table with schema enforcement.
5. **Partitioned Table** – Create `sales_partitioned_v3` table partitioned by `Year` and `Month`.

## 🛠️ Tech Stack
- **Apache Spark (PySpark)**
- **Databricks**
- **Delta Lake**
- **AWS S3**

## 🎯 What This Project Showcases
- Modern **data engineering practices** (ETL/ELT pipeline).
- **Delta Lake** features: ACID transactions, schema enforcement, and time travel.
- **Partitioning** strategy for query optimization.
- **Cloud integration** with AWS S3.

## 📊 Use Case
The pipeline supports **business intelligence, sales analytics, and financial reporting** by providing reliable, partitioned, and query-optimized datasets.

# Customer Segmentation & Lifetime Value with SQL

## 📌 Overview
This project demonstrates an **ELT pipeline** using SQL to:
- Clean raw customer and order data.
- Calculate **Customer Lifetime Value (CLV)**.
- Segment customers into **Platinum, Gold, Silver** tiers.

## 🛠 Tech Stack
- SQL (PostgreSQL/MySQL/BigQuery compatible)
- Mock dataset (customers + orders)

## 📂 Project Structure
- `schema.sql` → DDL for tables
- `data.sql` → Sample inserts
- `etl.sql` → Cleaning, transformations, and final segmentation
- `README.md` → Project documentation

## 🚀 Key Features
- Data cleaning (duplicates, NULL handling)
- Window functions
- Aggregations & CASE-based segmentation
- Final customer segments table

## ✅ Business Impact
Companies can use this pipeline to:
- Identify high-value customers (Platinum).
- Build marketing strategies per customer tier.
- Track customer spending trends over time.

---

