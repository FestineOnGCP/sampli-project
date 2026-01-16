# Terraform Infrastructure for Flask IP App

This Terraform configuration creates a complete AWS infrastructure for deploying the Flask IP address application.

## Architecture

The infrastructure includes:
- **ECR Repository**: Container image registry
- **VPC**: Virtual private cloud with public and private subnets
- **ECS Cluster**: Fargate cluster for running containers
- **ECS Task Definition**: Defines the container configuration
- **ECS Service**: Manages the running tasks
- **Application Load Balancer (ALB)**: Distributes traffic to ECS tasks
- **Target Group**: Routes traffic from ALB to ECS tasks
- **CloudFront Distribution**: CDN with ALB as origin

## Prerequisites

1. AWS CLI configured with appropriate credentials
2. Terraform installed (>= 1.0)
3. Docker image pushed to ECR (or use the GitHub Actions workflow)

## Usage

1. **Copy the example variables file:**
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   ```

2. **Edit `terraform.tfvars` with your desired values:**
   ```bash
   # Modify values as needed
   aws_region = "us-east-1"
   project_name = "flask-ip-app"
   ```

3. **Initialize Terraform:**
   ```bash
   cd terraform
   terraform init
   ```

4. **Review the execution plan:**
   ```bash
   terraform plan
   ```

5. **Apply the configuration:**
   ```bash
   terraform apply
   ```

6. **Get the CloudFront URL:**
   After applying, you can access your application via the CloudFront URL:
   ```bash
   terraform output cloudfront_url
   ```

## Important Notes

### CloudFront and ALB Configuration

The CloudFront distribution accesses the ALB directly. For production, consider:

1. Using AWS WAF with CloudFront for additional security
2. Restricting ALB security group to CloudFront IP ranges (optional, but recommended for production)
3. Using custom domain with SSL certificate
4. Enabling HTTPS on the ALB listener for end-to-end encryption

### ECR Image

Before the ECS service can start, you need to push an image to the ECR repository:

```bash
# Get login token
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Build and tag image
docker build -t flask-ip-app .
docker tag flask-ip-app:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/flask-ip-app:latest

# Push image
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/flask-ip-app:latest
```

Or use the GitHub Actions workflow to automatically build and push.

## Outputs

After applying, Terraform will output:
- ECR repository URL
- ECS cluster and service names
- ALB DNS name
- CloudFront distribution ID and domain name
- CloudFront URL

## Destroying Resources

To destroy all created resources:
```bash
terraform destroy
```

## Variables

See `variables.tf` for all available variables and their descriptions.
