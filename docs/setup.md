# Setup Guide

This guide will help you set up your local development environment to work with Ollyver and deploy the sample application to AWS.

## Prerequisites

Before you begin, ensure you have the following installed:

- **AWS Account** with CLI configured
- **AWS CLI** - [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- **AWS SAM CLI** - [Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- **Docker** - Required for SAM build
- **Python 3.11+** - For Lambda functions
- **Kiro CLI** - [Installation Guide](https://kiro.dev/)

## Step 1: Clone the Repository

```bash
git clone https://github.com/aws-samples/observability-driven-development.git
cd observability-driven-development
```

## Step 2: Configure AWS CLI

Ensure your AWS CLI is configured with credentials:

```bash
aws configure
```

You'll need:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-1`)
- Default output format (e.g., `json`)

## Step 3: Install Kiro CLI

Follow the [Kiro CLI installation guide](https://kiro.dev/) for your operating system.

After installation, authenticate using AWS Builder ID:

```bash
kiro-cli login --use-device-flow
```

Follow the prompts to authenticate:
1. Copy the URL from your terminal into a new browser window
2. Login using AWS Builder ID
3. Return to the terminal to complete authentication

## Step 4: Deploy the Application

Deploy the serverless application using SAM:

```bash
# Navigate to cloudformation directory
cd cloudformation

# Build the application
sam build

# Deploy with guided prompts
sam deploy --guided
```

During deployment, you'll be prompted for:
- **Stack Name**: Use `observability-driven-development`
- **AWS Region**: Choose your preferred region (e.g., `us-east-1`)
- **Confirm changes before deploy**: Choose `Y` or `N`
- **Allow SAM CLI IAM role creation**: Choose `Y`
- **Save arguments to samconfig.toml**: Choose `Y` for future deployments

## Step 5: Test Your Deployment

After deployment completes, test the API endpoint:

### Get API Endpoint

```bash
export API_URL=$(aws cloudformation describe-stacks \
  --stack-name observability-driven-development \
  --query 'Stacks[0].Outputs[?OutputKey==`HttpApiUrl`].OutputValue' \
  --output text)

echo $API_URL
```

### Test POST Request

```bash
curl -X POST ${API_URL}items \
  -d '{
    "id": "1a2b3c4d",
    "name": "first last",
    "milesTraveled": "12",
    "totalTravelTime": "600",
    "price": "13.32",
    "tenantId": "1001"
  }' -i
```

Expected response: `200 OK` with message "Item added successfully"

### Test GET Request

```bash
curl ${API_URL}items/1a2b3c4d
```

Expected response: JSON object with the ride information you just posted.

## Step 6: Setup Ollyver Agent

Navigate to the project root and activate the Ollyver agent:

```bash
cd ..
kiro-cli chat --agent ollyver
```

You should see Ollyver's welcome message. The agent is now ready to help you add observability to your application.

## Step 7: Generate Load (Optional)

To simulate realistic traffic for observability testing, you can generate synthetic load:

```bash
# Install artillery if not already installed
npm install -g artillery

# Set your API URL
export URL=$(aws cloudformation describe-stacks \
  --stack-name observability-driven-development \
  --query 'Stacks[0].Outputs[?OutputKey==`HttpApiUrl`].OutputValue' \
  --output text)

# Run load generator (runs for 50 minutes)
artillery run loadgen.yaml
```

> **Note**: Keep the terminal window open while the load generator runs. Open a new terminal for the workshop modules.

## Troubleshooting

### SAM Build Fails
- Ensure Docker is running
- Check that Python 3.11+ is installed
- Verify you're in the `cloudformation` directory

### Kiro CLI Authentication Issues
- Ensure you have an active internet connection
- Try logging out and back in: `kiro-cli logout` then `kiro-cli login --use-device-flow`

### API Endpoint Not Found
- Verify the CloudFormation stack deployed successfully
- Check the stack outputs in AWS Console or via CLI

## What's Next

Now that your environment is set up and the application is deployed, proceed to [Module 1: Explore Your Application](module-1-explore-application.md) to begin discovering observability gaps.
