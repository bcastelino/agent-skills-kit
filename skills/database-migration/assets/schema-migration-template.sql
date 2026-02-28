-- Schema Migration Template
-- Migration: [DESCRIPTION]
-- Date: [DATE]
-- Author: [AUTHOR]

-- ============================================================
-- PRE-MIGRATION CHECKS
-- ============================================================
-- Verify current schema state
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'TARGET_TABLE';

-- ============================================================
-- FORWARD MIGRATION
-- ============================================================
BEGIN;

-- Step 1: Add new structures
-- ALTER TABLE target_table ADD COLUMN new_col TYPE;

-- Step 2: Backfill data (if needed)
-- UPDATE target_table SET new_col = transform(old_col);

-- Step 3: Add constraints
-- ALTER TABLE target_table ALTER COLUMN new_col SET NOT NULL;
-- CREATE INDEX CONCURRENTLY idx_name ON target_table(new_col);

COMMIT;

-- ============================================================
-- VERIFICATION
-- ============================================================
-- Verify migration success
-- SELECT COUNT(*) FROM target_table WHERE new_col IS NULL;

-- ============================================================
-- ROLLBACK (if needed)
-- ============================================================
-- BEGIN;
-- ALTER TABLE target_table DROP COLUMN new_col;
-- COMMIT;
