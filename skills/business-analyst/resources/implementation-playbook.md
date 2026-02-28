# Business Analyst Implementation Playbook

Detailed patterns, frameworks, and examples for data-driven business analysis.

## Analysis Frameworks

### SWOT Analysis Template
| | Helpful | Harmful |
|---|---------|---------|
| Internal | Strengths | Weaknesses |
| External | Opportunities | Threats |

### Business Case Structure
1. Executive Summary
2. Problem Statement
3. Options Analysis
4. Recommended Solution
5. Financial Impact (ROI, NPV, IRR)
6. Risk Assessment
7. Implementation Timeline

## Data Analysis Patterns

### Exploratory Data Analysis (EDA)
```python
import pandas as pd
import matplotlib.pyplot as plt

def quick_eda(df):
    print(df.describe())
    print(df.info())
    print(df.isnull().sum())
    for col in df.select_dtypes(include=["number"]).columns:
        df[col].hist(bins=30)
        plt.title(col)
        plt.show()
```

### KPI Dashboard Design
- Define metrics hierarchy: North Star -> Primary -> Secondary -> Input
- Use SMART criteria for each KPI
- Include trend lines, targets, and thresholds
- Group by business function

## Stakeholder Communication

### Presentation Structure
1. Hook: Key finding or surprising insight
2. Context: Business background and data sources
3. Analysis: Methods and findings with visualizations
4. Recommendations: Prioritized actions with expected impact
5. Next Steps: Timeline and resource requirements

### Report Templates
- Executive Brief: 1-page summary with key metrics and actions
- Deep Dive: Full analysis with methodology and appendix
- Dashboard: Interactive metrics with drill-down capability

## A/B Testing Guide

### Experiment Design
1. Define hypothesis and success metrics
2. Calculate required sample size
3. Set significance level (typically 0.05)
4. Determine minimum detectable effect
5. Plan rollout and monitoring

### Statistical Methods
- Chi-squared test for categorical outcomes
- T-test for continuous metrics
- Mann-Whitney U for non-normal distributions
- Bayesian methods for faster decisions
