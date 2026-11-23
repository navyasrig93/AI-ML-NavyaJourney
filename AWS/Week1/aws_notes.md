AWS Learning Journey - Week 1

Goal
Build foundational AWS Cloud knowledge while preparing for:

AWS Certified Cloud Practitioner
AWS AI Practitioner
AWS Machine Learning Engineer Associate
Week 1 Learning Summary
This week focused on understanding cloud fundamentals, AWS global infrastructure, security concepts, storage, compute services, and serverless computing.

Day 1 - Cloud Fundamentals
Topics Learned
What is Cloud Computing
Benefits of Cloud Computing
What is AWS
Key Learnings
Cloud Computing provides on-demand access to computing resources over the internet.

Benefits
Cost Savings
Scalability
Reliability
Flexibility
Day 2 - AWS Global Infrastructure
Topics Learned
AWS Regions
Geographic locations where AWS operates data centers.

Availability Zones
Independent groups of data centers within a Region.

Edge Locations
Locations used to deliver content closer to end users.

Key Learnings
High Availability
Fault Tolerance
Disaster Recovery
Global Scalability
Day 3 - Shared Responsibility Model
Security of the Cloud (AWS Responsibility)
AWS manages:

Hardware
Networking Infrastructure
Physical Security
Data Centers
Global Infrastructure
Security in the Cloud (Customer Responsibility)
Customers manage:

Applications
Data
User Permissions
IAM Configuration
Passwords
Encryption
Key Learning
AWS and customers share security responsibilities.

Day 4 - IAM (Identity and Access Management)
Topics Learned
IAM User
An individual identity that can access AWS services and resources.

IAM Group
A collection of users sharing similar permissions.

IAM Policy
A set of permissions that determines what actions are allowed or denied.

Root User
The account owner with unrestricted access.

AWS Best Practices
Enable MFA
Avoid using Root User for daily work
Follow Least Privilege Principle
Use IAM Users and Groups
Day 5 - Amazon S3
What is Amazon S3?
Amazon Simple Storage Service (S3) is a highly scalable object storage service.

Key Concepts
Bucket
A container used to store objects.

Example:

navya-ml-data
Object
A file stored inside a bucket.

Examples:

sales.csv
resume.pdf
image.jpg
S3 Use Cases
Backup & Recovery
Store backups securely.

Data Lakes
Store large amounts of structured and unstructured data.

Static Website Hosting
Host web applications.

AI & Machine Learning
Store:

Training Data
Images
Videos
Feature Files
Model Artifacts
Day 6 - Amazon EC2
What is EC2?
Amazon Elastic Compute Cloud (EC2) provides virtual servers that can be launched on demand.

Simple Definition
A virtual computer running inside AWS.

Key Concepts
Instance
A virtual machine running in AWS.

Security Group
A virtual firewall controlling inbound and outbound traffic.

Instance Types
Different hardware configurations.

Examples:

t2.micro
t3.micro
m5.large
EC2 Use Cases
Website Hosting
Backend APIs
Application Servers
Databases
Machine Learning Inference
EC2 vs S3
EC2	S3
Compute Service	Storage Service
Runs Applications	Stores Files
Virtual Server	Object Storage
Processes Data	Stores Data
Day 7 - AWS Lambda
What is AWS Lambda?
AWS Lambda is a serverless compute service that allows code execution without managing servers.

Key Idea
EC2 = Manage Servers

Lambda = No Server Management
AWS automatically handles:

Server Provisioning
Scaling
Maintenance
Infrastructure Management
Key Concepts
Serverless
Developers focus on code while AWS manages the infrastructure.

Event-Driven Computing
Functions execute when events occur.

Examples:

File uploaded to S3
API Request
Database Change
Scheduled Event
Lambda Use Cases
Automated Scheduled Jobs
Run periodic tasks automatically.

Real-Time Data Processing
Process incoming data streams instantly.

File Processing
Resize images or process uploaded files.

AI/ML Automation
Trigger machine learning workflows and data pipelines.

Backend APIs
Power lightweight serverless applications.

Lambda vs EC2
Lambda	EC2
Serverless	Server-Based
AWS Manages Infrastructure	User Manages Infrastructure
Event Driven	Always Running
Automatic Scaling	Manual Configuration
Pay Per Execution	Pay for Running Time
AWS Services Learned During Week 1
Service	Purpose
IAM	Identity & Access Management
S3	Object Storage
EC2	Virtual Servers
Lambda	Serverless Computing
Regions	Global Infrastructure
Availability Zones	Fault Tolerance
Edge Locations	Faster Content Delivery
Cloud Practitioner Progress
Completed Topics
Cloud Computing Fundamentals
AWS Overview
AWS Global Infrastructure
Regions
Availability Zones
Edge Locations
Shared Responsibility Model
IAM Fundamentals
Amazon S3
Amazon EC2
AWS Lambda
Topics Remaining
Amazon RDS
Amazon CloudWatch
AWS Billing & Pricing
AWS Security Services
AWS Support Plans
Week 1 Reflection
Key Takeaways
Cloud
Understand AWS global infrastructure.
Understand shared responsibility in cloud security.
Security
IAM is the foundation of AWS security.
Least Privilege is a key security principle.
Storage
S3 provides scalable and durable object storage.
Compute
EC2 provides virtual servers.
Lambda provides serverless computing.
AI/ML Perspective
S3 stores datasets and model artifacts.
EC2 hosts applications and ML solutions.
Lambda automates AI/ML workflows.
Certification Roadmap
Current Goal
AWS Certified Cloud Practitioner
Future Goals
AWS AI Practitioner
AWS Machine Learning Engineer Associate
Progress Tracker
Day 1 - Cloud Fundamentals
Day 2 - Global Infrastructure
Day 3 - Shared Responsibility Model
Day 4 - IAM Fundamentals
Day 5 - Amazon S3
Day 6 - Amazon EC2
Day 7 - AWS Lambda
Week 1 Completion Status
🏆 Week 1 Successfully Completed

AWS Progress
7 / 7 Core Topics Completed

