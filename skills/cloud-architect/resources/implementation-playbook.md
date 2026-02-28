# Cloud Architect Implementation Playbook

Detailed patterns, templates, and decision frameworks for multi-cloud infrastructure design.

## Architecture Decision Framework

### Cloud Provider Selection
| Factor | AWS | Azure | GCP |
|--------|-----|-------|-----|
| Compute | EC2, Lambda, ECS | VMs, Functions, AKS | GCE, Cloud Run, GKE |
| Database | RDS, DynamoDB | SQL DB, Cosmos DB | Cloud SQL, Firestore |
| AI/ML | SageMaker, Bedrock | Azure AI, OpenAI | Vertex AI, Gemini |
| Pricing | Pay-as-you-go | Enterprise agreements | Sustained discounts |

### Well-Architected Pillars
1. **Operational Excellence**: Automate operations, respond to events
2. **Security**: Protect data and systems, manage identities
3. **Reliability**: Recover from failures, meet availability targets
4. **Performance**: Use resources efficiently, monitor performance
5. **Cost Optimization**: Manage spending, right-size resources
6. **Sustainability**: Minimize environmental impact

## Infrastructure as Code

### Terraform Patterns
```hcl
module "vpc" {
  source  = "./modules/vpc"
  cidr    = var.vpc_cidr
  azs     = var.availability_zones
  tags    = local.common_tags
}

module "eks" {
  source       = "./modules/eks"
  vpc_id       = module.vpc.vpc_id
  subnet_ids   = module.vpc.private_subnet_ids
  cluster_name = var.cluster_name
}
```

### State Management
- Use remote state (S3, GCS, Azure Blob)
- Enable state locking (DynamoDB, GCS)
- Separate state per environment
- Use workspaces for environment isolation

## High Availability Patterns

### Multi-AZ Deployment
- Deploy across minimum 3 availability zones
- Use load balancers for traffic distribution
- Implement health checks and auto-scaling
- Design for graceful degradation

### Disaster Recovery Strategies
| Strategy | RPO | RTO | Cost |
|----------|-----|-----|------|
| Backup & Restore | Hours | Hours | Low |
| Pilot Light | Minutes | Minutes | Medium |
| Warm Standby | Seconds | Minutes | High |
| Active-Active | Zero | Zero | Highest |

## Cost Optimization

### FinOps Practices
- Tag all resources for cost allocation
- Use reserved instances for steady-state workloads
- Implement auto-scaling for variable workloads
- Review unused resources monthly
- Set up billing alerts and budgets
