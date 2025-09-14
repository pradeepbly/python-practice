#🟢 Section 1: Basic Python (Core Fundamentals)
#Q1. Reverse a string without using slicing
def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("Mastercard"))  # dra cretsaM

#Q2. Count word occurrences in a sentence
from collections import Counter

def word_count(sentence: str) -> dict:
    words = sentence.lower().split()
    return dict(Counter(words))

print(word_count("AWS Cloud AWS Platform Engineering"))
# {'aws': 2, 'cloud': 1, 'platform': 1, 'engineering': 1}

#Q3. Find the second largest number in a list
def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums[-2] if len(unique_nums) >= 2 else None

print(second_largest([10, 20, 5, 8, 20]))  # 10

#Q4. Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1,2,2,3,4,4,5]))  # [1, 2, 3, 4, 5]

#🟢 Section 2: File Handling & JSON
#Q5. Read JSON and extract all S3 bucket names
import json

data = '''
{
  "Buckets": [
    {"Name": "finance-data"},
    {"Name": "logs-archive"},
    {"Name": "dev-bucket"}
  ]
}
'''

parsed = json.loads(data)
buckets = [bucket["Name"] for bucket in parsed["Buckets"]]
print(buckets)  # ['finance-data', 'logs-archive', 'dev-bucket']

#Q6. Read CSV and filter by region
import csv

def filter_users(file, region):
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        return [row for row in reader if row["Region"] == region]

# Example usage:
print(filter_users("users.csv", "ap-south-1"))

#🟢 Section 3: OOPs in Python
#Q7. CloudResource base class
class CloudResource:
    def __init__(self, name):
        self._name = name  # encapsulation

    def create(self):
        raise NotImplementedError("Subclass must implement create method")

class EC2Instance(CloudResource):
    def create(self):
        return f"EC2 instance '{self._name}' created."

class S3Bucket(CloudResource):
    def create(self):
        return f"S3 bucket '{self._name}' created."

resources = [EC2Instance("web-server"), S3Bucket("logs-data")]
for r in resources:
    print(r.create())

#🟢 Section 4: AWS Automation with boto3

#(These are the most likely interview)

#Q8. List all S3 buckets
import boto3

s3 = boto3.client("s3")
buckets = [bucket["Name"] for bucket in s3.list_buckets()["Buckets"]]
print(buckets)

#Q9. Fetch all EC2 instances with state
import boto3

def list_ec2_instances(region):
    ec2 = boto3.client("ec2", region_name=region)
    instances = ec2.describe_instances()
    result = []
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            result.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"],
                "Type": instance["InstanceType"]
            })
    return result

print(list_ec2_instances("us-east-1"))

#Q10. Start/Stop EC2 instances by tag
import boto3

def stop_instances_by_tag(tag_key, tag_value):
    ec2 = boto3.client("ec2")
    filters = [{"Name": f"tag:{tag_key}", "Values": [tag_value]}]
    instances = ec2.describe_instances(Filters=filters)
    ids = [i["InstanceId"] for r in instances["Reservations"] for i in r["Instances"]]
    if ids:
        ec2.stop_instances(InstanceIds=ids)
        print(f"Stopped: {ids}")
    else:
        print("No matching instances found")

# stop_instances_by_tag("Environment", "Dev")

#Q11. Export EC2 details across multiple regions to CSV
import boto3
import csv

def export_ec2_to_csv(filename="ec2_report.csv"):
    regions = [r["RegionName"] for r in boto3.client("ec2").describe_regions()["Regions"]]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["InstanceId", "Name", "State", "Region"])
        
        for region in regions:
            ec2 = boto3.client("ec2", region_name=region)
            reservations = ec2.describe_instances()["Reservations"]
            for res in reservations:
                for inst in res["Instances"]:
                    name = ""
                    for tag in inst.get("Tags", []):
                        if tag["Key"] == "Name":
                            name = tag["Value"]
                    writer.writerow([inst["InstanceId"], name, inst["State"]["Name"], region])

export_ec2_to_csv()

#🟢 Section 5: Practical DevOps/Platform Tasks
#Q12. Parse log file and find top 5 errors
from collections import Counter

