from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("Analisis").getOrCreate()

df = spark.read.csv(
    "train.csv",
    header=True,
    inferSchema=True
)

print("Cantidad de registros:")
print(df.count())

print("Precio promedio:")
df.select(avg("SalePrice")).show()

print("Datos:")
df.show()

spark.stop()