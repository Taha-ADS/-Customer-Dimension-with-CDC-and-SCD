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


## 📂 Project Structure
