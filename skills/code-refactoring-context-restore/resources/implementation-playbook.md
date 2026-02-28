# Code Refactoring Context Restore Implementation Playbook

Detailed patterns and strategies for restoring and maintaining project context during code refactoring sessions.

## Context Recovery Strategies

### File-Based Context Discovery
```bash
# Find recently modified files
git log --oneline --since="2 weeks ago" --name-only | sort -u

# Find related files by import/dependency
grep -r "import.*ModuleName" --include="*.py" -l

# Find test files for a module
find . -name "test_*.py" -exec grep -l "ModuleName" {} \;
```

### Architecture Recovery
1. **Identify entry points**: main files, API routes, event handlers
2. **Trace data flow**: follow imports and function calls
3. **Map dependencies**: build module dependency graph
4. **Identify patterns**: recognize design patterns in use
5. **Document findings**: create architecture decision records

## Refactoring Session Management

### Before Starting
- Document current state and intent
- Create a branch with descriptive name
- Run existing tests to establish baseline
- Identify affected modules and dependencies

### During Refactoring
- Make small, incremental changes
- Run tests after each change
- Commit frequently with clear messages
- Keep a log of decisions and trade-offs

### After Completing
- Run full test suite
- Review all changes holistically
- Update documentation
- Create PR with clear description

## Context Preservation Techniques

### Decision Records
```markdown
# ADR-001: Refactoring Authentication Module

## Status: Accepted
## Context: Auth module has grown complex with mixed concerns
## Decision: Split into auth, session, and permission modules
## Consequences: Better separation of concerns, more files to manage
```

### Dependency Mapping
- Use AST analysis to find all references
- Build call graphs for critical paths
- Document external API contracts
- Track configuration dependencies

## Common Refactoring Patterns

### Extract Module
1. Identify cohesive group of functions
2. Create new module with clear interface
3. Move functions, update imports
4. Verify no circular dependencies
5. Update tests

### Consolidate Duplicates
1. Find similar code blocks
2. Identify common abstraction
3. Create shared utility
4. Replace duplicates with calls to shared code
5. Test each replacement individually
