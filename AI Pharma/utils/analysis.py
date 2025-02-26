import pandas as pd

# Sample medical data (You can expand this)
medicine_db = {
    "Paracetamol": {"Usage": "Pain relief, fever", "Dosage": "500mg", "Warnings": "Liver damage in overdose"},
    "Ibuprofen": {"Usage": "Inflammation, pain", "Dosage": "200mg", "Warnings": "Avoid in kidney disease"},
    "Aspirin": {"Usage": "Blood thinner, pain", "Dosage": "81mg", "Warnings": "Risk of stomach bleeding"},
}

def analyze_prescription(text):
    """Analyzes extracted text for medicine details and potential warnings."""
    detected_medicines = {}
    
    for med, details in medicine_db.items():
        if med.lower() in text.lower():
            detected_medicines[med] = details
    
    if not detected_medicines:
        return "No known medicines detected."
    
    return pd.DataFrame(detected_medicines).T
