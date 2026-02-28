# Data-Driven Feature Implementation Playbook

Detailed patterns for building features guided by data insights, A/B testing, and measurement.

## Phase 1: Data Analysis

### Hypothesis Formation
```markdown
Template:
- Observation: [What data shows]
- Hypothesis: If we [change], then [metric] will [improve] by [amount]
- Test: [How to validate]
- Success Criteria: [Measurable threshold]
```

### Instrumentation Patterns
```python
def track_event(event_name, properties, user_id):
    event = {
        "event": event_name,
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat(),
        "properties": properties,
    }
    analytics_queue.send(event)

def is_feature_enabled(feature_key, user_id):
    return feature_flags.evaluate(feature_key, user_id)
```

## Phase 2: Experiment Design

### A/B Test Setup
1. Define control and treatment groups
2. Calculate sample size for statistical power
3. Set experiment duration
4. Define primary and guardrail metrics
5. Plan analysis methodology

### Metric Hierarchy
- **North Star**: Core business metric (e.g., revenue, engagement)
- **Primary**: Direct feature impact metrics
- **Secondary**: Supporting behavioral metrics
- **Guardrail**: Metrics that must not degrade

## Phase 3: Implementation

### Feature Flag Patterns
```python
if feature_flags.percentage_rollout("new-checkout", user_id, percentage=10):
    return new_checkout_flow(request)
return existing_checkout_flow(request)
```

### Data Pipeline Integration
- Log all feature interactions
- Track conversion funnels
- Monitor error rates per variant
- Capture latency metrics

## Phase 4: Analysis and Iteration

### Statistical Analysis
- Check for statistical significance (p < 0.05)
- Calculate confidence intervals
- Look for segments with different effects
- Validate no metric degradation in guardrails
- Document findings and next steps
