# Code Reviewer Implementation Playbook

Detailed patterns, checklists, and frameworks for expert-level code review.

## Review Checklist

### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation on all user inputs
- [ ] SQL queries use parameterized statements
- [ ] Authentication and authorization checks present
- [ ] No sensitive data in logs or error messages
- [ ] Dependencies are from trusted sources
- [ ] CORS and CSP headers configured correctly

### Performance
- [ ] No N+1 query patterns
- [ ] Appropriate indexing for database queries
- [ ] Pagination for large result sets
- [ ] Caching strategy where applicable
- [ ] No unnecessary memory allocations in loops
- [ ] Async operations for I/O-bound tasks

### Reliability
- [ ] Error handling covers edge cases
- [ ] Graceful degradation for external dependencies
- [ ] Timeouts set for network calls
- [ ] Retry logic with exponential backoff
- [ ] Circuit breakers for critical paths
- [ ] Resource cleanup (connections, file handles)

### Maintainability
- [ ] Functions have single responsibility
- [ ] Clear and descriptive naming
- [ ] No magic numbers or strings
- [ ] Appropriate abstraction level
- [ ] Tests cover happy path and edge cases
- [ ] Documentation for public APIs

## Review Workflow

### Severity Classification
| Level | Label | Action |
|-------|-------|--------|
| P0 | Blocker | Must fix before merge |
| P1 | Important | Should fix before merge |
| P2 | Suggestion | Nice to have improvement |
| P3 | Nit | Minor style preference |

### Feedback Templates
```markdown
**[P0 - Security]** SQL injection vulnerability
Line 42: User input is concatenated directly into query.
Suggestion: Use parameterized queries instead.

**[P2 - Performance]** Consider caching
This endpoint is called frequently with the same parameters.
Adding a TTL cache could reduce database load significantly.
```

## AI-Generated Code Review

### Additional Checks for AI Code
- Verify logic correctness (LLMs can produce plausible but wrong code)
- Check for hallucinated APIs or libraries
- Validate error handling completeness
- Ensure consistent patterns with existing codebase
- Test edge cases that AI may not have considered
