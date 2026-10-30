from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("StreamingViviendas") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "viviendas") \
    .load()

consulta = df.writeStream \
    .format("console") \
    .start()

consulta.awaitTermination()