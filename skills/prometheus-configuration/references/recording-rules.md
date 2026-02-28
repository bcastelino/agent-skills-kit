# Prometheus Recording Rules Reference

Recording rules precompute frequently needed or expensive expressions.

## Syntax

```yaml
groups:
  - name: group_name
    interval: 30s  # Optional, overrides global
    rules:
      - record: metric_name
        expr: PromQL_expression
        labels:
          extra_label: value
```

## HTTP Metrics

```yaml
groups:
  - name: http_rules
    rules:
      # Request rate per second
      - record: job:http_requests:rate5m
        expr: rate(http_requests_total[5m])

      # Error rate ratio
      - record: job:http_errors:ratio5m
        expr: >
          rate(http_requests_total{status=~"5.."}[5m])
          / rate(http_requests_total[5m])

      # P99 latency
      - record: job:http_duration:p99
        expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

      # P50 latency
      - record: job:http_duration:p50
        expr: histogram_quantile(0.50, rate(http_request_duration_seconds_bucket[5m]))
```

## Resource Metrics

```yaml
groups:
  - name: resource_rules
    rules:
      # CPU usage percentage
      - record: instance:cpu_usage:percent
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

      # Memory usage percentage
      - record: instance:memory_usage:percent
        expr: (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

      # Disk usage percentage
      - record: instance:disk_usage:percent
        expr: (1 - node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100
```

## Best Practices

1. **Naming convention**: `level:metric:operations` (e.g., `job:http_requests:rate5m`)
2. **Pre-compute dashboards**: Record rules for frequently viewed metrics
3. **Keep rules simple**: One meaningful computation per rule
4. **Match alert expressions**: Record rules should match what alerts use