def top_errors(logfile):
    with open(logfile, "r") as f:
        errors = [line.strip() for line in f if "ERROR" in line]
    return Counter(errors).most_common(5)

# print(top_errors("app.log"))

#Q13. Validate IAM policy only allows s3:GetObject
import json

def validate_policy(policy_json):
    policy = json.loads(policy_json)
    for stmt in policy["Statement"]:
        if stmt["Effect"] == "Allow":
            if stmt["Action"] != "s3:GetObject":
                return False
    return True

policy = '''
{
  "Version": "2012-10-17",
  "Statement": [
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "*"}
  ]
}
'''

print(validate_policy(policy))  # True

#Q14. Check if IP allowed in WAF rule (from JSON)
import json

def is_ip_allowed(ip, waf_json):
    data = json.loads(waf_json)
    allowed_ips = data.get("AllowedIPs", [])
    return ip in allowed_ips

waf_config = '{"AllowedIPs": ["10.0.0.1", "192.168.1.10"]}'
print(is_ip_allowed("10.0.0.1", waf_config))  # True

#🟢 Section 6: CI/CD & Testing
#Q15. Unit test a function that validates S3 bucket name
import re
import unittest

def is_valid_bucket_name(name: str) -> bool:
    return bool(re.match(r"^[a-z0-9.-]{3,63}$", name))

class TestBucketName(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_bucket_name("my-bucket"))
    def test_invalid(self):
        self.assertFalse(is_valid_bucket_name("Invalid_Bucket"))

unittest.main(argv=[''], exit=False)



'''
5. String Formatting
You often need to insert variables into a string. F-strings (formatted string literals) are the modern and most readable way to do this.
'''
name = "Alice"
age = 30
# The 'f' at the start indicates an f-string
message = f"Hello, my name is {name} and I am {age} years old."
print(message) # Output: "Hello, my name is Alice and I am 30 years old."


'''
4. Splitting and Joining Strings
These operations are crucial for parsing text. The split() method breaks a string into a list of substrings, and the join() method does the opposite
'''
my_string = "apple,banana,cherry"
# Split the string by the comma delimiter
fruits_list = my_string.split(',')
print(fruits_list) # Output: ['apple', 'banana', 'cherry']

# Join the list elements back into a string with a space
new_string = ' '.join(fruits_list)
print(new_string) # Output: "apple banana cherry"


'''
3. Palindrome Check
A palindrome is a word or phrase that reads the same forwards and backward. 
You can check this by comparing the original string with its reversed version.
'''

word = "madam"
# Convert the word to lowercase for a case-insensitive check
word = word.lower()

# Check if the word is equal to its reversed version
if word == word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

'''
Counting Vowels and Consonants
This program iterates through a string and checks each character
'''
sentence = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha(): # Check if the character is an alphabet
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)      # Output: Vowels: 3
print("Consonants:", consonant_count) # Output: Consonants: 7


'''
2. Common String Programs and Logic
Reversing a String
This is a classic problem. The simplest way is using string slicing.
'''
my_string = "Python"
reversed_string = my_string[::-1]
print(reversed_string) # Output: "nohtyP"



'''
1. Basic OperationsCreating a String:
'''
my_string = "Hello, Python!"

'''
Accessing Characters:
Strings are like arrays of characters, so you can access them by index.
'''
    
first_char = my_string[0]  # Output: 'H'
last_char = my_string[-1]   # Output: '!'
Slicing a String:
You can extract a substring using slicing [start:end:step].

# Get a substring from index 0 to 4 (exclusive)
substring1 = my_string[0:5] # Output: "Hello"

# Get a substring from index 7 to the end
substring2 = my_string[7:]  # Output: "Python!"

# Reverse the string
reversed_string = my_string[::-1] # Output: "!nohtyP ,olleH"


'''2. Common String Programs and Logic
Reversing a String
This is a classic problem. The simplest way is using string slicing.

Python
'''
my_string = "Python"
reversed_string = my_string[::-1]
print(reversed_string) # Output: "nohtyP"
Alternatively, you can use a loop or the reversed() function combined with ''.join().
