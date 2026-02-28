# Prometheus Scrape Configuration Reference

## Static Targets

```yaml
scrape_configs:
  - job_name: "my-service"
    static_configs:
      - targets: ["host1:9090", "host2:9090"]
        labels:
          env: production
```

## Service Discovery

### Kubernetes
```yaml
- job_name: "k8s-pods"
  kubernetes_sd_configs:
    - role: pod
  relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      target_label: __address__
```

### Consul
```yaml
- job_name: "consul-services"
  consul_sd_configs:
    - server: "consul:8500"
      services: ["web", "api"]
```

### File-Based
```yaml
- job_name: "file-targets"
  file_sd_configs:
    - files: ["targets/*.json"]
      refresh_interval: 30s
```

## Common Relabel Configs

### Keep/Drop by Label
```yaml
relabel_configs:
  - source_labels: [__meta_kubernetes_namespace]
    action: keep
    regex: "production|staging"
```

### Add Custom Labels
```yaml
relabel_configs:
  - target_label: team
    replacement: platform
```

### Override Metrics Path
```yaml
relabel_configs:
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
    action: replace
    target_label: __metrics_path__
    regex: (.+)
```
