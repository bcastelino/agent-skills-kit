# Model Training Reference

## Training Best Practices

### Experiment Setup
```python
import mlflow

mlflow.set_experiment("my-experiment")

with mlflow.start_run(run_name="baseline-v1"):
    # Log parameters
    mlflow.log_params({"model": "xgboost", "lr": 0.1, "max_depth": 6})

    # Train
    model.fit(X_train, y_train)

    # Evaluate and log metrics
    predictions = model.predict(X_test)
    mlflow.log_metrics({"accuracy": accuracy, "f1": f1_score})

    # Save model
    mlflow.sklearn.log_model(model, "model")
```

### Hyperparameter Tuning

#### Grid Search
```python
from sklearn.model_selection import GridSearchCV

param_grid = {"max_depth": [3, 5, 10], "n_estimators": [100, 200]}
search = GridSearchCV(model, param_grid, cv=5, scoring="f1")
search.fit(X_train, y_train)
```

#### Bayesian Optimization
```python
import optuna

def objective(trial):
    lr = trial.suggest_float("lr", 1e-4, 1e-1, log=True)
    depth = trial.suggest_int("max_depth", 3, 15)
    model = XGBClassifier(learning_rate=lr, max_depth=depth)
    return cross_val_score(model, X, y, cv=5).mean()

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)
```

## Model Evaluation

### Classification Metrics
- Accuracy, Precision, Recall, F1-Score
- ROC-AUC, PR-AUC
- Confusion matrix
- Classification report per class

### Regression Metrics
- MAE, MSE, RMSE
- R-squared, Adjusted R-squared
- MAPE (Mean Absolute Percentage Error)
