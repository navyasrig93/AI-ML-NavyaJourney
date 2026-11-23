AWS Learning Journey
Week 2 - Day 1
Student
Navya

Topic
Amazon RDS (Relational Database Service)

Learning Objective
Understand:

Relational Databases
Amazon RDS
Managed Database Services
RDS Benefits
Database Engines Supported by AWS
RDS vs EC2
What is Amazon RDS?
Amazon Relational Database Service (RDS) is a managed database service provided by AWS.

It allows users to create, operate, and scale relational databases without managing underlying server infrastructure.

AWS handles most administrative tasks such as:

Backups
Software Patching
Monitoring
High Availability
Infrastructure Management
Why RDS is Used
Traditionally, database administrators are responsible for:

Installing databases
Performing upgrades
Taking backups
Managing storage
Configuring replication
With RDS, AWS automates these tasks.

Supported Database Engines
Amazon RDS supports:

MySQL
Open-source relational database.

PostgreSQL
Advanced open-source relational database.

MariaDB
Community-developed MySQL alternative.

Microsoft SQL Server
Enterprise relational database from Microsoft.

Oracle Database
Enterprise-grade database platform.

Key Features of Amazon RDS
Automated Backups
AWS automatically creates database backups.

Benefits
Disaster recovery
Data protection
Point-in-time recovery
Automated Patching
AWS applies database updates and security patches.

Benefits
Improved security
Reduced administration effort
Scalability
Storage and compute resources can be adjusted as business requirements grow.

Benefits
Improved performance
Business flexibility
High Availability
Multi-AZ deployments improve reliability.

Benefits
Reduced downtime
Better fault tolerance
Amazon RDS Architecture
Application
      │
      ▼
 Amazon RDS
      │
      ▼
 Managed Database
AWS manages the infrastructure while users focus on the database and applications.

Amazon RDS vs EC2
EC2 Database Setup
User Responsibilities

Install Database
Configure Database
Manage Backups
Apply Updates
Monitor Infrastructure
Amazon RDS
AWS Responsibilities

Installation
Patching
Backups
Monitoring
Infrastructure Management
Comparison Table
Feature	Amazon RDS	Database on EC2
Installation	AWS Managed	Customer Managed
Backups	Automated	Manual
Patching	Automated	Manual
Monitoring	Built-In	Customer Managed
Administrative Effort	Low	High
Scalability	Easy	Manual
Why RDS is Important for AI/ML
Machine Learning solutions depend on reliable data sources.

RDS can store:

Customer Information
Transaction Data
Product Catalogs
Application Data
Features for Machine Learning Models
AI/ML Workflow Example
Amazon RDS
        ↓
SQL Queries
        ↓
Python / Pandas
        ↓
Data Cleaning
        ↓
Machine Learning Model
Key Learning Points
✅ RDS is a managed relational database service

✅ AWS manages backups, patching, and infrastructure

✅ RDS supports multiple database engines

✅ RDS reduces database administration effort

✅ RDS is commonly used as a structured data source for analytics and machine learning

Certification Notes
Important Cloud Practitioner Concepts
Difference between:

Amazon EC2
Virtual servers.

Customer manages operating systems and database software.

Amazon RDS
Managed database service.

AWS manages database infrastructure and maintenance.

Day 1 Reflection
What I Learned
How managed databases simplify administration
Benefits of automated backups
Differences between EC2 and RDS
How databases support AI/ML workflows
Why relational databases remain important in modern cloud architectures
AWS Progress Tracker
Week 1
Cloud Computing Fundamentals
AWS Global Infrastructure
Shared Responsibility Model
IAM Fundamentals
Amazon S3
Amazon EC2
AWS Lambda
Week 2
Day 1 - Amazon RDS
Day 2 - CloudWatch
Day 3 - AWS Billing & Pricing
Day 4 - AWS Security Services
Day 5 - AWS Databases Deep Dive
Cloud Practitioner Readiness
~70% Complete

Created by: Navya
AWS Certification & AI/ML Engineer Learning Journey
