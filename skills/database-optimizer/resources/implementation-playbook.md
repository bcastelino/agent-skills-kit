# Database Optimizer Implementation Playbook

Detailed patterns, queries, and strategies for database performance tuning.

## Query Analysis

### EXPLAIN Plan Reading
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE u.created_at > '2024-01-01'
GROUP BY u.name
HAVING COUNT(o.id) > 5;
```

### Key Metrics to Watch
| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Query time | < 100ms | 100ms-1s | > 1s |
| Rows scanned | ~rows returned | 10x returned | 100x returned |
| Buffer hits | > 99% | 95-99% | < 95% |
| Lock waits | 0 | < 5/min | > 5/min |

## Indexing Strategies

### Index Selection Rules
1. Index columns in WHERE, JOIN, and ORDER BY clauses
2. Use composite indexes matching query patterns
3. Consider covering indexes for frequent queries
4. Avoid over-indexing (slows writes)
5. Monitor index usage and remove unused ones

### Common Patterns
```sql
-- Composite index for common query pattern
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

-- Partial index for active records only
CREATE INDEX idx_active_users ON users(email) WHERE active = true;

-- Covering index to avoid table lookup
CREATE INDEX idx_orders_covering ON orders(user_id, status, total);
```

## Connection Management

### Connection Pool Configuration
```python
engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,
)
```

## Slow Query Investigation

### Diagnostic Queries (PostgreSQL)
```sql
-- Find slow queries
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 20;

-- Find missing indexes
SELECT relname, seq_scan, idx_scan,
       ROUND(100.0 * idx_scan / (seq_scan + idx_scan), 1) AS idx_ratio
FROM pg_stat_user_tables
WHERE seq_scan + idx_scan > 100
ORDER BY seq_scan DESC;

-- Find unused indexes
SELECT indexrelname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND indexrelname NOT LIKE 'pg_%';
```
