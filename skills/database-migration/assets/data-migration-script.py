#!/usr/bin/env python3
"""Data migration script template.

Usage:
    python data-migration-script.py --source SOURCE_DB --target TARGET_DB [--batch-size 1000] [--dry-run]
"""
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Data migration script")
    parser.add_argument("--source", required=True, help="Source database URL")
    parser.add_argument("--target", required=True, help="Target database URL")
    parser.add_argument("--batch-size", type=int, default=1000, help="Batch size")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    return parser.parse_args()


def migrate_batch(source_conn, target_conn, offset, batch_size, dry_run=False):
    """Migrate a single batch of rows."""
    # TODO: Customize query for your migration
    rows = source_conn.execute(
        f"SELECT * FROM source_table ORDER BY id LIMIT {batch_size} OFFSET {offset}"
    ).fetchall()

    if not rows:
        return 0

    for row in rows:
        transformed = transform_row(row)
        if not dry_run:
            target_conn.execute(
                "INSERT INTO target_table (...) VALUES (...)", transformed
            )

    if not dry_run:
        target_conn.commit()

    return len(rows)


def transform_row(row):
    """Transform a source row to target format."""
    # TODO: Implement transformation logic
    return row


def main():
    args = parse_args()
    print(f"Migrating from {args.source} to {args.target}")
    print(f"Batch size: {args.batch_size}, Dry run: {args.dry_run}")

    # TODO: Set up database connections
    # source_conn = connect(args.source)
    # target_conn = connect(args.target)

    offset = 0
    total = 0
    while True:
        count = migrate_batch(None, None, offset, args.batch_size, args.dry_run)
        if count == 0:
            break
        total += count
        offset += args.batch_size
        print(f"Processed {total} rows...")

    print(f"Migration complete. Total rows: {total}")


if __name__ == "__main__":
    main()
