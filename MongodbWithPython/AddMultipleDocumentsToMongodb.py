import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongoURI = os.getenv("MONGOURI")

client = MongoClient(mongoURI)

#referencing the 'banks' database
db = client.banks

#referencing the 'accounts' collection
accounts_collection = db.accounts

#the insert_many method takes an iterable list of documents
new_accounts = [{
      "accountNumber": "2345678901",
      "accountHolderName": "Jane Smith",
      "accountType": "Checking",
      "balance": 2500.50,
      "branch": "Uptown",
      "createdAt": "2023-02-20T14:30:00Z"
    },
    {
      "accountNumber": "3456789012",
      "accountHolderName": "Alice Johnson",
      "accountType": "Savings",
      "balance": 32000.00,
      "branch": "Midtown",
      "createdAt": "2023-03-10T09:15:00Z"
    },
    {
      "accountNumber": "4567890123",
      "accountHolderName": "Bob Brown",
      "accountType": "Checking",
      "balance": 500.00,
      "branch": "Suburban",
      "createdAt": "2023-04-05T11:45:00Z"
    },
    {
      "accountNumber": "5678901234",
      "accountHolderName": "Carol White",
      "accountType": "Savings",
      "balance": 7800.25,
      "branch": "Rural",
      "createdAt": "2023-05-25T16:00:00Z"
    }]

#the insert_many method returns a result that gives us access to the _id of inserted documents
result = accounts_collection.insert_many(new_accounts)

documentIDs = result.inserted_ids

print(f"The number of inserted documents is: {str(len(documentIDs))}")
print(f"The IDs of the inserted documents are: {documentIDs}")

client.close()