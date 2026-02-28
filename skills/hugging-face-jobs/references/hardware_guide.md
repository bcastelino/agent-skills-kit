# Hugging Face Jobs Hardware Guide

## Available Hardware Flavors

### CPU
| Flavor | vCPUs | RAM | Use Case |
|--------|-------|-----|----------|
| `cpu-basic` | 2 | 16 GB | Data processing, light tasks |
| `cpu-upgrade` | 8 | 32 GB | Heavy data processing, Polars |

### GPU
| Flavor | GPU | VRAM | Use Case |
|--------|-----|------|----------|
| `t4-small` | 1x T4 | 16 GB | <1B models, quick tests |
| `t4-medium` | 1x T4 | 16 GB | Small models, more CPU/RAM |
| `l4x1` | 1x L4 | 24 GB | 1-7B models |
| `l4x4` | 4x L4 | 96 GB | Multi-GPU, large models |
| `a10g-small` | 1x A10G | 24 GB | 7B models, fine-tuning |
| `a10g-large` | 1x A10G | 24 GB | 7-13B models, more RAM |
| `a10g-largex2` | 2x A10G | 48 GB | Large model inference |
| `a10g-largex4` | 4x A10G | 96 GB | Very large models |
| `a100-large` | 1x A100 | 80 GB | 13B+ models, training |

### TPU
| Flavor | Config | Use Case |
|--------|--------|----------|
| `v5e-1x1` | 1 chip | JAX/Flax workloads |
| `v5e-2x2` | 4 chips | Medium TPU workloads |
| `v5e-2x4` | 8 chips | Large TPU workloads |

## Cost Estimation

| Flavor | Approx Cost/Hour |
|--------|-------------------|
| `cpu-basic` | ~$0.10 |
| `cpu-upgrade` | ~$0.30 |
| `t4-small` | ~$0.60 |
| `l4x1` | ~$2.50 |
| `a10g-small` | ~$2.00 |
| `a10g-large` | ~$5.00 |
| `a100-large` | ~$10.00 |

**Formula**: `Total Cost = Hours x Cost/hr`

## Selection Guidelines

1. **Start small, scale up**: Begin with `cpu-basic` or `t4-small`
2. **Match VRAM to model size**: 7B model needs ~14GB VRAM minimum
3. **Multi-GPU for parallel**: Use `l4x4` or `a10g-largex4` for data parallelism
4. **TPUs for JAX/Flax**: Only use TPU flavors with JAX-based code
5. **CPU for data processing**: Polars, pandas, data wrangling don't need GPU
