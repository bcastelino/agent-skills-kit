# Data Scientist Implementation Playbook

Detailed patterns, templates, and code examples for advanced analytics and machine learning.

## Exploratory Data Analysis

### Standard EDA Workflow
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def comprehensive_eda(df):
    print(f"Shape: {df.shape}")
    print(f"Types:\n{df.dtypes}")
    print(f"Missing:\n{df.isnull().sum()}")
    print(df.describe())

    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

    for col in df.select_dtypes(include=[np.number]).columns:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        df[col].hist(bins=30, ax=axes[0])
        axes[0].set_title(f"{col} - Distribution")
        df.boxplot(column=col, ax=axes[1])
        axes[1].set_title(f"{col} - Box Plot")
        plt.tight_layout()
        plt.show()
```

## Model Development

### Train-Test Split Best Practices
```python
from sklearn.model_selection import train_test_split, cross_val_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scores = cross_val_score(model, X, y, cv=5, scoring="f1_macro")
print(f"CV Score: {scores.mean():.3f} +/- {scores.std():.3f}")
```

### Feature Engineering Patterns
- **Numerical**: Scaling, binning, log transform, polynomial features
- **Categorical**: One-hot encoding, target encoding, frequency encoding
- **Temporal**: Time-based features, lag features, rolling statistics
- **Text**: TF-IDF, word embeddings, sentiment features

## Experiment Tracking

### MLflow Integration
```python
import mlflow

with mlflow.start_run(run_name="experiment_v1"):
    mlflow.log_params({"model": "xgboost", "lr": 0.1})
    mlflow.log_metrics({"accuracy": 0.95, "f1": 0.92})
    mlflow.sklearn.log_model(model, "model")
```

## Statistical Testing

### Choosing the Right Test
| Data Type | Groups | Normal | Test |
|-----------|--------|--------|------|
| Continuous | 2 | Yes | T-test |
| Continuous | 2 | No | Mann-Whitney U |
| Continuous | 3+ | Yes | ANOVA |
| Continuous | 3+ | No | Kruskal-Wallis |
| Categorical | 2+ | N/A | Chi-squared |
