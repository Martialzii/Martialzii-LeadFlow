from __future__ import annotations

import google.generativeai as genai
import streamlit as st

from config import settings


def generate_sop(raw_logs: str) -> str:
    if not settings.gemini_api_key:
        raise RuntimeError("Missing GEMINI_API_KEY in environment.")

    genai.configure(api_key=settings.gemini_api_key)
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
Transform the following technical logs into a professional Standard Operating Procedure (SOP).

Use this structure:
1. Device Model Identification
2. Problem Statement
3. Technical Resolution Steps
4. Optimization Performed

Raw Logs:
{raw_logs}
"""
    response = model.generate_content(prompt)
    return response.text


st.set_page_config(page_title="SOP Genie", page_icon="SG")
st.title("SOP Genie")
logs = st.text_area("Paste PowerShell or command logs here:", height=300)

if st.button("Generate SOP", type="primary"):
    if not logs.strip():
        st.warning("Paste logs before generating an SOP.")
    else:
        with st.spinner("Analyzing logs..."):
            try:
                formatted_text = generate_sop(logs)
            except Exception as exc:
                st.error(str(exc))
            else:
                st.markdown(formatted_text)
                st.success("SOP generated.")
