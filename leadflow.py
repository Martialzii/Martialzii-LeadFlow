import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
import datetime

# Martialzii Branding
st.set_page_config(page_title="Martialzii LeadFlow", page_icon="📈")
st.title("📈 Martialzii LeadFlow")
st.subheader("Automated Client Onboarding & Billing")

# Sidebar for API Key (Secure)
with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key", type="password")
    if api_key:
        genai.configure(api_key=api_key)

# 1. Lead Capture Form
with st.form("lead_form"):
    client_name = st.text_input("Client Name / Business")
    contact = st.text_input("Phone Number (M-Pesa)")
    service_request = st.text_area("Describe the service you need (e.g., Laptop repair, Flutter App)")
    submit = st.form_submit_button("Submit Request")

if submit and api_key:
    # 2. AI Lead Categorization
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Categorize this service request into 'Hardware', 'Software', or 'Fintech'. Request: {service_request}"
    response = model.generate_content(prompt)
    category = response.text.strip()
    
    st.success(f"Lead Captured! Category: **{category}**")

    # 3. Simulated M-Pesa STK Push
    st.info(f"Simulating STK Push to {contact} for {category} evaluation fee...")
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/15/M-Pesa_logo.png", width=100)