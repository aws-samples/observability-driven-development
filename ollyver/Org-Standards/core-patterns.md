# Core Observability Patterns

## Pattern 1: Automatic X-Ray Instrumentation
**Trigger**: Lambda function without tracing
**Action**: Add X-Ray tracing configuration and SDK imports
**Demonstrates**: Distributed tracing fundamentals

```python
# Before (manual)
def lambda_handler(event, context):
    return process_request(event)

# After (Ollyver automated)
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
patch_all()

@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    return process_request(event)
```

## Pattern 2: Structured Logging Detection
**Trigger**: Print statements or basic logging
**Action**: Implement structured JSON logging with correlation IDs
**Demonstrates**: Log analysis and correlation

```python
# Before (manual)
print(f"Processing user {user_id}")

# After (Ollyver automated)
import json
import uuid

correlation_id = str(uuid.uuid4())
logger.info(json.dumps({
    "message": "Processing user",
    "user_id": user_id,
    "correlation_id": correlation_id,
    "timestamp": datetime.utcnow().isoformat()
}))
```

## Pattern 3: Business Metrics Identification
**Trigger**: Business logic without metrics
**Action**: Add custom CloudWatch metrics for key operations with namespace - RideShare/Business
**Demonstrates**: Business observability vs technical metrics

```python
# Before (manual)
def process_order(order):
    result = validate_order(order)
    return result

# After (Ollyver automated)
import boto3
cloudwatch = boto3.client('cloudwatch')

def process_order(order):
    result = validate_order(order)
    
    # Ollyver adds business metrics
    cloudwatch.put_metric_data(
        Namespace='RideShare/Business',
        MetricData=[{
            'MetricName': 'OrdersProcessed',
            'Value': 1,
            'Unit': 'Count',
            'Dimensions': [{'Name': 'Status', 'Value': result.status}]
        }]
    )
    return result
```

## Pattern 4: Multi-Tenant Observability
**Trigger**: Multi-tenant code patterns detected
**Action**: Add tenant-specific logging and metrics
**Demonstrates**: Tenant isolation in observability

```python
# Before (manual)
def handle_request(event):
    return process_tenant_data(event['data'])

# After (Ollyver automated)
def handle_request(event):
    tenant_id = extract_tenant_id(event)
    
    with xray_recorder.in_subsegment(f'tenant_{tenant_id}'):
        logger.info(json.dumps({
            "tenant_id": tenant_id,
            "operation": "process_data",
            "correlation_id": correlation_id
        }))
        
        result = process_tenant_data(event['data'])
        
        cloudwatch.put_metric_data(
            Namespace='MultiTenant/Usage',
            MetricData=[{
                'MetricName': 'RequestsPerTenant',
                'Value': 1,
                'Dimensions': [{'Name': 'TenantId', 'Value': tenant_id}]
            }]
        )
    return result
```

## Pattern 5: Error Handling & Alerting
**Trigger**: Exception handling without observability
**Action**: Add error tracking and alerting
**Demonstrates**: Proactive error monitoring

```python
# Before (manual)
try:
    result = risky_operation()
except Exception as e:
    return {"error": str(e)}

# After (Ollyver automated)
try:
    result = risky_operation()
except Exception as e:
    # Ollyver adds comprehensive error tracking
    error_details = {
        "error_type": type(e).__name__,
        "error_message": str(e),
        "correlation_id": correlation_id,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    logger.error(json.dumps(error_details))
    
    cloudwatch.put_metric_data(
        Namespace='ErrorTracking',
        MetricData=[{
            'MetricName': 'Errors',
            'Value': 1,
            'Dimensions': [{'Name': 'ErrorType', 'Value': type(e).__name__}]
        }]
    )
    
    xray_recorder.current_subsegment().add_exception(e)
    return {"error": "Internal server error", "correlation_id": correlation_id}
```

## Implementation Methodology
1. **Show the Gap**: Identify what's missing
2. **Explain the Pattern**: Why this observability is needed
3. **Automate the Fix**: Implement the solution
4. **Demonstrate Value**: Show the resulting observability data
5. **Reinforce Understanding**: Explain how to apply this pattern elsewhere
