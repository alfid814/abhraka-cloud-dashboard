# 📖 Abhraka Cloud Dashboard - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Dashboard Overview](#dashboard-overview)
4. [Service Management](#service-management)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)

## Introduction

Abhraka Cloud Dashboard is a professional infrastructure management platform that provides unified control over 10 AWS services running on LocalStack.

## Dashboard Overview

### Navigation
- **Top Bar**: System health status and platform info
- **Stats Cards**: Quick overview of services and resources
- **Service Cards**: Individual service management

### Understanding the Interface

|      Element    | 		     Description 	       |
|-----------------|--------------------------------------------|
| Active Services | Total number of monitored services         |
| Healthy Count   | Number of services with operational status |
| Total Assets    | Sum of all resources across services       |
| Click Card      | Interactive management access              |

## Service Management

### 1. S3 Storage
- **Create bucket**: Enter bucket name
- **Upload file**: Provide file name, content, and bucket
- **View buckets**: Dashboard shows existing buckets

### 2. API Gateway
- **Create API**: Enter API name and stage
- **Test API**: Select existing API to test endpoint

### 3. DynamoDB
- **Create table**: Will be auto-created on first insert
- **Add item**: Provide table name, ID, and data

[Continue with all 10 services...]

## Troubleshooting

### Common Issues

|	     Issue 	    | 		    Solution 	  	    |
|---------------------------|---------------------------------------|
| Dashboard not loading     | Check if LocalStack is running	    |
| 404 errors 		    | Ensure you're using correct port 5000 |
| Cannot connect to service | Verify Docker is running 		    |

### Getting Help

- Check the logs: `tail -f logs/dashboard.log`
- Verify LocalStack health: `curl http://localhost:4566/_localstack/health`

## FAQ

**Q: Do I need an AWS account?**  
A: No, LocalStack emulates AWS locally.

**Q: Is data persisted?**  
A: Yes, with PERSISTENCE=1 enabled.

**Q: Can I access from another computer?**  
A: Yes, use the WSL2 IP address instead of localhost.
