# ML Engineer Implementation Playbook

Detailed patterns and templates for production machine learning systems.

## Model Serving Patterns

### FastAPI Model Server
```python
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
async def predict(features: dict):
    prediction = model.predict([list(features.values())])
    return {"prediction": prediction.tolist()}
```

### Batch Inference Pipeline
```python
def batch_predict(input_path, output_path, batch_size=1000):
    model = load_model("production_model")
    reader = pd.read_csv(input_path, chunksize=batch_size)
    results = []
    for chunk in reader:
        features = preprocess(chunk)
        predictions = model.predict(features)
        chunk["prediction"] = predictions
        results.append(chunk)
    pd.concat(results).to_csv(output_path, index=False)
```

## Feature Engineering

### Feature Store Integration
```python
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo/")
features = store.get_online_features(
    features=["user_features:age", "user_features:purchase_count"],
    entity_rows=[{"user_id": 123}],
).to_dict()
```

## Model Monitoring

### Drift Detection
```python
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=train_df, current_data=prod_df)
report.save_html("drift_report.html")
```

### Performance Monitoring Metrics
| Metric | Threshold | Action |
|--------|-----------|--------|
| Prediction latency | < 100ms p99 | Scale horizontally |
| Model accuracy | > 95% | Retrain if below |
| Feature drift | < 0.1 PSI | Investigate data pipeline |
| Prediction distribution | Within 2 sigma | Alert and investigate |

## ML Pipeline Architecture

### Training Pipeline
1. Data validation (Great Expectations, Pandera)
2. Feature engineering (reproducible transforms)
3. Model training with hyperparameter tuning
4. Model evaluation against holdout set
5. Model registration in model registry
6. Automated testing (unit, integration, model)
7. Deployment with canary or shadow mode
