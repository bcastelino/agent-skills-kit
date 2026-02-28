# ML Pipeline Workflow Implementation Playbook

Detailed patterns and templates for end-to-end MLOps pipeline development.

## Pipeline Architecture

### Standard ML Pipeline DAG
```yaml
stages:
  data_ingestion:
    inputs: [raw_data_source]
    outputs: [raw_dataset]
  data_validation:
    inputs: [raw_dataset]
    outputs: [validated_dataset]
    checks: [schema, completeness, freshness]
  feature_engineering:
    inputs: [validated_dataset]
    outputs: [feature_store]
  model_training:
    inputs: [feature_store]
    outputs: [trained_model]
    params: [hyperparameters.yaml]
  model_evaluation:
    inputs: [trained_model, test_dataset]
    outputs: [evaluation_report]
  model_deployment:
    inputs: [trained_model, evaluation_report]
    outputs: [deployed_model]
    gate: [evaluation_threshold]
```

## Data Preparation

### Data Validation with Great Expectations
```python
import great_expectations as gx

context = gx.get_context()
validator = context.sources.pandas_default.read_csv("data.csv")
validator.expect_column_values_to_not_be_null("user_id")
validator.expect_column_values_to_be_between("age", 0, 150)
validator.expect_column_values_to_be_in_set("status", ["active", "inactive"])
```

## Model Training

### Hyperparameter Tuning
```python
from sklearn.model_selection import RandomizedSearchCV

param_distributions = {
    "n_estimators": [100, 200, 500],
    "max_depth": [5, 10, 20, None],
    "learning_rate": [0.01, 0.05, 0.1],
}

search = RandomizedSearchCV(
    model, param_distributions, n_iter=20, cv=5, scoring="f1"
)
search.fit(X_train, y_train)
```

## Deployment Patterns

### Canary Deployment
1. Deploy new model alongside production model
2. Route 5% traffic to new model
3. Compare metrics for 24-48 hours
4. Gradually increase traffic if metrics are good
5. Full cutover after validation period

### Shadow Mode
1. Deploy new model receiving production traffic
2. Log predictions but do not serve them
3. Compare new vs current model predictions
4. Switch when confidence is high

## Monitoring and Alerting

### Key Metrics to Track
- **Data Quality**: Schema violations, null rates, distribution shifts
- **Model Performance**: Accuracy, latency, throughput
- **Infrastructure**: CPU/GPU utilization, memory, queue depth
- **Business**: Conversion rate, user engagement, revenue impact
