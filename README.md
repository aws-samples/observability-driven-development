# Operations-Driven Development with Ollyver

AI-powered observability automation using the Ollyver agent to transform serverless applications from "black box" to "glass box" observability.

---

> **📢 Preview Release**
> 
> This content is best experienced at an AWS-hosted event using the full workshop: [Operations-Driven Development Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US)
>
> **Current Status:** This repository is in **preview mode**. You can currently access and use the Ollyver agent code and configuration. 
>
> **Coming Soon:** Full standalone workshop experience with MCP (Model Context Protocol) integration for organizational standards management. Stay tuned for updates!

---

## Overview

This project demonstrates **Operations-Driven Development** - an approach that elevates observability to a primary concern in the development lifecycle using AI agents. Meet **Ollyver**, an AI agent that automatically detects observability gaps and implements comprehensive monitoring, logging, and tracing across your serverless applications.

## What You'll Learn

This hands-on workshop teaches you how to transform a serverless application from "black box" to "glass box" observability using AI automation. You'll experience:

- **AI-Powered Observability** - Watch Ollyver automatically detect and fix observability gaps
- **Distributed Tracing** - Implement AWS X-Ray tracing across all services
- **Structured Logging** - Create JSON logs with tenant attribution and correlation IDs
- **Custom Metrics** - Build business KPIs and operational dashboards
- **Organizational Scaling** - Apply consistent observability patterns across teams

### Workshop Format

This is a **self-paced, hands-on workshop** where you'll:

1. **Deploy** a real serverless application to your AWS account
2. **Discover** observability gaps in the application
3. **Meet Ollyver** - Your AI observability companion
4. **Transform** the application with automated instrumentation
5. **Validate** improvements in AWS CloudWatch and X-Ray

**Time Required:** 2-3 hours  
**Cost:** Minimal AWS charges (< $5 for workshop duration)

### What is Ollyver?

