"""Generate missing resources/implementation-playbook.md files."""
import os
import re

SKILLS_ROOT = os.path.join(os.path.dirname(__file__), '..', 'skills')

# Playbook content keyed by skill name
PLAYBOOKS = {
    "business-analyst": """# Business Analyst Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Data-Driven Decision Framework
- Define clear business questions before analysis
- Map KPIs to measurable metrics
- Establish baselines before proposing changes
- Use statistical significance thresholds (p < 0.05)

### 2. Stakeholder Communication
- Tailor detail level to audience (executive summary vs technical deep-dive)
- Lead with insights, not methodology
- Use visualizations to support narrative

### 3. Requirements Gathering
- SMART criteria: Specific, Measurable, Achievable, Relevant, Time-bound
- User story format: "As a [role], I want [feature], so that [benefit]"
- Acceptance criteria checklist for every requirement

## Analysis Patterns

### 1. Exploratory Data Analysis (EDA)
```python
import pandas as pd
import matplotlib.pyplot as plt

def quick_eda(df: pd.DataFrame) -> dict:
    return {
        "shape": df.shape,
        "dtypes": df.dtypes.value_counts().to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum(),
        "numeric_summary": df.describe().to_dict(),
    }
```

### 2. A/B Test Analysis
```python
from scipy import stats

def ab_test_significance(control: list, treatment: list, alpha=0.05):
    t_stat, p_value = stats.ttest_ind(control, treatment)
    return {
        "t_statistic": t_stat,
        "p_value": p_value,
        "significant": p_value < alpha,
        "recommendation": "Adopt treatment" if p_value < alpha else "No significant difference"
    }
```

### 3. ROI Calculation Template
```
Revenue Impact = (New Metric - Baseline) × Unit Value × Volume
Cost = Development + Infrastructure + Maintenance
ROI = (Revenue Impact - Cost) / Cost × 100%
Payback Period = Cost / Monthly Revenue Impact
```

## Dashboard Design Checklist
- [ ] Single key metric prominently displayed
- [ ] Time-series trends with clear annotations
- [ ] Comparison to targets/benchmarks
- [ ] Drill-down capability for root cause analysis
- [ ] Mobile-friendly layout
- [ ] Refresh cadence documented

## Best Practices
1. Always validate data quality before analysis
2. Document assumptions and limitations
3. Present confidence intervals, not point estimates
4. Maintain a decision log linking analysis to outcomes
5. Version control all analysis scripts and queries

## Common Pitfalls
- Confusing correlation with causation
- Survivorship bias in historical analysis
- Ignoring seasonality in time-series data
- Over-fitting models to small samples
- Presenting data without actionable recommendations
""",

    "cloud-architect": """# Cloud Architect Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Well-Architected Framework Pillars
- **Operational Excellence**: Automate operations, prepare for failure
- **Security**: Defense in depth, least privilege, encryption at rest/in transit
- **Reliability**: Fault isolation, auto-scaling, multi-AZ/region design
- **Performance Efficiency**: Right-sizing, caching, CDN optimization
- **Cost Optimization**: Reserved capacity, spot instances, right-sizing
- **Sustainability**: Efficient resource utilization, carbon-aware scheduling

### 2. Infrastructure as Code (IaC) Patterns
```hcl
# Terraform module pattern
module "vpc" {
  source  = "./modules/vpc"
  cidr    = var.vpc_cidr
  azs     = var.availability_zones
  tags    = local.common_tags
}

module "eks" {
  source     = "./modules/eks"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
  node_groups = var.node_groups
}
```

### 3. Multi-Cloud Decision Matrix
| Factor | AWS | Azure | GCP |
|--------|-----|-------|-----|
| Compute | EC2/ECS/Lambda | VMs/AKS/Functions | GCE/GKE/Cloud Run |
| Database | RDS/DynamoDB | CosmosDB/SQL | Cloud SQL/Spanner |
| AI/ML | SageMaker | Azure ML | Vertex AI |
| Best for | Enterprise breadth | Hybrid/Microsoft | Data/ML workloads |

## Architecture Patterns

### 1. Microservices Reference Architecture
```
[API Gateway] → [Service Mesh] → [Microservices]
                                    ├── Auth Service
                                    ├── User Service
                                    ├── Order Service
                                    └── Notification Service
                  [Message Queue] ←→ [Event Bus]
                  [Shared Cache]  ←→ [Service Registry]
```

### 2. DR Strategy Tiers
- **Backup & Restore**: RPO hours, RTO hours (lowest cost)
- **Pilot Light**: RPO minutes, RTO 10s of minutes
- **Warm Standby**: RPO seconds, RTO minutes
- **Multi-Site Active/Active**: RPO ~0, RTO ~0 (highest cost)

## FinOps Checklist
- [ ] Tag all resources with cost-center, environment, owner
- [ ] Set budget alerts at 50%, 80%, 100% thresholds
- [ ] Review Reserved Instance coverage monthly
- [ ] Right-size instances based on utilization metrics
- [ ] Implement auto-scaling policies
- [ ] Use spot/preemptible for fault-tolerant workloads

## Best Practices
1. Design for failure — assume every component can fail
2. Implement infrastructure as code for all environments
3. Use immutable infrastructure patterns
4. Enforce least-privilege IAM policies
5. Encrypt everything: data at rest and in transit
6. Monitor with distributed tracing and centralized logging

## Common Pitfalls
- Over-engineering for scale before validating demand
- Ignoring data gravity when choosing regions
- Hardcoding configuration instead of using parameter stores
- Neglecting cost optimization during initial architecture
- Single-AZ deployments in production
""",

    "code-refactoring-context-restore": """# Context Restore Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Context Recovery Strategy
When resuming work on an unfamiliar or complex codebase:
1. **Map the architecture** — identify entry points, core modules, data flow
2. **Trace the execution** — follow key user flows through the code
3. **Identify patterns** — recognize design patterns and conventions used
4. **Document discoveries** — create context maps for future reference

### 2. Codebase Exploration Techniques
```bash
# Quick architecture overview
find . -name "*.py" | head -50
grep -r "class " --include="*.py" -l | sort
grep -r "def main" --include="*.py"
grep -r "import" --include="*.py" | cut -d: -f2 | sort | uniq -c | sort -rn | head -20

# Dependency graph
pipdeptree --graph-output png > deps.png
```

### 3. Context Map Template
```markdown
## Module: [name]
- **Purpose**: [one sentence]
- **Key classes**: [list]
- **Dependencies**: [imports from]
- **Dependents**: [imported by]
- **Entry points**: [public API]
- **State**: [stateless/stateful, persistence mechanism]
- **Tests**: [test file location, coverage %]
```

## Recovery Patterns

### 1. Top-Down Exploration
Start from entry points and work inward:
1. Find `main()`, `app()`, or framework entry points
2. Identify routing/dispatch layer
3. Map service/business logic layer
4. Understand data access layer
5. Note cross-cutting concerns (auth, logging, errors)

### 2. Bottom-Up from Bug Reports
When restoring context to fix a specific issue:
1. Reproduce the issue and capture the stack trace
2. Identify the failing function/line
3. Trace callers upward to understand invocation context
4. Map data flow to understand state at failure point
5. Check recent git history for related changes

### 3. Git Archaeology
```bash
# Who works on what
git shortlog -sn --all -- path/to/module/
# Recent changes in area of interest
git log --oneline -20 -- path/to/module/
# When was a function last changed
git log -1 --format="%ai %an" -S "function_name"
```

## Checklist: Before Making Changes
- [ ] Can describe the module's purpose in one sentence
- [ ] Know the data flow for the feature being changed
- [ ] Have identified all callers of the function being modified
- [ ] Have located relevant tests
- [ ] Understand the deployment pipeline
- [ ] Have a rollback plan

## Best Practices
1. Never refactor and add features in the same commit
2. Write characterization tests before changing legacy code
3. Use IDE navigation (go-to-definition, find-references) extensively
4. Create scratch notes documenting your exploration path
5. Time-box exploration — set limits before diving deeper
""",

    "code-reviewer": """# Code Reviewer Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Review Priorities (ordered)
1. **Correctness** — Does it work? Edge cases handled?
2. **Security** — Injection, auth bypass, data exposure?
3. **Performance** — N+1 queries, unnecessary allocations, blocking I/O?
4. **Maintainability** — Readable, well-named, appropriate abstractions?
5. **Testing** — Adequate coverage, meaningful assertions?

### 2. Review Comment Categories
- 🔴 **Blocker**: Must fix before merge (security, correctness)
- 🟡 **Suggestion**: Recommended improvement (performance, maintainability)
- 🟢 **Nit**: Minor style/naming preference (optional)
- 💡 **Question**: Seeking understanding (not a change request)

### 3. Constructive Feedback Patterns
```
❌ "This is wrong."
✅ "This may cause an issue when X is null — consider adding a guard clause."

❌ "Don't do it this way."
✅ "Have you considered using Y here? It handles Z edge case more cleanly."
```

## Review Checklists

### Security Review
- [ ] No hardcoded secrets or credentials
- [ ] Input validation on all user-supplied data
- [ ] SQL queries use parameterized statements
- [ ] Authentication checks on all protected endpoints
- [ ] Sensitive data not logged or exposed in errors

### Performance Review
- [ ] Database queries are indexed for common access patterns
- [ ] No N+1 query patterns
- [ ] Large collections use pagination
- [ ] Expensive operations are cached where appropriate
- [ ] Async/await used correctly for I/O operations

### Testing Review
- [ ] Happy path tests present
- [ ] Edge cases covered (empty, null, boundary values)
- [ ] Error conditions tested
- [ ] Mocks used appropriately (not over-mocked)
- [ ] Tests are deterministic (no flaky dependencies)

## Review Output Template
```markdown
## Summary
[One-paragraph overview of the change and its impact]

## Strengths
- [What's done well]

## Required Changes
- 🔴 [file:line] [Description of blocker]

## Suggestions
- 🟡 [file:line] [Description of improvement]

## Questions
- 💡 [Question about design decision]

## Verdict
[APPROVE / REQUEST_CHANGES / NEEDS_DISCUSSION]
```

## Best Practices
1. Review in under 60 minutes — take breaks for large PRs
2. Focus on logic, not style (use linters for style)
3. Praise good patterns alongside critique
4. Ask questions rather than make demands
5. Review your own code first before requesting review

## Common Pitfalls
- Bikeshedding on style while missing logic bugs
- Rubber-stamping large PRs without thorough review
- Being overly critical without offering alternatives
- Reviewing too much code at once (>400 lines loses effectiveness)
""",

    "data-engineering-data-driven-feature": """# Data-Driven Feature Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Feature Development Lifecycle
1. **Hypothesis** — Define what you expect to happen and why
2. **Instrumentation** — Add metrics/events to measure the outcome
3. **Implementation** — Build the feature with measurement hooks
4. **Experiment** — A/B test or staged rollout
5. **Analysis** — Evaluate results against hypothesis
6. **Decision** — Ship, iterate, or revert based on data

### 2. Metric Types
- **North Star Metric**: Single metric capturing core value (e.g., weekly active users)
- **Driver Metrics**: Levers that influence the north star (e.g., onboarding completion)
- **Guardrail Metrics**: Ensure no regression (e.g., error rate, latency, churn)

### 3. Event Schema Design
```python
# Standard event structure
event = {
    "event_name": "feature_used",
    "timestamp": "2024-01-15T10:30:00Z",
    "user_id": "u_123",
    "session_id": "s_456",
    "properties": {
        "feature_name": "smart_search",
        "variant": "treatment_a",
        "latency_ms": 142,
        "result_count": 15
    }
}
```

## A/B Testing Patterns

### 1. Sample Size Calculator
```python
from scipy.stats import norm
import math

def min_sample_size(baseline_rate, mde, alpha=0.05, power=0.80):
    z_alpha = norm.ppf(1 - alpha / 2)
    z_beta = norm.ppf(power)
    p = baseline_rate
    delta = mde
    n = (2 * p * (1 - p) * (z_alpha + z_beta) ** 2) / (delta ** 2)
    return math.ceil(n)
```

### 2. Feature Flag Integration
```python
def get_feature_variant(user_id: str, experiment: str) -> str:
    # Deterministic bucketing
    hash_val = hash(f"{user_id}:{experiment}") % 100
    if hash_val < 50:
        return "control"
    return "treatment"
```

## Instrumentation Checklist
- [ ] Define primary metric and expected lift
- [ ] Set guardrail metrics with thresholds
- [ ] Implement event tracking for all user interactions
- [ ] Validate events in staging before launch
- [ ] Set up real-time monitoring dashboard
- [ ] Document experiment in experiment tracker

## Best Practices
1. Define success criteria before building
2. Use deterministic bucketing for consistent user experience
3. Run experiments for at least 2 full business cycles
4. Check for novelty effects by monitoring metrics over time
5. Document all experiment results regardless of outcome

## Common Pitfalls
- Peeking at results before reaching sample size
- Not accounting for multiple comparisons
- Ignoring network effects in social features
- Changing experiment parameters mid-flight
- Launching without guardrail metrics
""",

    "data-scientist": """# Data Scientist Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Analysis Workflow
1. **Problem Framing** — Translate business question into analytical approach
2. **Data Collection** — Gather, validate, and profile data sources
3. **EDA** — Explore distributions, relationships, and anomalies
4. **Feature Engineering** — Transform raw data into predictive signals
5. **Modeling** — Train, validate, and compare models
6. **Interpretation** — Explain results in business context
7. **Deployment** — Operationalize model or deliver insights

### 2. Statistical Testing Framework
```python
from scipy import stats

def choose_test(data_type, groups, paired=False):
    if data_type == "continuous":
        if groups == 2:
            return stats.ttest_rel if paired else stats.ttest_ind
        return stats.f_oneway
    elif data_type == "categorical":
        return stats.chi2_contingency
    elif data_type == "ordinal":
        return stats.mannwhitneyu if groups == 2 else stats.kruskal
```

### 3. Feature Engineering Patterns
```python
import pandas as pd
import numpy as np

def temporal_features(df, date_col):
    df['day_of_week'] = df[date_col].dt.dayofweek
    df['month'] = df[date_col].dt.month
    df['is_weekend'] = df[date_col].dt.dayofweek >= 5
    df['days_since_start'] = (df[date_col] - df[date_col].min()).dt.days
    return df

def interaction_features(df, col_a, col_b):
    df[f'{col_a}_x_{col_b}'] = df[col_a] * df[col_b]
    df[f'{col_a}_div_{col_b}'] = df[col_a] / df[col_b].replace(0, np.nan)
    return df
```

## Model Selection Guide
| Problem Type | Small Data (<10K) | Medium (10K-1M) | Large (>1M) |
|---|---|---|---|
| Classification | Logistic Regression, SVM | Random Forest, XGBoost | Neural Networks |
| Regression | Linear Regression, Ridge | Gradient Boosting | Deep Learning |
| Clustering | K-Means, DBSCAN | Mini-Batch K-Means | Approximate NN |
| Time Series | ARIMA, Prophet | LightGBM | Transformer |

## Model Evaluation Checklist
- [ ] Train/validation/test split (no data leakage)
- [ ] Cross-validation for reliable estimates
- [ ] Multiple metrics evaluated (not just accuracy)
- [ ] Calibration checked for probabilistic predictions
- [ ] Fairness metrics across protected groups
- [ ] Learning curves plotted for overfitting detection

## Best Practices
1. Start simple — baseline models before complex ones
2. Validate assumptions (normality, independence, stationarity)
3. Use cross-validation, not single train/test split
4. Report confidence intervals, not point estimates
5. Version control data, code, and models together
6. Document methodology for reproducibility

## Common Pitfalls
- Data leakage from future information in features
- Over-fitting to validation set through repeated evaluation
- Ignoring class imbalance in classification
- Using accuracy alone for imbalanced datasets
- Not checking for distribution shift between train and production
""",

    "data-storytelling": """# Data Storytelling Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Story Arc for Data
1. **Hook** — Surprising fact or compelling question
2. **Context** — Background the audience needs
3. **Rising Action** — Build through data exploration
4. **Insight** — The key finding (climax)
5. **Implication** — What this means for the audience
6. **Call to Action** — What should happen next

### 2. Visualization Selection Matrix
| Data Relationship | Chart Type | When to Use |
|---|---|---|
| Comparison | Bar chart | Comparing categories |
| Trend | Line chart | Changes over time |
| Distribution | Histogram/box plot | Understanding spread |
| Composition | Stacked bar/pie | Parts of a whole |
| Correlation | Scatter plot | Two-variable relationships |
| Geographic | Choropleth/bubble map | Location-based data |

### 3. Audience-Adapted Detail Levels
- **Executive**: 1-3 key metrics, clear recommendation, one slide
- **Manager**: Trends, comparisons, options with trade-offs, 3-5 slides
- **Analyst**: Methodology, statistical details, full dataset access, report

## Visualization Best Practices

### 1. Chart Design Principles
```python
import matplotlib.pyplot as plt

def clean_chart(ax, title, subtitle=""):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(title, fontsize=14, fontweight='bold', loc='left')
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes,
                fontsize=10, color='gray', va='bottom')
    ax.tick_params(axis='both', which='both', length=0)
    return ax
```

### 2. Color Usage Guidelines
- Use sequential palette for ordered data (light → dark)
- Use diverging palette for data with meaningful midpoint
- Use categorical palette for nominal groups (max 7 colors)
- Highlight the key insight with accent color, gray everything else

## Presentation Checklist
- [ ] Title states the insight, not the topic
- [ ] Every chart has a clear takeaway
- [ ] Annotations highlight key data points
- [ ] Consistent color encoding throughout
- [ ] Source and date on every data slide
- [ ] Call to action on final slide

## Best Practices
1. Lead with the "so what", not the methodology
2. One chart, one message — never overload
3. Use annotations to guide the viewer's eye
4. Remove chartjunk (unnecessary gridlines, 3D effects, decorations)
5. Test your narrative with someone unfamiliar with the data

## Common Pitfalls
- Starting with methodology instead of insights
- Truncating axes to exaggerate differences
- Using pie charts for more than 5 categories
- Presenting data without context or benchmarks
- Overwhelming slides with too many numbers
""",

    "database-migration": """# Database Migration Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Migration Strategy Selection
| Strategy | Downtime | Complexity | Risk | Best For |
|---|---|---|---|---|
| Big Bang | Hours | Low | High | Small DBs, maintenance windows |
| Blue-Green | Minutes | Medium | Medium | Stateless apps |
| Rolling | Zero | High | Low | Large production systems |
| Strangler Fig | Zero | High | Low | Legacy to modern migration |

### 2. Schema Migration Pattern
```sql
-- Forward migration
ALTER TABLE users ADD COLUMN email_verified BOOLEAN DEFAULT FALSE;
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- Rollback migration
DROP INDEX CONCURRENTLY IF EXISTS idx_users_email;
ALTER TABLE users DROP COLUMN IF EXISTS email_verified;
```

### 3. Data Transformation Template
```python
def migrate_data_batch(source_conn, target_conn, batch_size=1000):
    offset = 0
    while True:
        rows = source_conn.execute(
            f"SELECT * FROM old_table LIMIT {batch_size} OFFSET {offset}"
        ).fetchall()
        if not rows:
            break
        transformed = [transform_row(row) for row in rows]
        target_conn.executemany(
            "INSERT INTO new_table VALUES (?, ?, ?)", transformed
        )
        target_conn.commit()
        offset += batch_size
        print(f"Migrated {offset} rows...")
```

## Zero-Downtime Migration Steps

### 1. Expand Phase
- Add new columns/tables alongside existing ones
- Deploy code that writes to both old and new structures
- Backfill new structures from existing data

### 2. Migrate Phase
- Switch reads to new structure
- Verify data consistency between old and new
- Monitor for errors and performance regression

### 3. Contract Phase
- Remove writes to old structure
- Drop old columns/tables after verification period
- Clean up dual-write code

## Pre-Migration Checklist
- [ ] Full backup verified and tested
- [ ] Rollback script written and tested
- [ ] Estimated migration time calculated
- [ ] Maintenance window communicated (if needed)
- [ ] Monitoring dashboards configured
- [ ] Data validation queries prepared

## Best Practices
1. Always have a tested rollback plan
2. Migrate in small, reversible steps
3. Use transactions for data consistency
4. Test migration on production-size data copy
5. Monitor query performance after schema changes

## Common Pitfalls
- Running migrations without backups
- Locking tables during long-running migrations
- Not testing rollback procedures
- Forgetting to update ORM models after schema changes
- Ignoring index impact on write-heavy tables during migration
""",

    "database-optimizer": """# Database Optimizer Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Query Optimization Workflow
1. **Identify** — Find slow queries (slow query log, pg_stat_statements)
2. **Analyze** — Run EXPLAIN ANALYZE to understand execution plan
3. **Optimize** — Apply appropriate technique (index, rewrite, cache)
4. **Validate** — Measure improvement with before/after benchmarks
5. **Monitor** — Track performance over time for regression

### 2. EXPLAIN Output Reading
```sql
-- PostgreSQL
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, COUNT(o.id)
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01'
GROUP BY u.name;
```

Key indicators:
- **Seq Scan** on large tables → needs index
- **Nested Loop** with large outer → consider Hash Join
- **Sort** with high cost → add index for ORDER BY
- **Buffers shared read** high → data not cached

### 3. Index Strategy Decision Tree
```
Is the column in WHERE/JOIN/ORDER BY?
├── No → Don't index
└── Yes → What's the cardinality?
    ├── Very low (boolean) → Partial index
    ├── Medium → B-tree index
    └── High (unique-ish) → B-tree or Hash index
        └── Is it a text search? → GIN/GiST index
```

## Optimization Patterns

### 1. N+1 Query Fix
```python
# Bad: N+1 queries
users = db.query(User).all()
for user in users:
    orders = db.query(Order).filter_by(user_id=user.id).all()

# Good: Eager loading
users = db.query(User).options(joinedload(User.orders)).all()
```

### 2. Pagination Optimization
```sql
-- Bad: OFFSET pagination (scans skipped rows)
SELECT * FROM events ORDER BY id LIMIT 20 OFFSET 10000;

-- Good: Keyset pagination (uses index)
SELECT * FROM events WHERE id > 10000 ORDER BY id LIMIT 20;
```

## Performance Tuning Checklist
- [ ] Slow query log enabled and reviewed
- [ ] Missing indexes identified via pg_stat_user_tables
- [ ] Connection pooling configured (PgBouncer/pgpool)
- [ ] Query plans cached (prepared statements)
- [ ] Vacuum and analyze running on schedule
- [ ] Appropriate work_mem and shared_buffers set

## Best Practices
1. Measure before optimizing — don't guess bottlenecks
2. Add indexes for read-heavy patterns, minimize for write-heavy
3. Use connection pooling for all production databases
4. Partition large tables by time or tenant
5. Archive old data to keep working set small

## Common Pitfalls
- Adding indexes without measuring write impact
- Over-indexing (indexes on every column)
- Using SELECT * when only specific columns needed
- Not using parameterized queries (plan cache misses)
- Ignoring table bloat and vacuum schedules
""",

    "embedding-strategies": """# Embedding Strategies Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Embedding Model Selection
| Model | Dimensions | Speed | Quality | Best For |
|---|---|---|---|---|
| text-embedding-3-small | 1536 | Fast | Good | General purpose |
| text-embedding-3-large | 3072 | Medium | Excellent | High-precision RAG |
| all-MiniLM-L6-v2 | 384 | Very fast | Good | On-device, low latency |
| BGE-large-en | 1024 | Medium | Excellent | MTEB benchmark leader |
| Cohere embed-v3 | 1024 | Fast | Excellent | Multilingual |

### 2. Chunking Strategies
```python
def fixed_size_chunks(text, chunk_size=512, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def semantic_chunks(text, headers_regex=r'^#{1,3} '):
    import re
    sections = re.split(headers_regex, text, flags=re.MULTILINE)
    return [s.strip() for s in sections if s.strip()]
```

### 3. Distance Metrics
- **Cosine Similarity**: Best for normalized embeddings (most common)
- **Euclidean Distance**: Good for dense, non-normalized vectors
- **Dot Product**: Fastest; equivalent to cosine for normalized vectors

## Implementation Patterns

### 1. Embedding Pipeline
```python
from openai import OpenAI

client = OpenAI()

def embed_documents(texts: list[str], model="text-embedding-3-small"):
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]

def embed_query(query: str, model="text-embedding-3-small"):
    response = client.embeddings.create(input=[query], model=model)
    return response.data[0].embedding
```

### 2. Hybrid Search
```python
def hybrid_search(query, vector_results, keyword_results, alpha=0.7):
    # Reciprocal Rank Fusion
    scores = {}
    for rank, doc in enumerate(vector_results):
        scores[doc.id] = scores.get(doc.id, 0) + alpha / (rank + 60)
    for rank, doc in enumerate(keyword_results):
        scores[doc.id] = scores.get(doc.id, 0) + (1 - alpha) / (rank + 60)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
```

## Quality Evaluation Checklist
- [ ] Test retrieval with representative queries
- [ ] Measure recall@k and precision@k
- [ ] Compare chunking strategies on your data
- [ ] Evaluate with domain-specific edge cases
- [ ] Benchmark latency at expected query volume
- [ ] Test with multilingual content (if applicable)

## Best Practices
1. Chunk at semantic boundaries, not arbitrary sizes
2. Include metadata in chunks for filtering
3. Use hybrid search (vector + keyword) for best recall
4. Benchmark multiple models on YOUR data, not just leaderboards
5. Re-embed periodically as models improve

## Common Pitfalls
- Chunks too large (diluted semantics) or too small (lost context)
- Not normalizing vectors before cosine similarity
- Embedding queries and documents with different models
- Ignoring metadata filtering opportunities
- Over-relying on vector search without keyword fallback
""",

    "fastapi-pro": """# FastAPI Pro Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Application Structure
```
app/
├── main.py              # FastAPI app instance, middleware, startup
├── api/
│   ├── v1/
│   │   ├── endpoints/   # Route handlers
│   │   └── deps.py      # Shared dependencies
├── core/
│   ├── config.py        # Settings (pydantic-settings)
│   ├── security.py      # Auth utilities
│   └── database.py      # DB session management
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── services/            # Business logic
└── tests/
```

### 2. Async Patterns
```python
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### 3. Dependency Injection
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def get_current_user(token = Depends(security)):
    user = await verify_token(token.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

async def require_admin(user = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin required")
    return user
```

## Performance Patterns

### 1. Background Tasks
```python
from fastapi import BackgroundTasks

@app.post("/send-email")
async def send_email(bg: BackgroundTasks, email: EmailSchema):
    bg.add_task(send_email_task, email.to, email.body)
    return {"status": "queued"}
```

### 2. Response Caching
```python
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

@app.get("/expensive")
@cache(expire=300)
async def expensive_operation():
    return await compute_heavy_result()
```

## Production Checklist
- [ ] CORS middleware configured for allowed origins
- [ ] Rate limiting enabled (slowapi or similar)
- [ ] Health check endpoint at /health
- [ ] Structured logging (structlog or loguru)
- [ ] Error handlers return consistent JSON format
- [ ] OpenAPI docs disabled in production (or auth-protected)

## Best Practices
1. Use Pydantic models for all request/response validation
2. Keep route handlers thin — delegate to service layer
3. Use dependency injection for cross-cutting concerns
4. Implement proper error handling with custom exception handlers
5. Use async for I/O-bound operations, sync for CPU-bound

## Common Pitfalls
- Blocking async event loop with synchronous database calls
- Not using connection pooling for database access
- Putting business logic in route handlers
- Missing input validation on path/query parameters
- Not handling database transaction rollbacks properly
""",

    "full-stack-orchestration-full-stack-feature": """# Full-Stack Feature Orchestration Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Feature Development Phases
1. **Architecture & Design** — API contracts, database schema, component hierarchy
2. **Parallel Development** — Backend and frontend can work simultaneously
3. **Integration** — Connect frontend to backend, end-to-end testing
4. **Deployment** — Staged rollout with feature flags

### 2. API Contract First
```yaml
# OpenAPI spec defined before implementation
paths:
  /api/v1/tasks:
    get:
      summary: List tasks
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, completed, archived]
      responses:
        200:
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Task'
```

### 3. Full-Stack Checklist Per Feature
- [ ] Database migration written and tested
- [ ] API endpoints with request/response validation
- [ ] Unit tests for backend logic
- [ ] Frontend components with props typed
- [ ] API integration with error handling
- [ ] E2E test for critical user flow
- [ ] Feature flag for controlled rollout

## Integration Patterns

### 1. Type-Safe API Layer
```typescript
// Shared types generated from OpenAPI
interface Task {
  id: string;
  title: string;
  status: 'pending' | 'completed' | 'archived';
  createdAt: string;
}

// API client with type safety
async function getTasks(status?: string): Promise<Task[]> {
  const params = status ? `?status=${status}` : '';
  const res = await fetch(`/api/v1/tasks${params}`);
  if (!res.ok) throw new ApiError(res.status, await res.json());
  return res.json();
}
```

### 2. Error Handling Across Stack
```
Frontend: Try/catch → User-friendly message → Optional retry
    ↕
API Layer: Validate → Process → Structured error response
    ↕
Backend: Business logic → Domain exceptions → HTTP status mapping
    ↕
Database: Constraints → Unique violations → Conflict response
```

## Best Practices
1. Define API contracts before implementation
2. Use code generation for type-safe client/server communication
3. Implement optimistic UI updates with server reconciliation
4. Feature flags for gradual rollout and quick rollback
5. Monitor both frontend and backend metrics for each feature

## Common Pitfalls
- Frontend and backend developed in isolation without shared contracts
- Missing error handling at integration boundaries
- No loading/error states in the UI
- Deploying frontend changes before backend is ready
- Not testing the full flow end-to-end before merge
""",

    "git-advanced-workflows": """# Git Advanced Workflows Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Rebase vs Merge Decision
| Scenario | Use Rebase | Use Merge |
|---|---|---|
| Feature branch cleanup | ✅ | |
| Shared branch integration | | ✅ |
| Linear history preferred | ✅ | |
| Preserving branch context | | ✅ |
| Public/pushed branches | | ✅ |

### 2. Interactive Rebase Workflow
```bash
# Clean up last 5 commits before merge
git rebase -i HEAD~5

# Common actions in editor:
# pick   abc1234 Keep this commit as-is
# reword abc1234 Edit commit message
# squash abc1234 Merge into previous commit
# fixup  abc1234 Merge into previous, discard message
# drop   abc1234 Remove this commit entirely
```

### 3. Cherry-Pick Patterns
```bash
# Single commit from another branch
git cherry-pick abc1234

# Range of commits
git cherry-pick abc1234..def5678

# Cherry-pick without committing (stage only)
git cherry-pick --no-commit abc1234
```

## Recovery Techniques

### 1. Reflog — Your Safety Net
```bash
# View recent HEAD movements
git reflog --oneline -20

# Recover from bad rebase
git reset --hard HEAD@{5}

# Find a deleted branch
git reflog | grep "checkout: moving from deleted-branch"
git checkout -b recovered-branch HEAD@{N}
```

### 2. Git Bisect — Find Breaking Commit
```bash
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
# Git checks out middle commit — test it
git bisect good  # or git bisect bad
# Repeat until found
git bisect reset
```

### 3. Worktrees — Multiple Branches Simultaneously
```bash
# Create worktree for hotfix while keeping main work
git worktree add ../hotfix-branch hotfix/critical-bug
cd ../hotfix-branch
# Work on hotfix without stashing current changes
git worktree remove ../hotfix-branch  # when done
```

## Branch Cleanup Script
```bash
#!/bin/bash
# Delete merged local branches
git branch --merged main | grep -v "main\\|develop" | xargs -r git branch -d

# Prune remote tracking branches
git remote prune origin

# List stale remote branches (>30 days)
git for-each-ref --sort=-committerdate --format='%(committerdate:short) %(refname:short)' refs/remotes/origin/ | tail -20
```

## Best Practices
1. Rebase feature branches before merge for clean history
2. Never rebase shared/public branches
3. Use `git reflog` before panicking about lost work
4. Commit early and often, clean up with interactive rebase
5. Use worktrees instead of stashing for context switches

## Common Pitfalls
- Rebasing shared branches causing duplicate commits
- Force-pushing without `--force-with-lease`
- Not backing up before complex history rewrites
- Cherry-picking instead of merging (losing merge tracking)
- Ignoring reflog expiry (default 90 days)
""",

    "github-actions-templates": """# GitHub Actions Templates Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Workflow Structure
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: pip
      - run: pip install -r requirements.txt
      - run: pytest --cov
```

### 2. Matrix Build Pattern
```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.10', '3.11', '3.12']
        exclude:
          - os: macos-latest
            python-version: '3.10'
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

### 3. Reusable Workflow
```yaml
# .github/workflows/reusable-deploy.yml
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      deploy_key:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - run: echo "Deploying to ${{ inputs.environment }}"
```

## Security Patterns

### 1. Secret Management
```yaml
- name: Deploy
  env:
    API_KEY: ${{ secrets.API_KEY }}
  run: ./deploy.sh
  # Never echo secrets: echo $API_KEY ← DANGEROUS
```

### 2. Dependency Pinning
```yaml
# Pin by SHA, not tag (prevents supply chain attacks)
- uses: actions/checkout@8ade135a41bc03ea155e62e844d188df1ea18608  # v4.1.0
```

## Workflow Templates

### CI Template (Python)
```yaml
- run: |
    pip install ruff pytest
    ruff check .
    pytest --cov --cov-report=xml
- uses: codecov/codecov-action@v3
```

### Deploy Template
```yaml
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-arn: ${{ secrets.AWS_ROLE_ARN }}
- run: aws ecs update-service --force-new-deployment
```

## Workflow Checklist
- [ ] Concurrency group to prevent duplicate runs
- [ ] Dependency caching enabled (actions/cache or built-in)
- [ ] Secrets stored in GitHub Secrets, not in code
- [ ] Actions pinned by SHA, not floating tags
- [ ] Timeout set for long-running jobs
- [ ] Status badge added to README

## Best Practices
1. Use reusable workflows for common patterns
2. Cache dependencies to speed up builds
3. Use concurrency groups to cancel stale runs
4. Pin action versions to SHA for security
5. Use `GITHUB_TOKEN` with minimal permissions

## Common Pitfalls
- Caching incorrectly (stale deps, cache misses)
- Not using concurrency groups (wasted compute)
- Hardcoding values instead of using inputs/secrets
- Missing timeout-minutes (stuck workflows eat quota)
- Triggering on all branches instead of main/PRs only
""",

    "ml-engineer": """# ML Engineer Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Model Serving Architecture
```
[Client] → [API Gateway] → [Load Balancer]
                              ├── [Model Server A] (GPU)
                              ├── [Model Server B] (GPU)
                              └── [Model Server C] (GPU)
[Feature Store] → [Feature Pipeline] → [Model Servers]
[Model Registry] → [CI/CD] → [Deployment]
```

### 2. Feature Store Pattern
```python
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo/")

# Online serving (low latency)
features = store.get_online_features(
    features=["user_features:avg_purchase", "user_features:last_login_days"],
    entity_rows=[{"user_id": 123}]
).to_dict()

# Offline training (batch)
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=["user_features:avg_purchase"],
).to_df()
```

### 3. Model Optimization Techniques
```python
# Quantization (reduce model size 4x)
import torch
model_int8 = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

# ONNX export for cross-platform serving
torch.onnx.export(model, dummy_input, "model.onnx",
                   opset_version=17, dynamic_axes={"input": {0: "batch"}})
```

## Deployment Patterns

### 1. Canary Deployment
```yaml
# Gradually shift traffic to new model version
stages:
  - name: canary-5
    traffic_split: {v1: 95, v2: 5}
    duration: 1h
    success_criteria: latency_p99 < 200ms AND error_rate < 0.1%
  - name: canary-50
    traffic_split: {v1: 50, v2: 50}
    duration: 4h
  - name: full-rollout
    traffic_split: {v2: 100}
```

### 2. A/B Model Testing
```python
def route_request(user_id: str, models: dict):
    bucket = hash(user_id) % 100
    if bucket < 10:  # 10% to challenger
        return models["challenger"].predict(features)
    return models["champion"].predict(features)
```

## Production Checklist
- [ ] Model serves under latency SLA (p99)
- [ ] Graceful degradation on model failure (fallback)
- [ ] Input validation and feature bounds checking
- [ ] Prediction logging for monitoring and retraining
- [ ] Model versioning in registry with rollback capability
- [ ] GPU memory monitoring and auto-scaling configured

## Best Practices
1. Version everything: models, data, code, configs
2. Implement shadow mode before replacing production model
3. Monitor data drift and model performance continuously
4. Use feature stores for consistency between training and serving
5. Optimize inference (batching, quantization, caching)

## Common Pitfalls
- Training/serving skew from different feature pipelines
- Not monitoring prediction distribution for drift
- Loading models on every request instead of at startup
- Ignoring cold start latency for auto-scaled services
- Missing fallback behavior when model service is unavailable
""",

    "ml-pipeline-workflow": """# ML Pipeline Workflow Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Pipeline Architecture
```
[Data Ingestion] → [Validation] → [Preprocessing] → [Feature Engineering]
                                                          ↓
[Model Registry] ← [Evaluation] ← [Training] ← [Split]
                                                          ↓
                   [Monitoring] ← [Serving] ← [Deployment]
```

### 2. Pipeline Orchestration
```python
# Example with Prefect
from prefect import flow, task

@task
def extract_data(source: str) -> pd.DataFrame:
    return pd.read_parquet(source)

@task
def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    assert df.shape[0] > 100, "Insufficient data"
    assert df.isnull().sum().max() < df.shape[0] * 0.1, "Too many nulls"
    return df

@task
def train_model(df: pd.DataFrame) -> Model:
    X_train, X_test, y_train, y_test = train_test_split(...)
    model = XGBClassifier().fit(X_train, y_train)
    return model

@flow
def ml_pipeline(source: str):
    data = extract_data(source)
    validated = validate_data(data)
    model = train_model(validated)
    return model
```

### 3. Experiment Tracking
```python
import mlflow

with mlflow.start_run():
    mlflow.log_params({"learning_rate": 0.01, "n_estimators": 100})
    model.fit(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(model, "model")
```

## Data Validation Patterns

### 1. Schema Validation
```python
import pandera as pa

schema = pa.DataFrameSchema({
    "user_id": pa.Column(int, nullable=False, unique=True),
    "age": pa.Column(int, pa.Check.in_range(0, 150)),
    "email": pa.Column(str, pa.Check.str_matches(r'.+@.+')),
    "score": pa.Column(float, pa.Check.in_range(0.0, 1.0)),
})

validated_df = schema.validate(raw_df)
```

## Pipeline Checklist
- [ ] Data validation at pipeline entry point
- [ ] Experiment tracking for all training runs
- [ ] Model versioning with metadata
- [ ] Automated evaluation against baseline
- [ ] Reproducible pipeline (pinned deps, seeds)
- [ ] Alerting on pipeline failures

## Best Practices
1. Validate data at every pipeline boundary
2. Use experiment tracking for all training runs
3. Automate the full pipeline, not just training
4. Pin random seeds for reproducibility
5. Implement automated retraining triggers

## Common Pitfalls
- Manual steps between pipeline stages
- No data validation leading to silent failures
- Training without experiment tracking
- Not comparing new models against production baseline
- Forgetting to log preprocessing parameters
""",

    "mlops-engineer": """# MLOps Engineer Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. MLOps Maturity Levels
| Level | Description | Practices |
|---|---|---|
| 0 | Manual | Jupyter notebooks, manual deployment |
| 1 | ML Pipeline | Automated training, basic monitoring |
| 2 | CI/CD | Automated testing, model validation gates |
| 3 | Full MLOps | Auto-retraining, drift detection, A/B testing |

### 2. CI/CD for ML
```yaml
# .github/workflows/ml-pipeline.yml
on:
  push:
    paths: ['models/**', 'features/**']

jobs:
  train-and-validate:
    steps:
      - run: dvc pull  # Pull training data
      - run: python train.py
      - run: python evaluate.py --threshold 0.85
      - run: python register_model.py --if-better
```

### 3. Model Monitoring
```python
from evidently import ColumnMapping, Report
from evidently.metrics import DataDriftTable, ClassificationQualityMetric

report = Report(metrics=[
    DataDriftTable(),
    ClassificationQualityMetric(),
])
report.run(reference_data=train_df, current_data=prod_df,
           column_mapping=ColumnMapping(target="label"))
report.save_html("monitoring_report.html")
```

## Infrastructure Patterns

### 1. Training Infrastructure
```yaml
# Kubernetes training job
apiVersion: batch/v1
kind: Job
metadata:
  name: model-training
spec:
  template:
    spec:
      containers:
        - name: trainer
          image: ml-pipeline:latest
          resources:
            limits:
              nvidia.com/gpu: 1
              memory: 16Gi
```

### 2. Serving Infrastructure
```python
# FastAPI model server with health checks
@app.get("/health")
async def health():
    return {"status": "healthy", "model_version": MODEL_VERSION}

@app.post("/predict")
async def predict(request: PredictRequest):
    features = preprocess(request.data)
    prediction = model.predict(features)
    log_prediction(request, prediction)  # For monitoring
    return {"prediction": prediction.tolist()}
```

## MLOps Checklist
- [ ] Version control for code, data (DVC), and models
- [ ] Automated training pipeline with data validation
- [ ] Model evaluation gates before promotion
- [ ] Automated deployment with rollback capability
- [ ] Production monitoring (drift, performance, latency)
- [ ] Alerting on model degradation

## Best Practices
1. Treat ML pipelines as software — test, version, review
2. Implement data versioning alongside code versioning
3. Use model registries with promotion stages (dev → staging → prod)
4. Monitor both data drift and model performance
5. Automate retraining but require human approval for deployment

## Common Pitfalls
- Deploying models without validation gates
- No rollback mechanism for bad model versions
- Monitoring only accuracy, not input data distribution
- Manual feature engineering not captured in pipeline
- Training on stale data without freshness checks
""",

    "prometheus-configuration": """# Prometheus Configuration Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Metric Types
| Type | Description | Example |
|---|---|---|
| Counter | Monotonically increasing | `http_requests_total` |
| Gauge | Can go up and down | `temperature_celsius` |
| Histogram | Distribution of values | `http_request_duration_seconds` |
| Summary | Similar to histogram, client-side quantiles | `rpc_duration_seconds` |

### 2. Naming Conventions
```
# Format: <namespace>_<subsystem>_<name>_<unit>
http_server_requests_total           # Counter
http_server_request_duration_seconds # Histogram
node_memory_usage_bytes              # Gauge
```

### 3. Basic Configuration
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "rules/*.yml"

scrape_configs:
  - job_name: 'app'
    static_targets: ['localhost:8080']
    metrics_path: /metrics
    scrape_interval: 10s
```

## Scrape Configuration Patterns

### 1. Service Discovery
```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
```

### 2. Recording Rules
```yaml
# rules/app-rules.yml
groups:
  - name: app_rules
    rules:
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
      - record: job:http_request_duration:p99
        expr: histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, job))
```

### 3. Alerting Rules
```yaml
groups:
  - name: app_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
```

## PromQL Cheat Sheet
```
# Request rate
rate(http_requests_total[5m])

# Error percentage
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# 99th percentile latency
histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))

# Top 5 memory consumers
topk(5, container_memory_usage_bytes)
```

## Configuration Checklist
- [ ] Scrape interval appropriate for metric cardinality
- [ ] Recording rules for frequently-used aggregations
- [ ] Alert rules for SLO breaches
- [ ] Retention period configured for storage capacity
- [ ] Federation set up for multi-cluster monitoring
- [ ] Grafana dashboards connected

## Best Practices
1. Use recording rules for expensive queries
2. Keep label cardinality under control (no user IDs as labels)
3. Set appropriate scrape intervals (15s default, adjust per target)
4. Use histograms over summaries for aggregatable percentiles
5. Implement alerting on SLOs, not raw metrics

## Common Pitfalls
- High cardinality labels causing memory explosion
- Missing `rate()` on counters (raw counter values are useless)
- Alerting on instantaneous values instead of trends
- No recording rules for dashboard queries (slow dashboards)
- Scraping too frequently for high-cardinality endpoints
""",

    "spark-optimization": """# Spark Optimization Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Shuffle Optimization
```python
# Bad: Unnecessary shuffle from repartition
df.repartition(200).groupBy("key").count()

# Good: Use coalesce to reduce partitions without full shuffle
df.coalesce(50).write.parquet("output/")

# Good: Pre-partition by join key
df1 = df1.repartition("join_key")
df2 = df2.repartition("join_key")
result = df1.join(df2, "join_key")
```

### 2. Partition Sizing
```
Target partition size: 128MB - 256MB
Formula: num_partitions = total_data_size / target_partition_size

# Example: 100GB dataset
num_partitions = 100GB / 200MB = 500 partitions
spark.conf.set("spark.sql.shuffle.partitions", 500)
```

### 3. Caching Strategy
```python
from pyspark.storagelevel import StorageLevel

# Cache frequently accessed DataFrame
df_cached = df.persist(StorageLevel.MEMORY_AND_DISK)
df_cached.count()  # Trigger materialization

# Unpersist when done
df_cached.unpersist()

# Decision tree:
# Used 2+ times? → Cache
# Fits in memory? → MEMORY_ONLY
# Doesn't fit? → MEMORY_AND_DISK
# Serialization needed? → MEMORY_ONLY_SER
```

## Performance Patterns

### 1. Broadcast Join
```python
from pyspark.sql.functions import broadcast

# Small table (<10MB) joined with large table
result = large_df.join(broadcast(small_df), "key")
# Avoids shuffle of large table
```

### 2. Predicate Pushdown
```python
# Good: Filter early, push predicates to source
df = spark.read.parquet("data/").filter("date >= '2024-01-01'")

# Bad: Read all data then filter
df = spark.read.parquet("data/")
df = df.filter("date >= '2024-01-01'")
# Note: Spark optimizer may handle this, but explicit is safer with complex queries
```

### 3. Skew Handling
```python
# Salt the skewed key
from pyspark.sql.functions import lit, rand, concat

salt_factor = 10
df_salted = df.withColumn("salted_key",
    concat("skewed_key", lit("_"), (rand() * salt_factor).cast("int")))
```

## Configuration Cheat Sheet
```python
spark.conf.set("spark.sql.shuffle.partitions", "auto")  # Spark 3.0+ AQE
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

## Optimization Checklist
- [ ] Adaptive Query Execution (AQE) enabled
- [ ] Partition count matches data volume
- [ ] Broadcast joins for small dimension tables
- [ ] No unnecessary shuffles (check query plan)
- [ ] Data skew handled (salting or AQE skew join)
- [ ] Caching used for repeated computations

## Best Practices
1. Enable AQE for automatic partition coalescing and skew handling
2. Use columnar formats (Parquet/ORC) with predicate pushdown
3. Broadcast small tables to avoid shuffle joins
4. Monitor Spark UI for stage-level bottlenecks
5. Right-size executors: 4-5 cores, 4-8GB memory per executor

## Common Pitfalls
- Using `collect()` on large DataFrames (OOM on driver)
- Too many or too few partitions (overhead vs underutilization)
- Not using broadcast for small dimension tables
- Ignoring data skew causing straggler tasks
- UDFs instead of built-in functions (no Catalyst optimization)
""",

    "temporal-python-pro": """# Temporal Python SDK Implementation Playbook

This file contains detailed patterns, checklists, and code samples referenced by the skill.

## Core Concepts

### 1. Workflow Fundamentals
```python
from temporalio import workflow
from datetime import timedelta

@workflow.defn
class OrderWorkflow:
    @workflow.run
    async def run(self, order: Order) -> OrderResult:
        # Activities are the only way to do I/O
        payment = await workflow.execute_activity(
            process_payment, order.payment,
            start_to_close_timeout=timedelta(seconds=30),
        )
        if not payment.success:
            return OrderResult(status="payment_failed")

        shipment = await workflow.execute_activity(
            create_shipment, order.items,
            start_to_close_timeout=timedelta(minutes=5),
            retry_policy=RetryPolicy(maximum_attempts=3),
        )
        return OrderResult(status="completed", tracking=shipment.tracking_id)
```

### 2. Activity Patterns
```python
from temporalio import activity

@activity.defn
async def process_payment(payment: PaymentInfo) -> PaymentResult:
    # Activities can do I/O, call external services, etc.
    result = await payment_gateway.charge(payment)
    return PaymentResult(success=result.ok, transaction_id=result.id)

@activity.defn
async def send_notification(user_id: str, message: str) -> None:
    activity.heartbeat()  # For long-running activities
    await notification_service.send(user_id, message)
```

### 3. Worker Setup
```python
from temporalio.client import Client
from temporalio.worker import Worker

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="order-processing",
        workflows=[OrderWorkflow],
        activities=[process_payment, create_shipment, send_notification],
    )
    await worker.run()
```

## Advanced Patterns

### 1. Saga Pattern (Compensating Transactions)
```python
@workflow.defn
class SagaWorkflow:
    @workflow.run
    async def run(self, data):
        compensations = []
        try:
            result_a = await workflow.execute_activity(step_a, data)
            compensations.append(("compensate_a", result_a))

            result_b = await workflow.execute_activity(step_b, result_a)
            compensations.append(("compensate_b", result_b))
        except Exception:
            # Reverse compensations
            for comp_name, comp_data in reversed(compensations):
                await workflow.execute_activity(comp_name, comp_data)
            raise
```

### 2. Signals and Queries
```python
@workflow.defn
class ApprovalWorkflow:
    def __init__(self):
        self.approved = False

    @workflow.signal
    async def approve(self):
        self.approved = True

    @workflow.query
    def get_status(self) -> str:
        return "approved" if self.approved else "pending"

    @workflow.run
    async def run(self):
        await workflow.wait_condition(lambda: self.approved)
        return "Workflow completed after approval"
```

## Production Checklist
- [ ] Retry policies configured for all activities
- [ ] Heartbeats implemented for long-running activities
- [ ] Timeouts set for workflows and activities
- [ ] Worker scaled appropriately for task throughput
- [ ] Dead letter queue monitoring configured
- [ ] Workflow versioning strategy implemented

## Best Practices
1. Keep workflows deterministic — no I/O, randomness, or system time
2. Use activities for all side effects and external calls
3. Set appropriate timeouts (start-to-close, schedule-to-close)
4. Implement heartbeats for activities longer than 30 seconds
5. Use signals for external events, queries for state inspection

## Common Pitfalls
- Performing I/O directly in workflows (non-deterministic)
- Not setting retry policies (infinite retries by default)
- Missing heartbeats on long activities (timeout without retry)
- Large payloads in workflow state (use references/IDs instead)
- Not using workflow versioning for live updates
""",
}


def main():
    created = 0
    for skill_name, content in PLAYBOOKS.items():
        resources_dir = os.path.join(SKILLS_ROOT, skill_name, 'resources')
        os.makedirs(resources_dir, exist_ok=True)
        filepath = os.path.join(resources_dir, 'implementation-playbook.md')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        created += 1
        print(f"Created: {skill_name}/resources/implementation-playbook.md")
    print(f"\nTotal created: {created}")


if __name__ == "__main__":
    main()
