_**CuraAI**_
----------------------
Project Overview: CuraAI is an AI-powered platform designed to analyze prescriptions and recommend medicines. It leverages Google Vision API and machine learning to extract and interpret handwritten prescriptions, improving accuracy and reducing prescription errors.


**Features**

✅ AI-based prescription text extraction

✅ AI-driven medicine recommendations

✅ Secure, HIPAA-compliant data processing

✅ User-friendly dashboard for insights



**Tech Stack**

Programming Language: Python

Libraries & Frameworks: Streamlit, OpenCV, Pandas, NumPy, Google Cloud Vision API

Cloud Services: Google Cloud Platform (GCP), Firebase



**Installation & Setup**

1. _Clone the Repository_

- git clone https://github.com/YOUR_USERNAME/AI-Pharma.git

- cd AI-Pharma


2. _Set Up a Virtual Environment_

- python3 -m venv env

- source env/bin/activate  # On Windows: `env\Scripts\activate`


3. _Install Dependencies_
   
- pip install -r requirements.txt



**Setting Up Google Cloud Vision API**

To use Google Vision API, you must set up your own credentials:

1️ **Create Google Cloud Credentials**

- Go to Google Cloud Console

- Enable Vision API in your Google Cloud project

- Create a Service Account and download the service_account.json file

- Do not upload this file to GitHub!

2️ **Store Credentials Locally**

- Move service_account.json into a secure folder on your system (not in the repo).

- Set up authentication using:

- export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json"

- Or, in Python:

- import os

- os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/service_account.json"



**Running the Project**

- Once setup is complete, run: streamlit run app.py

- This will launch AI-Pharma in your web browser.

- You can navigate using the sidebar in the website.

- In the Upload Analyze page, you can browse documents and add one of the prescriptions availabe in the assets file

- After analysing it will extract the text 




**Security & Secrets Management**

- Never upload service_account.json to GitHub

- Each user must download their own credentials and upload it in the credentials folder



**Troubleshooting**

1️_Error: 401 Unauthenticated_

- Ensure your service_account.json is correct

- Verify GOOGLE_APPLICATION_CREDENTIALS is set


2️ _**Module Not Found**_

- Run: pip install -r requirements.txt


3️ _**Streamlit Not Launching**_

- Activate virtual environment

- Run streamlit run app.py from project root
