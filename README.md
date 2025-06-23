Quenzy Question Paper Generator
Setup and Usage Guide

Welcome to Quenzy!
This guide will walk you through the necessary steps to set up and run the Quenzy Question Paper Generator locally. Quenzy leverages AI to help you effortlessly create question papers. Follow the instructions carefully to get started.

1. XAMPP Installation
XAMPP provides an Apache web server, MySQL database, and PHP, which are essential for running Quenzy.

Download XAMPP from the official Apache Friends website: https://www.apachefriends.org/index.html
Choose the appropriate installer for your operating system (Windows, macOS, Linux).
Run the installer and follow the on-screen prompts. It's recommended to install XAMPP in its default directory (e.g., C:\xampp on Windows).
2. Python Installation
Quenzy's AI features are powered by Python. Ensure you have Python installed.

Download Python from the official Python website: https://www.python.org/downloads/
Choose the latest stable version (e.g., Python 3.9 or higher).
Run the installer. Important: Make sure to check "Add Python to PATH" during installation. This makes it easier to run Python commands from your terminal.
Verify installation by opening a command prompt/terminal and typing:
python --version
or
python3 --version
3. Python Library Installation
Install the required Python libraries using pip. These libraries enable AI functionalities, PDF handling, and database connectivity.

pip install google-generativeai PyPDF2 mysql-connector-python python-dotenv
Copy Code
Note: Libraries like os, sys, and datetime are standard Python modules and do not require separate installation.

4. Starting Apache and MySQL
After installing XAMPP, you need to start its services.

Open the XAMPP Control Panel (you can find it in your Start Menu or Applications folder).
In the Control Panel, click the "Start" button next to Apache and MySQL.
Their status indicators should turn green once they are running.
5. Database Setup
You need to create a database for Quenzy and import the provided SQL file.

Open your web browser and navigate to http://localhost/phpmyadmin. This is the phpMyAdmin interface for managing your MySQL databases.
If a database named quenzy already exists, select it from the left sidebar and then click on the "Operations" tab. Under "Remove database", click on "Drop the database (DROP DATABASE)". Confirm the deletion.
On the left sidebar, click on "New" or the "Databases" tab at the top.
Enter quenzy as the database name and click "Create".
Now, select the newly created quenzy database from the left sidebar.
Click on the "Import" tab at the top.
Click "Choose File" and select the quenzy.sql file provided with the application.
Scroll down and click the "Go" button to import the database structure and initial data.
6. Project Directory Structure
After unzipping the Quenzy application files, your project directory structure within C:\xampp\htdocs\ should look like this:


C:\xampp\htdocs\
└── quenzy\
    ├── auth\
    ├── dashboard\
    ├── database\
    ├── assets\
    ├── python_scripts\
    ├── includes\
    ├── quenzy.sql
    ├── index.php
    └── .env
            
Ensure your files and folders are organized as shown above for the application to function correctly.

7. Application Usage: Signup/Login
Once the database is set up and Apache is running, you can access the Quenzy application.

Unzip the Quenzy application files into the htdocs directory inside your XAMPP installation folder (e.g., C:\xampp\htdocs\quenzy).
Open your web browser and go to http://localhost/quenzy (or the specific path if you placed it in a subfolder).
You will be presented with the signup or login page.
If you are a new user, click on "Sign Up" and fill in the required details to create an account.
If you have an existing account (or after signing up), use your credentials to "Log In".
Upon successful login, you will be redirected to the Quenzy dashboard, where you can start generating question papers!
8. AI-Powered Question Generator Details
Quenzy uses advanced AI capabilities to assist you in creating diverse and high-quality question papers.

Intelligent Question Generation: The system can generate questions based on topics, difficulty levels, and question types (e.g., Multiple Choice, Short Answer, Essay) you specify.
Content Analysis: Upload or input text content, and the AI can analyze it to extract key concepts and generate relevant questions.
Customizable Output: You have control over the number of questions, their complexity, and the format of the generated paper.
Review and Edit: All generated questions can be reviewed, edited, or deleted before finalizing your paper.
Efficiency: Significantly reduces the time and effort required to prepare comprehensive question papers.
You're now ready to use Quenzy! Enjoy generating your question papers.

For any issues or feedback, please refer to the Quenzy documentation or support channels.
