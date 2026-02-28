# Schema Migration Patterns

Safe patterns for evolving database schemas in production.

## Adding Columns

### Non-Nullable Column (Safe)
```sql
-- Step 1: Add as nullable
ALTER TABLE users ADD COLUMN status VARCHAR(20);

-- Step 2: Backfill default values
UPDATE users SET status = 'active' WHERE status IS NULL;

-- Step 3: Add NOT NULL constraint
ALTER TABLE users ALTER COLUMN status SET NOT NULL;
```

## Renaming Tables

### Safe Rename Pattern
1. Create new table with desired name
2. Set up triggers to dual-write
3. Backfill data from old to new
4. Switch application reads to new table
5. Drop triggers and old table

## Adding Indexes

### Online Index Creation
```sql
-- PostgreSQL: concurrent index (no lock)
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- MySQL: Online DDL
ALTER TABLE users ADD INDEX idx_email (email), ALGORITHM=INPLACE, LOCK=NONE;
```

## Splitting Tables

### Vertical Split
1. Create new table with subset of columns + foreign key
2. Backfill data
3. Update application to join or read from new table
4. Remove moved columns from original table
