#AI-Pharma

Project Overview: AI-Pharma is an AI-powered platform designed to analyze prescriptions and recommend medicines. It leverages Google Vision API and machine learning to extract and interpret handwritten prescriptions, improving accuracy and reducing prescription errors.


Features

✅ AI-based prescription text extraction

✅ AI-driven medicine recommendations

✅ Secure, HIPAA-compliant data processing

✅ User-friendly dashboard for insights


Tech Stack
Programming Language: Python
Libraries & Frameworks: Streamlit, OpenCV, Pandas, NumPy, Google Cloud Vision API
Cloud Services: Google Cloud Platform (GCP), Firebase


🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/AI-Pharma.git
cd AI-Pharma
2️⃣ Set Up a Virtual Environment
python3 -m venv env
source env/bin/activate  # On Windows: `env\Scripts\activate`
3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Setting Up Google Cloud Vision API


To use Google Vision API, you must set up your own credentials:
1️⃣ Create Google Cloud Credentials
Go to Google Cloud Console
Enable Vision API in your Google Cloud project
Create a Service Account and download the service_account.json file
Do not upload this file to GitHub!
2️⃣ Store Credentials Locally
Move service_account.json into a secure folder on your system (not in the repo).
Set up authentication using:
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json"
Or, in Python:
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/service_account.json"


🚀 Running the Project
Once setup is complete, run: streamlit run app.py
This will launch AI-Pharma in your web browser.


🔐 Security & Secrets Management
❌ Never upload service_account.json to GitHub
✅ Each user must download their own credentials and upload it in the credentials folder


🛠 Troubleshooting
1️⃣ Error: 401 Unauthenticated
✔ Ensure your service_account.json is correct
✔ Verify GOOGLE_APPLICATION_CREDENTIALS is set

2️⃣ Module Not Found
Run:
pip install -r requirements.txt
3️⃣ Streamlit Not Launching
✔ Activate virtual environment
✔ Run streamlit run app.py from project root
