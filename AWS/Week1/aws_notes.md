AWS Learning Journey - Week 1
Goal
Build a strong AWS foundation while preparing for:

AWS Certified Cloud Practitioner
AWS AI Practitioner
AWS Machine Learning Engineer Associate
Week 1 Learning Summary
During Week 1, I learned the foundational concepts of AWS Cloud, Security, IAM, and Amazon S3.

Day 1 - Cloud Fundamentals
Topics Learned
What is Cloud Computing
Benefits of Cloud Computing
What is AWS
Key Learnings
Cloud Computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing.

Benefits
Cost Savings
Scalability
Flexibility
Reliability
Day 2 - AWS Global Infrastructure
Topics Learned
AWS Regions
Availability Zones
Edge Locations
Region
A physical geographic location where AWS operates data centers.

Availability Zone
One or more isolated data centers within a Region.

Edge Location
Locations used by AWS services to deliver content closer to users.

Key Learning
Applications can be deployed across multiple Availability Zones to improve availability and fault tolerance.

Day 3 - Shared Responsibility Model
Topics Learned
Security of the Cloud
Security in the Cloud
AWS Responsibilities
AWS manages:

Physical Data Centers
Hardware
Networking Infrastructure
Physical Security
Customer Responsibilities
Customers manage:

Applications
Data
IAM Configuration
User Permissions
Passwords
Encryption
Key Learning
Security in AWS is a shared responsibility between AWS and the customer.

Day 4 - IAM (Identity and Access Management)
Topics Learned
IAM Users
IAM Groups
IAM Policies
Root User
IAM User
An individual identity that can access AWS resources.

Examples:

Developers
Administrators
Applications
IAM Group
A collection of IAM users with similar permissions.

Examples:

Developers
QA Team
Administrators
IAM Policy
A set of permissions that determines what actions are allowed or denied.

Examples:

Read S3 Buckets
Launch EC2 Instances
Access CloudWatch
Root User
The root account has complete administrative access to the AWS account.

Best Practice
Enable MFA
Avoid using Root User for daily work
Create IAM users for normal access
Day 5 - Amazon S3
Topics Learned
S3 Basics
Buckets
Objects
S3 Use Cases
S3 for AI/ML
What is Amazon S3?
Amazon Simple Storage Service (S3) is a scalable object storage service used to store and retrieve data from anywhere.

Key Concepts
Bucket
A storage container used to organize objects.

Example:

navya-ml-project-data
Object
A file stored within a bucket.

Examples:

resume.pdf
customer_data.csv
image.jpg
Benefits of S3
High Durability
Scalability
Security
Cost Efficiency
S3 Use Cases
Backup and Recovery
Store backups for disaster recovery.

Application Data Storage
Store images, videos, reports, and documents.

Big Data Analytics
Store large datasets for processing and analysis.

Machine Learning
Store:

Training Data
Validation Data
Model Artifacts
Logs
Why S3 Matters for AI/ML
Amazon S3 acts as a centralized data lake for:

Structured Data
Unstructured Data
Datasets
Images
Videos
ML Models
Training Outputs
Most AWS AI and Machine Learning services integrate directly with S3.

AWS Services Learned So Far
Service	Purpose
IAM	Identity and Access Management
S3	Object Storage
Regions	Geographic Infrastructure
Availability Zones	High Availability Infrastructure
Edge Locations	Content Delivery Infrastructure
Cloud Practitioner Progress
Completed Topics
Cloud Computing Fundamentals
AWS Fundamentals
AWS Regions
Availability Zones
Edge Locations
Shared Responsibility Model
IAM Fundamentals
Amazon S3 Fundamentals
Upcoming Topics
Amazon EC2
AWS Lambda
Amazon RDS
CloudWatch
Billing and Pricing
Security Services
Week 1 Reflection
Key Takeaways
AWS infrastructure is designed for scalability and fault tolerance.
Security is shared between AWS and customers.
IAM is the foundation of AWS security.
S3 is one of the most widely used AWS services.
Cloud concepts form the foundation for AI, Machine Learning, and modern application development.
Certification Roadmap
Current Goal
AWS Certified Cloud Practitioner
Future Certifications
AWS AI Practitioner
AWS Machine Learning Engineer Associate
Progress Tracker
Day 1 - Cloud Fundamentals
Day 2 - Global Infrastructure
Day 3 - Shared Responsibility Model
Day 4 - IAM Fundamentals
Day 5 - Amazon S3
Week 1 Completion
AWS Progress: 5 / 5 Topics Completed

Cloud Practitioner Readiness: ~50%

Last Updated: November 2026
