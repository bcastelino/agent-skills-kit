# ORM Switching Guide

Patterns for migrating between ORMs while maintaining data integrity.

## SQLAlchemy to Django ORM

### Key Differences
| Feature | SQLAlchemy | Django ORM |
|---------|------------|------------|
| Schema definition | Declarative Base | models.Model |
| Queries | session.query() | Model.objects |
| Relationships | relationship() | ForeignKey() |
| Migrations | Alembic | django-admin migrate |

### Migration Steps
1. Map SQLAlchemy models to Django models
2. Generate Django migrations from existing schema
3. Verify migration matches production schema
4. Update query layer incrementally
5. Run parallel reads during transition

## Django ORM to SQLAlchemy

### Steps
1. Generate SQLAlchemy models from database introspection
2. Create Alembic baseline migration
3. Verify model mapping completeness
4. Migrate query layer with unit tests
5. Switch session management

## Prisma to SQLAlchemy

### Considerations
- Prisma schema is declarative; map to SQLAlchemy declarative models
- Handle Prisma-specific features (@@unique, @@index)
- Migrate client calls to session-based queries
