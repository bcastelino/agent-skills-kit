# Data Transformation Patterns

Techniques for transforming data during migrations.

## Batch Processing

### Chunked Updates
```python
BATCH_SIZE = 5000
offset = 0

while True:
    rows = db.execute(
        f"SELECT id FROM source_table ORDER BY id LIMIT {BATCH_SIZE} OFFSET {offset}"
    ).fetchall()
    if not rows:
        break
    ids = [r[0] for r in rows]
    db.execute(
        "UPDATE target_table SET new_col = transform(old_col) WHERE id IN :ids",
        {"ids": tuple(ids)},
    )
    db.commit()
    offset += BATCH_SIZE
    print(f"Processed {offset} rows")
```

## Type Conversions

### Common Patterns
| From | To | Strategy |
|------|----|----------|
| VARCHAR -> INT | Cast with validation | Add new column, backfill, swap |
| INT -> ENUM | Map values | Create enum type, add column, backfill |
| TEXT -> JSON | Parse and validate | Add JSONB column, backfill with parsing |
| DATETIME -> TIMESTAMPTZ | Convert timezone | Add new column, backfill with TZ conversion |

## Data Enrichment

### Adding Computed Columns
```sql
-- Add full_name from first_name + last_name
ALTER TABLE users ADD COLUMN full_name VARCHAR(510);
UPDATE users SET full_name = first_name || ' ' || last_name;
```
