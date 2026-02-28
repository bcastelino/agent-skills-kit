# Prometheus Configuration Implementation Playbook

Detailed configuration patterns, templates, and examples for Prometheus monitoring.

## Base Configuration Template

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  scrape_timeout: 10s

rule_files:
  - "rules/*.yml"

alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
  - job_name: "node"
    static_configs:
      - targets: ["node-exporter:9100"]
```

## Scrape Configuration Patterns

### Kubernetes Service Discovery
```yaml
- job_name: "kubernetes-pods"
  kubernetes_sd_configs:
    - role: pod
  relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      target_label: __address__
      regex: (.+)
```

### Application Metrics
```yaml
- job_name: "fastapi-app"
  metrics_path: "/metrics"
  static_configs:
    - targets: ["app:8000"]
  scrape_interval: 10s
```

## Recording Rules

```yaml
groups:
  - name: http_rules
    interval: 30s
    rules:
      - record: job:http_requests_total:rate5m
        expr: rate(http_requests_total[5m])
      - record: job:http_request_duration:p99
        expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
      - record: job:http_error_rate:ratio
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])
```

## Alert Rules

```yaml
groups:
  - name: availability
    rules:
      - alert: HighErrorRate
        expr: job:http_error_rate:ratio > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
      - alert: HighLatency
        expr: job:http_request_duration:p99 > 1
        for: 10m
        labels:
          severity: warning
```

## Validation Script

```bash
#!/bin/bash
set -euo pipefail
echo "Validating Prometheus configuration..."
promtool check config prometheus.yml
echo "Validating rules..."
for f in rules/*.yml; do
  promtool check rules "$f"
done
echo "All validations passed."
```
