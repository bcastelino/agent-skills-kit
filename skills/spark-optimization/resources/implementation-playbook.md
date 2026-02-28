# Spark Optimization Implementation Playbook

Detailed patterns and tuning guides for Apache Spark job optimization.

## Partition Tuning

### Right-Sizing Partitions
```python
data_size_gb = 100
target_partition_mb = 200
num_partitions = int(data_size_gb * 1024 / target_partition_mb)
df = spark.read.parquet("data/").repartition(num_partitions)
```

### Partition Strategies
| Strategy | When to Use | Example |
|----------|-------------|---------|
| Hash partitioning | Even distribution | `repartition(200, "key")` |
| Range partitioning | Sorted output | `repartitionByRange(200, "date")` |
| Coalesce | Reduce partitions | `coalesce(50)` (no shuffle) |
| Custom | Domain-specific | Salted keys for skew |

## Shuffle Optimization

### Reducing Shuffles
```python
from pyspark.sql.functions import broadcast
result = large_df.join(broadcast(small_df), "key")

# Pre-partition for multiple joins on same key
df = df.repartition(200, "user_id").cache()
result1 = df.join(table1, "user_id")
result2 = df.join(table2, "user_id")
```

### Shuffle Service Configuration
```python
spark.conf.set("spark.shuffle.service.enabled", "true")
spark.conf.set("spark.sql.shuffle.partitions", "200")
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
```

## Caching Strategies

### When to Cache
- DataFrame used multiple times in same job
- After expensive transformations (joins, aggregations)
- Small lookup tables used repeatedly

```python
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK_SER)
df.count()  # Trigger materialization
```

## Memory Tuning

### Executor Configuration
```python
spark.conf.set("spark.executor.memory", "8g")
spark.conf.set("spark.executor.memoryOverhead", "2g")
spark.conf.set("spark.memory.fraction", "0.6")
spark.conf.set("spark.memory.storageFraction", "0.5")
```

## Data Skew Handling

### Salt Key Technique
```python
import pyspark.sql.functions as F

salt_range = 10
skewed_df = skewed_df.withColumn(
    "salted_key",
    F.concat(F.col("key"), F.lit("_"), (F.rand() * salt_range).cast("int")),
)

small_df_salted = small_df.crossJoin(
    spark.range(salt_range).withColumnRenamed("id", "salt")
).withColumn(
    "salted_key",
    F.concat(F.col("key"), F.lit("_"), F.col("salt")),
)

result = skewed_df.join(small_df_salted, "salted_key")
```
