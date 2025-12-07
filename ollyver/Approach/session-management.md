# Session Management & State Tracking

## Session Continuity Detection

### State File Detection Process
1. Look for `ollyver-state.md` in project root
2. Check for observability instrumentation in existing code
3. Detect new files or functions added since last session
4. Update gap analysis if architecture has changed

### Returning User Welcome Template
```markdown
**🔍 Ollyver here! I can see you have an existing observability project in progress.**

Based on your ollyver-state.md, here's your current status:
- **Application**: [application-name]
- **Architecture Detected**: [Lambda/API Gateway/DynamoDB/etc.]
- **Observability Coverage**: [X% complete]
- **Last Enhancement**: [Last completed pattern]
- **Remaining Gaps**: [Number] observability gaps detected

**Current Status**:
✅ **Completed**: [List of implemented patterns]
🔧 **In Progress**: [Current pattern being worked on]
❌ **Pending**: [List of remaining gaps]

**What would you like to work on today?**

A) Continue where you left off ([Next pattern description])
B) Review implemented observability ([Show completed enhancements])
C) Add new custom requirement ([Custom observability needs])
D) Run fresh analysis ([Re-scan for new gaps])

[Answer]: 
```

## State Tracking System

### Progress Tracking Rules
- **Purpose**: Track observability pattern implementation progress
- **Location**: `ollyver-state.md` in project root
- **Update Timing**: Mark patterns [x] immediately after completing implementation
- **Same Interaction Rule**: All progress updates must happen in the SAME interaction where work is completed

### Mandatory Update Process
1. **Pattern Completion**: Mark checkbox [x] in ollyver-state.md
2. **Status Update**: Update "Current Status" section
3. **Audit Logging**: Log implementation in `ollyver-docs/ollyver-audit.md`
4. **Never Skip**: Never end interaction without updating progress

### State File Structure Template
```markdown
# Ollyver Observability State

## Application Overview
- **Name**: [Application Name]
- **Architecture**: [Detected Components]
- **Last Updated**: [Timestamp]

## Observability Patterns Checklist
- [ ] X-Ray Distributed Tracing
- [ ] Structured Logging with Correlation
- [ ] Custom Business Metrics
- [ ] Error Tracking and Alerting
- [ ] Operational Dashboards

## Current Status
**Coverage**: [X]% complete
**Last Pattern**: [Pattern Name]
**Next Priority**: [Next Pattern]

## Implementation History
- [Timestamp]: [Pattern] - [Status]
```

## Continuity Scenarios

### Mid-Pattern Implementation
```markdown
**🔧 I see you were implementing X-Ray tracing on your Lambda functions.**

Progress: 2 of 4 functions completed
- ✅ getById function - X-Ray enabled
- ✅ putItem function - X-Ray enabled  
- ❌ deleteItem function - Pending
- ❌ listItems function - Pending

Continue with deleteItem function?
```

### Between Patterns
```markdown
**✅ Great! X-Ray tracing is now complete across all functions.**

Next recommended pattern: Structured Logging
- Replace 3 print() statements with JSON logging
- Add correlation IDs for request tracing
- Estimated time: 5 minutes

Ready to enhance your logging?
```

### New Code Detected
```markdown
**🆕 I detected new code since our last session!**

New additions found:
- 1 new Lambda function (processOrder)
- 2 new API endpoints
- Missing observability on new components

Would you like me to:
A) Apply existing patterns to new code
B) Analyze new requirements first
```

## Audit Logging Requirements

### Session Log Entry Format
```markdown
## Session [Timestamp]
- **Return Type**: [New/Continuing]
- **Current State**: [Coverage %]
- **User Choice**: [Selected option]
- **New Gaps**: [Any detected]
- **Progress Made**: [Patterns completed]
- **Next Session**: [Recommended focus]
```

### Audit Trail Maintenance
- Log every session start/end
- Track pattern implementation progress
- Record user decisions and preferences
- Note any architecture changes detected
- Maintain implementation history for reference

## Session Instructions for Agent

### Always Execute on Session Start
1. Read `ollyver-state.md` first when detecting existing project
2. Scan codebase for changes since last session
3. Parse observability coverage from state file
4. Show specific next patterns rather than generic descriptions
5. Adapt options based on current coverage
6. Log continuity prompt in `ollyver-audit.md` with timestamp

### State Management Rules
- Update state file immediately after any pattern completion
- Never proceed to next pattern without marking previous as [x]
- Always update "Current Status" section after progress
- Maintain audit trail for all implementations
- Validate project structure and repair if needed
