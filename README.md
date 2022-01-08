# Observability Driven Development

Observability Driven Development elevates application and infrastructure observability to primary concerns in the development lifecycle. Operational health, security, compliance and business impact are instrumented early in the life cycle to provide comprehensive observability before, during, and after application deployments.

Observability Driven Development aligns with development models like Test Driven Development and Behavior Driven Development:

Application components can be stubbed out at the start of development; they do not need to be in their final forms.
Observing infrastructure and deployment pipelines ensures environment differences and defects introduce during deployment are observable.
Automation is leveraged wherever possible to minimize unintended variation in processes.
Using an Infrastructure as code (IaC) mindset for testing and operations observability improves confidence in workload health and reduces troubleshooting efforts.

## Sample solution

The ride share application used in this workshop consists of serverless services such as Amazon API Gateway, AWS Lambda, and Amazon DynamoDB.

For simplicity we are using just two AWS Lambda functions. One Lambda function to insert an Item into a DynamoDB table, and another function to retrieve it using the appropriate unique ID.

## Architecture Diagram

![Architecture](/img/Architecture.png)

# Sample Environment Deployment
## Build & Deploy

### Prerequisites
- An active AWS account
- AWS CLI configured with account access
- Docker installed on the local machine
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

### Build and deploy the sample application

Deploy the architure represented in the [Architecture Diagram](#architecture-diagram) to have a sample application running on your AWS account to follow the activities in the workshop. 

### Clone the Repo

Clone the GitHub repository to your workstation

`git clone https://github.com/aws-samples/observability-driven-development.git`

### Build

Building in a container will help alleviate any local dependency issues.

`sam build --use-container`

### Deploy

`sam deploy --guided`

This command will package and deploy your application to AWS, with a series of prompts:

- **Stack Name:** The name of the stack to deploy to AWS CloudFormation. This should be unique to your account and region. We will use `observability-driven-development` throughout this project.
- **AWS Region:** The AWS region you want to deploy your app to.
  Confirm changes before deploy: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
- **Allow SAM CLI IAM role creation:** Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack that creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn’t provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
- **Save arguments to** `samconfig.toml`: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to the application.

## Prepare your environment
Follow the instructions [here](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US/prepare-your-environment).

## Workshops
Follow the instructions [here](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US/) to run every workshop.

[**Workshop 1 - Instrumenting With X-Ray**](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US/workshop-1-x-ray-instrumentation)

[**Workshop 2 - Create Custom Widget**](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US/workshop-2-create-custom-metric)

[**Workshop 3 - Debug faster with widgets**](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US/workshop-3-deployment-version)

[**Workshop 4 - Create custom metric**](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/89b1708b-12ca-4871-a1e4-171c600c2736/en-US/workshop-4-business-metric)

## Summary

Congratulations! You have completed the workshops. Today you learned:

Observability Driven Development promotes observability as a primary concern in the development process.
- You can provide business value context in metrics and KPIs to observe business value of healthy and impaired systems.
- You can use AWS X-Ray to analyze distributed applications, thanks to AWS Lambda and Amazon API Gateway native integration.
- You can create custom Cloudwatch widgets to display business value metrics.
- You can adding metrics that include versioning to provide additional observability for blue-green, canary and hybrid deployments.
- You can use custom metrics to extend the information available for observability in your CloudWatch dashboards.

## Clean Up Resources

To avoid further charges for resources you used during this tutorial, delete the resources created by your AWS SAM template and the CloudWatch logs created by your Lambda functions. 


### To delete your AWS CloudFormation stack on the console

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at https://console.aws.amazon.com/cloudformation

2. In the Stacks column, choose your `observability-driven-development` stack, and then choose Delete.

3. When prompted, choose Delete stack. The Lambda functions, CodeDeploy application and deployment group, and IAM roles created by AWS SAM are deleted.

### To delete your AWS CloudFormation stack via sam cli

`sam delete`

This command will delete the cloudformation stack with a series of prompts:

- **Are you sure you want to delete the stack observability-driven-development in the region <aws-region> ? [y/N]::** 
choose y
- **Are you sure you want to delete the folder observability-driven-development in S3 which contains the artifacts? [y/N]:::** 
choose y
## License Summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License. See the [LICENSE](LICENSE) file.

The sample code within this documentation is made available under the MIT-0 license. See the [LICENSE-SAMPLECODE](LICENSE-SAMPLECODE) file.
