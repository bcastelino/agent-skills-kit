# MLOps Engineer Implementation Playbook

Detailed patterns and templates for ML infrastructure automation and lifecycle management.

## Infrastructure Setup

### Kubernetes ML Platform
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model-serving
spec:
  replicas: 3
  selector:
    matchLabels:
      app: model-serving
  template:
    spec:
      containers:
        - name: model-server
          image: model-server:latest
          resources:
            requests:
              memory: "2Gi"
              cpu: "1"
              nvidia.com/gpu: "1"
          ports:
            - containerPort: 8080
```

## CI/CD for ML

### Training Pipeline CI
```yaml
name: ML Pipeline
on:
  push:
    paths: ["models/**", "features/**"]

jobs:
  train:
    runs-on: [self-hosted, gpu]
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: python train.py --config config.yaml
      - run: python evaluate.py --threshold 0.95
      - run: python register_model.py
```

## Experiment Tracking

### MLflow Setup
```python
import mlflow
mlflow.set_tracking_uri("http://mlflow-server:5000")
mlflow.set_experiment("recommendation-model")

with mlflow.start_run():
    mlflow.log_params({"model": "xgboost", "lr": 0.1})
    model.fit(X_train, y_train)
    mlflow.log_metrics({"accuracy": accuracy, "f1": f1})
    mlflow.sklearn.log_model(model, "model")
```

## Model Registry

### Model Lifecycle
| Stage | Description | Automated Check |
|-------|-------------|-----------------|
| Development | Active experimentation | Tests pass |
| Staging | Pre-production validation | Performance threshold |
| Production | Serving live traffic | A/B test results |
| Archived | Deprecated version | Retention policy |

## Monitoring

### Alert Configuration
```yaml
alerts:
  - name: model_accuracy_drop
    metric: model_accuracy
    threshold: 0.90
    comparison: less_than
    window: 1h
    severity: critical
  - name: prediction_latency
    metric: p99_latency_ms
    threshold: 200
    comparison: greater_than
    window: 5m
    severity: warning
```
