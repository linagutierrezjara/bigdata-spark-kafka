from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min

spark = SparkSession.builder.appName("Analisis").getOrCreate()

df = spark.read.csv(
    "train.csv",
    header=True,
    inferSchema=True
)

print("Registros antes de limpieza:")
print(df.count())

df = df.na.drop()

print("Registros después de limpieza:")
print(df.count())

print("Precio promedio:")
df.select(avg("SalePrice")).show()

print("Precio máximo:")
df.select(max("SalePrice")).show()

print("Precio mínimo:")
df.select(min("SalePrice")).show()

print("Datos:")
df.show()

spark.stop()
