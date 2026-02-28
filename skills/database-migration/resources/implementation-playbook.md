# Database Migration Implementation Playbook

Detailed patterns, scripts, and strategies for zero-downtime database migrations.

## ORM Migration Patterns

### SQLAlchemy/Alembic
```python
# alembic/versions/001_add_users_table.py
def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(255), unique=True, nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index("ix_users_email", "users", ["email"])

def downgrade():
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
```

### Django Migrations
```python
class Migration(migrations.Migration):
    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True)),
                ("email", models.EmailField(unique=True)),
            ],
        ),
    ]
```

## Zero-Downtime Strategies

### Expand-Contract Pattern
1. **Expand**: Add new column/table alongside old
2. **Migrate**: Backfill data, dual-write to both
3. **Contract**: Remove old column/table after verification

### Column Rename (Safe)
```sql
-- Step 1: Add new column
ALTER TABLE users ADD COLUMN full_name VARCHAR(255);

-- Step 2: Backfill (batched)
UPDATE users SET full_name = name WHERE full_name IS NULL LIMIT 1000;

-- Step 3: Dual-write in application
-- Step 4: Switch reads to new column
-- Step 5: Drop old column (after verification period)
ALTER TABLE users DROP COLUMN name;
```

## Data Transformation

### Batch Processing
```python
BATCH_SIZE = 1000

def migrate_data_batch(offset):
    rows = db.execute(
        f"SELECT * FROM old_table LIMIT {BATCH_SIZE} OFFSET {offset}"
    )
    for row in rows:
        transformed = transform(row)
        db.execute("INSERT INTO new_table ...", transformed)
    return len(rows)
```

## Rollback Strategies

### Pre-Migration Checklist
- [ ] Full database backup verified
- [ ] Rollback script tested
- [ ] Monitoring alerts configured
- [ ] Communication plan ready
- [ ] Maintenance window scheduled (if needed)

### Rollback Decision Tree
1. Migration fails immediately -> Automatic rollback
2. Data inconsistency detected -> Pause, assess, manual rollback
3. Performance degradation -> Monitor, rollback if SLA breached
4. Success with minor issues -> Fix forward
