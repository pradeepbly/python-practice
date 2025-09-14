# python-practice

OOPs Concepts in Python
Here are the main Python OOPs concepts that we will discuss in this tutorial:

Python Class
Python Objects
Inheritance
Polymorphism
Encapsulation
Data Abstraction


https://www.wscubetech.com/resources/python/oops-concepts

Lead Software Engineer (AWS Cloud, Platform Engineering) role is AWS + Platform + DevOps heavy, the Python coding exercises will most likely test:

Basic Python knowledge (OOPs, data structures, error handling).
Automation scripting (AWS SDK – boto3).
Problem-solving ability (loops, conditions, parsing, file handling).
Debugging / optimizing existing code.

They won’t ask hardcore DSA like FAANG, but expect practical coding that shows you can automate AWS tasks and write clean code.

🔹 Python Programs You Might Be Asked in Interview
1. String & List Basics
Reverse a string without using slicing ([::-1]).
Count occurrences of each word in a sentence.
Remove duplicates from a list while preserving order.
Find the second largest number in a list.

2. File Handling & JSON
Read a JSON file of AWS resources and print all S3 bucket names.
Parse a CSV of user data and filter only users from a given region.
Log output to a file with timestamps (basic logging).

4. OOPs Concepts (since JD mentions OOPs)
Write a CloudResource base class and extend it for EC2Instance and S3Bucket.
Implement encapsulation (private attributes for resource IDs).
Show polymorphism (same method create() but different behavior for EC2 vs S3).

4. AWS Automation with boto3 (most relevant for this job)
List all S3 buckets in an AWS account.
Fetch all EC2 instances in a region with their state.
Write a function to start/stop EC2 instances based on tags.
Rotate IAM access keys for a user.
Fetch Route 53 DNS records for a hosted zone.

5. Practical Coding (DevOps/Platform focus)
Given a log file, find the top 5 most common error messages.
Write a Python script to check if an IP is allowed in a WAF rule (given JSON).
Validate if an IAM policy allows only s3:GetObject and nothing else.
Generate a CloudFormation/JSON template dynamically from Python.

6. CI/CD & Testing Angle
Write a function that validates if a given CloudFormation template is JSON/YAML valid.
Unit test a function that checks if an S3 bucket name follows naming convention.
Parse Jenkins build logs and find failed stages.

✅ Example Question They Might Ask You to Code (fits Mastercard’s role):

“Write a Python script that lists all running EC2 instances across multiple regions and saves the details (InstanceId, Name Tag, State, Region) into a CSV file.”

This checks:
boto3 usage
loops & dict handling
file/CSV writing
Python basics
