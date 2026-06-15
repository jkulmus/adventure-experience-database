# Overview

As a software development student, I am continuing to build a personal software portfolio that demonstrates my growth in programming concepts and software development practices, and cloud technologies. This project is a Python-based Adventure Experience Database Manager that uses Google Firebase Firestore to store and manage adventure experience data in a cloud database

The software demonstrates sever core TypeScript concepts including:
- Cloud database connectivity
- Firestore collections and documents
- Create operations
- Read operations
- Update operations
- Delete operations
- Related collections
- Service account authentication

My program stores adventure experiences and categories in a Firestore database and demonstrates full CRUD (Create, Read, Update, Delete) functionality. The application connects to a cloud-hosted database, inserts records, retrieves stored data, updates existing records, and removes records when no longer needed.

The purpose of this project is to learn then strengthen my understanding of cloud databases, NoSQL data storage, Firebase configuration, and cloud-based application development while continuing to build software that could support larger future apps.


[Software Demo Video](https://youtu.be/WrLdDscoa1g)

# Development Environment

I used Visual Studio Code as my primary code editor and GitHub to publish my project to a public repository. 

This project was developed using:
- Python
- Google Firebase
- Cloud Firestore
- Firebase Admin SDK
- GitHub

My application runs in the terminal using Python and connects to a cloud-hosted Firestore database

# Useful Websites

* [Firebase Documentation](https://firebase.google.com/docs)
* [Cloud Firestore Docs](https://firebase.google.com/docs/firestore)
* [Firebase Console](https://console.firebase.google.com/)
* [Firebase Admin SDK for Python](https://firebase.google.com/docs/admin/setup)
* [Python Tutorial](https://docs.python.org/3/tutorial/)
* [Firestore Add Data Docs](https://firebase.google.com/docs/firestore/manage-data/add-data)


# Features

- Cloud-hosted Firestore database
- Adventure experience collection
- Category collection
- Create database records
- Read database records
- Update existing records
- Delete records
- Related collection structure using category ids
- Firebase service account authentication
- Terminal-based CRUD demonstration

# How to Run the Program

1. Download or clone the respoistory
2. Open the project folder in Visual Studio Code
3. Create a Firebase project and Firestore database
4. Download a Firebase service account key
5. Rename the file to serviceAccountKey.json
6. Place the file in the root project folder
7. Install dependencies
python -m pip install firebase-admin
8. Run the program:
python main.py


# Future Plans

In the future, I would like to add:
- Add user input instead of predefined records
- Build a menu-driven interface
- Add additional adventure categories
- Connect the database to a web application
- Implement user authentication
- Expand the database structure to support larger applications

# Time Spent

I spent approximately 17 hours researching Firebase and Firestore, configuring the cloud database, installing and configuring Python, implementing CRUD functionality, testing database operations, troubleshooting connection issues, documenting the project, and preparing the final submission.

# Learning Strategies

- Breaking the project into smaller components and test each step individually
- Verify database operations directly within the Firebase Console
- Using official Firebase documents to understand Firebase collections and documents
- Troubleshooting one problem at a time instead of changing multiple things are once
- Building and testing CRUD operations incrementally

# Challenges and Improvements

One major challenge was learning how to connect Python to cloud-hosted Firestore database and correctly configure Firebase authentication. I overcame this by following the official Firebase docs, testing the database connection first, and then implementing each CRUD operation one at a time.
Another challene was understanding how Firestore organizes information into collections an docs. I overcame this by creating sample categories and adventure experiences and verifying each operation inside the Firebase Console

# Stretch Challenge

For the stretch challenge, I created two related Firestore collections: categories and experience. Each experience document includes a category_id that links it to a category document. This demonstrates how related data can be organzied within a NoSQL cloud database structure.