Ollyver is a specialized AI agent built on [Kiro CLI](https://kiro.dev/) that automates observability implementation. Instead of manually instrumenting code, Ollyver:

- **Scans** your codebase to detect architecture and gaps
- **Detects** missing observability patterns against organizational standards
- **Suggests** fixes with educational context
- **Implements** patterns automatically with AWS deployment

### Key Features

- ✅ **Automated X-Ray Tracing** - Distributed tracing across all services
- ✅ **Structured Logging** - JSON logs with tenant attribution and correlation IDs
- ✅ **Custom Business Metrics** - Track KPIs and operational metrics
- ✅ **CloudWatch Dashboards** - Automated dashboard creation
- ✅ **Organizational Standards** - Enforce consistent observability patterns

## Architecture

The sample application is a serverless ride-sharing service consisting of:

- **Amazon API Gateway** - HTTP API endpoint
- **AWS Lambda** - Two functions (putItemFunction, getByIdFunction)
- **Amazon DynamoDB** - Data storage
- **CloudWatch** - Logs, metrics, and dashboards
- **AWS X-Ray** - Distributed tracing

![Architecture](/img/Architecture.png)

## Prerequisites

- **AWS Account** with CLI configured
- **AWS CLI** - [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- **AWS SAM CLI** - [Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- **Docker** - Required for SAM build
- **Python 3.11+** - For Lambda functions
- **Kiro CLI** - [Installation Guide](https://kiro.dev/)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/aws-samples/observability-driven-development.git
cd observability-driven-development
```

### 2. Deploy the Application

```bash
cd cloudformation
sam build
sam deploy --guided
```

Use stack name: `observability-driven-development`

### 3. Setup Kiro CLI

```bash
# Authenticate with AWS Builder ID
kiro-cli login --use-device-flow
```

### 4. Activate Ollyver Agent

```bash
# From project root
kiro-cli chat --agent ollyver
```

### 5. Test the Application

```bash
# Get API endpoint
export API_URL=$(aws cloudformation describe-stacks \
  --stack-name observability-driven-development \
  --query 'Stacks[0].Outputs[?OutputKey==`HttpApiUrl`].OutputValue' \
  --output text)

# Test POST
curl -X POST ${API_URL}items \
  -d '{"id":"1a2b3c4d","name":"test user","milesTraveled":"12","totalTravelTime":"600","price":"13.32","tenantId":"1001"}'

# Test GET
curl ${API_URL}items/1a2b3c4d
```

## Workshop Modules

This workshop is organized into modules that guide you through the complete observability transformation journey. **Start with the Introduction** to understand the concepts, then follow the modules in order.

### Getting Started

**📖 [Introduction](docs/introduction.md)** - Start here to understand:
- What is observability and why it matters
- The traditional observability gap problem
- How AI agents solve the developer burden
- What you'll accomplish in this workshop

**⚙️ [Setup Guide](docs/setup.md)** - Environment setup:
- Install prerequisites (AWS CLI, SAM CLI, Kiro CLI)
- Deploy the sample application
- Configure Ollyver agent
- Test your deployment

### Workshop Modules

**Module 1: [Explore Your Application](docs/module-1.md)**
- Examine the serverless ride-sharing application
- Discover observability gaps manually
- Understand organizational requirements
- See the "black box" problem firsthand

**Module 2: [Meet Ollyver](docs/module-2.md)**
- Introduction to the Ollyver AI agent
- Understand the automated workflow
- Test Ollyver's knowledge
- Prepare for transformation

**Module 3: [Closing the Gaps](docs/module-3.md)**
- Watch Ollyver detect observability gaps
- Implement X-Ray tracing automatically
- Add structured logging with correlation IDs
- Deploy and validate improvements

**Module 4: [Dynamic Requirements](docs/module-4.md)**
- Adapt to changing organizational standards
- Implement PII masking in logs
- See how Ollyver handles evolving requirements
- Experience continuous observability improvement

**Module 5: [Organizational Scaling](docs/module-5.md)**
- Scale observability patterns across teams
- Customize organizational standards
- Apply consistent patterns organization-wide
- Build a culture of observability excellence

## Ollyver Agent Configuration

The Ollyver agent is located in the `ollyver/` directory:

```
ollyver/
├── .amazonq/
│   └── cli-agents/
│       └── ollyver.json          # Agent configuration
├── Org-Standards/                 # Organizational requirements
│   ├── observability-requirements.md
│   ├── core-patterns.md
│   └── deployment-guide.md
├── Approach/                      # Agent workflow
│   ├── process-overview.md
│   ├── session-management.md
│   └── workshop-methodology.md
└── ollyver-agent-instructions.md  # Agent instructions
```

### Customizing Organizational Standards

Edit files in `ollyver/Org-Standards/` to customize observability requirements for your organization:

- **observability-requirements.md** - Define your observability standards
- **core-patterns.md** - Implementation patterns and best practices
- **deployment-guide.md** - AWS deployment procedures

## Project Structure

```
observability-driven-development/
├── cloudformation/              # CloudFormation templates
│   └── application.yaml         # Main application template
├── src/handlers/                # Lambda function code
│   ├── putItemFunction/
│   └── getByIdFunction/
├── ollyver/                     # Ollyver agent configuration
├── docs/                        # Workshop documentation
├── images/                      # Workshop images
└── README.md                    # This file
```

## What You'll Learn

By completing this workshop, you will:

- **Understand Observability Fundamentals** - Learn the three pillars (logs, metrics, traces) and why they matter
- **Experience AI-Powered Automation** - See how AI agents can automate complex observability tasks
- **Implement Distributed Tracing** - Add AWS X-Ray tracing across Lambda functions and API Gateway
- **Create Structured Logs** - Build JSON logs with tenant attribution and correlation IDs
- **Build Custom Metrics** - Track business KPIs and operational metrics in CloudWatch
- **Scale Organizational Patterns** - Apply consistent observability standards across teams
- **Master Operations-Driven Development** - Elevate observability as a primary development concern

### Skills You'll Gain

- Working with Kiro CLI and custom AI agents
- AWS observability services (X-Ray, CloudWatch, Lambda Insights)
- Serverless application instrumentation
- Infrastructure as Code with AWS SAM
- Best practices for production observability

## Clean Up

To avoid ongoing charges, delete the CloudFormation stack:

```bash
sam delete --stack-name observability-driven-development
```

Or via AWS Console:
1. Navigate to CloudFormation console
2. Select `observability-driven-development` stack
3. Click **Delete**

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

This project is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file for details.

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License.
