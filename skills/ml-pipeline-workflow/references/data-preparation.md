# Data Preparation Reference

## Data Validation

### Schema Validation
```python
import pandera as pa

schema = pa.DataFrameSchema({
    "user_id": pa.Column(int, nullable=False, unique=True),
    "age": pa.Column(int, pa.Check.in_range(0, 150)),
    "email": pa.Column(str, pa.Check.str_matches(r".+@.+\..+")),
    "status": pa.Column(str, pa.Check.isin(["active", "inactive"])),
})

validated_df = schema.validate(raw_df)
```

### Data Quality Checks
- **Completeness**: No unexpected nulls in required fields
- **Uniqueness**: Primary keys are unique
- **Consistency**: Related fields agree (e.g., start_date < end_date)
- **Freshness**: Data is recent enough for the use case
- **Volume**: Row count within expected range

## Feature Engineering

### Numerical Features
- Standard scaling: `(x - mean) / std`
- Min-max scaling: `(x - min) / (max - min)`
- Log transform: `log(1 + x)` for skewed distributions
- Binning: Convert continuous to categorical

### Categorical Features
- One-hot encoding for low cardinality
- Target encoding for high cardinality
- Frequency encoding as a simple alternative
- Embedding for very high cardinality (deep learning)

### Temporal Features
- Day of week, month, quarter, year
- Time since event (recency)
- Rolling aggregations (7-day, 30-day averages)
- Seasonal indicators
