# Embedding Strategies Implementation Playbook

Detailed patterns and examples for selecting and optimizing embedding models.

## Model Selection Guide

### Comparison Matrix
| Model | Dimensions | Speed | Quality | Cost |
|-------|-----------|-------|---------|------|
| text-embedding-3-large | 3072 | Fast | Excellent | Medium |
| text-embedding-3-small | 1536 | Very Fast | Good | Low |
| Cohere embed-v3 | 1024 | Fast | Excellent | Medium |
| BGE-large-en-v1.5 | 1024 | Medium | Very Good | Free |
| all-MiniLM-L6-v2 | 384 | Very Fast | Good | Free |

### Selection Decision Tree
1. Need highest quality? -> text-embedding-3-large or Cohere embed-v3
2. Cost constrained? -> Open-source (BGE, MiniLM)
3. Low latency critical? -> text-embedding-3-small or MiniLM
4. Domain-specific? -> Fine-tune BGE or train custom model

## Chunking Strategies

### By Document Type
| Document Type | Strategy | Chunk Size | Overlap |
|--------------|----------|-----------|---------|
| Technical docs | Heading-based | 500-1000 tokens | 50 tokens |
| Legal text | Paragraph-based | 300-500 tokens | 100 tokens |
| Code | Function/class-based | Varies | Full context |
| Conversations | Message-based | 5-10 messages | 2 messages |

### Implementation
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""],
    length_function=len,
)

chunks = splitter.split_text(document_text)
```

## Optimization Techniques

### Dimensionality Reduction
```python
# Matryoshka embeddings (OpenAI text-embedding-3)
response = client.embeddings.create(
    model="text-embedding-3-large",
    input=text,
    dimensions=512,  # Reduce from 3072 to 512
)
```

### Batch Processing
```python
BATCH_SIZE = 100
embeddings = []
for i in range(0, len(texts), BATCH_SIZE):
    batch = texts[i:i + BATCH_SIZE]
    response = client.embeddings.create(model=MODEL, input=batch)
    embeddings.extend([e.embedding for e in response.data])
```

## Evaluation

### Retrieval Quality Metrics
- **Recall@K**: Fraction of relevant docs in top K results
- **MRR**: Mean reciprocal rank of first relevant result
- **NDCG**: Normalized discounted cumulative gain
- **Hit Rate**: Percentage of queries with at least one relevant result
