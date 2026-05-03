import streamlit as st
import google.generativeai as genai
from fpdf import FPDF

# Configure your API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

class SOP_PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Martialzii Tech Restoration Report', 0, 1, 'C')
        self.ln(5)

def generate_sop(raw_logs):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Transform the following technical logs into a professional Standard Operating Procedure (SOP).
    Structure it with:
    1. Device Model Identification
    2. Problem Statement
    3. Technical Resolution Steps (Bullet points)
    4. Optimization Performed
    
    Raw Logs:
    {raw_logs}
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("SOP-Genie: Tech Doc Automation")
logs = st.text_area("Paste your PowerShell/Command logs here:", height=300)

if st.button("Generate Professional SOP"):
    with st.spinner("Analyzing logs..."):
        formatted_text = generate_sop(logs)
        st.markdown(formatted_text)
        
        # Simple PDF Export logic would go here
        st.success("SOP Generated! You can now copy this to your client report.")