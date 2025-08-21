from pyspark.sql import SparkSession

# Initialize SparkSession with Hive support
spark = SparkSession.builder \
    .appName("SuperstoreAnalysis") \
    .enableHiveSupport() \
    .getOrCreate()

# Load Hive table
df = spark.sql("SELECT * FROM retail.superstore")

# Sales by Category
print("=== Total Sales by Category ===")
df.groupBy("Category").sum("Sales").show()

# Profit by Region
print("=== Total Profit by Region ===")
df.groupBy("Region").sum("Profit").show()

# Sales & Profit by State
print("=== Sales & Profit by State ===")
result = df.groupBy("State").sum("Sales", "Profit")
result.show()

# Save aggregated results back into Hive
result.write.mode("overwrite").saveAsTable("retail.sales_by_state")

print("=== Aggregated results saved to Hive table: retail.sales_by_state ===")

spark.stop()
