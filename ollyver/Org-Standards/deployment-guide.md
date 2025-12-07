# AWS Deployment Guide

## Lambda Function Deployment

### Check for Existing Deployment Script
1. **Check if `code/workshop/updateLambda.sh` exists**
2. **If exists**: Use the existing script for deployment
3. **If not exists**: Use manual AWS CLI deployment commands

### Using Existing Script (Preferred)
```bash
# Navigate to workshop directory
cd code/workshop

# Execute the deployment script
./updateLambda.sh
```

### Manual Deployment (Fallback)
If the script doesn't exist, use these commands:
```bash
# For each Lambda function directory:
cd [function-directory]
zip index.zip index.py
aws lambda update-function-code --function-name [function-name] --zip-file fileb://index.zip
```

## Pattern-Specific Deployment Steps

### X-Ray Tracing Pattern
After deploying code changes, enable X-Ray tracing:
```bash
# Enable X-Ray tracing on Lambda functions
aws lambda update-function-configuration --function-name getByIdFunction --tracing-config Mode=Active
aws lambda update-function-configuration --function-name putItemFunction --tracing-config Mode=Active

# Update IAM role permissions
aws iam attach-role-policy --role-name lambda-execution-role --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess
```

### Operational Dashboards Pattern
Create CloudWatch dashboard:
```bash
# Create dashboard using AWS CLI
aws cloudwatch put-dashboard --dashboard-name "ObservabilityDashboard" --dashboard-body file://dashboard-config.json

# Or use AWS Console to create dashboard manually
# Navigate to CloudWatch > Dashboards > Create Dashboard
```

## Post-Deployment Validation
- Verify function updated in AWS Console
- Check CloudWatch logs for new observability data
- Validate X-Ray traces if implemented (X-Ray Console)
- Confirm custom metrics in CloudWatch Metrics
- Test dashboard widgets display data correctly
