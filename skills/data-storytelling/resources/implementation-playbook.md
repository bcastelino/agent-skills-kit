# Data Storytelling Implementation Playbook

Detailed patterns, templates, and examples for transforming data into compelling narratives.

## Story Frameworks

### The Situation-Complication-Resolution (SCR)
1. **Situation**: Establish context and baseline metrics
2. **Complication**: Present the unexpected finding or problem
3. **Resolution**: Recommend actions supported by data

### The Pyramid Principle
- Start with the conclusion
- Group supporting arguments logically
- Support each argument with data evidence
- Use MECE (Mutually Exclusive, Collectively Exhaustive) groupings

## Visualization Best Practices

### Chart Selection Guide
| Purpose | Best Chart | Avoid |
|---------|-----------|-------|
| Comparison | Bar chart | Pie chart (>5 items) |
| Trend | Line chart | Stacked bar |
| Distribution | Histogram, Box plot | Table of numbers |
| Composition | Stacked bar, Treemap | 3D pie chart |
| Relationship | Scatter plot | Bar chart |
| Geographic | Choropleth map | Table with locations |

### Design Principles
- Use consistent color palette (max 5-7 colors)
- Remove chart junk (gridlines, borders, backgrounds)
- Label directly instead of using legends
- Highlight the key finding with color or annotation
- Use appropriate aspect ratio (wider for trends)

## Presentation Templates

### Executive Summary (1 Page)
```markdown
# [Title: Key Finding in One Sentence]

**Bottom Line**: [One sentence recommendation]

**Key Metrics**: [3-4 numbers with trend arrows]

**Supporting Evidence**: [2-3 bullet points with data]

**Recommended Action**: [Specific next step with timeline]
```

### Data Deep Dive (Multi-Page)
1. Executive Summary (1 slide)
2. Context and Methodology (1 slide)
3. Key Findings (2-3 slides, one insight per slide)
4. Supporting Analysis (2-3 slides)
5. Recommendations (1 slide)
6. Appendix (detailed data, methodology notes)

## Audience Adaptation

### By Stakeholder Level
- **C-Suite**: Focus on business impact and ROI
- **Director**: Balance strategy with operational detail
- **Manager**: Include actionable tactics and timelines
- **Analyst**: Provide methodology and raw data access
