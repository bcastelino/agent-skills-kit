# Rollback Strategies

Proven patterns for safely reverting database migrations.

## Immediate Rollback

### Pre-Migration Snapshot
```bash
# PostgreSQL
pg_dump -Fc production_db > pre_migration_backup.dump

# Restore if needed
pg_restore -d production_db pre_migration_backup.dump
```

## Reversible Migrations

### Alembic Downgrade
```python
def downgrade():
    op.drop_column("users", "new_column")
    op.rename_table("new_table", "old_table")
```

### Django Reverse Migration
```bash
python manage.py migrate app_name 0005_previous_migration
```

## Blue-Green Database Pattern

1. Maintain two database instances (blue = current, green = new)
2. Apply migration to green
3. Test thoroughly on green
4. Switch traffic to green
5. Keep blue as rollback target for 24-48 hours

## Rollback Decision Framework

| Scenario | Action | Timeframe |
|----------|--------|-----------|
| Migration fails mid-execution | Auto-rollback from transaction | Immediate |
| Data corruption detected | Restore from pre-migration backup | Minutes-Hours |
| Performance degradation | Revert schema changes | Minutes |
| Subtle data issues found later | Fix-forward preferred | Hours-Days |

## Key Principles
- Always take backups before migrations
- Test rollback procedures in staging
- Set clear rollback triggers and timeframes
- Document rollback steps in migration plan
