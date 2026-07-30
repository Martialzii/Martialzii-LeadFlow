from __future__ import annotations

import google.generativeai as genai
import streamlit as st

from config import settings
from scrubber import redact_sensitive_data


SERVICE_CATEGORIES = ("Hardware", "Software", "Fintech", "Other")


def configure_gemini(api_key_override: str = "") -> bool:
    api_key = api_key_override or settings.gemini_api_key
    if not api_key:
        return False
    genai.configure(api_key=api_key)
    return True


def categorize_service_request(service_request: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
Categorize this service request as exactly one of: Hardware, Software, Fintech, Other.
Return only the category.

Request:
{service_request}
"""
    response = model.generate_content(prompt)
    category = response.text.strip()
    return category if category in SERVICE_CATEGORIES else "Other"


def score_lead(service_request: str, contact: str) -> int:
    score = 30

    if len(service_request.strip()) >= 40:
        score += 25
    if any(word in service_request.lower() for word in ("urgent", "today", "asap", "broken")):
        score += 20
    if contact.strip():
        score += 15
    if any(word in service_request.lower() for word in ("pay", "budget", "quote", "invoice")):
        score += 10

    return min(score, 100)


def next_action_for_score(score: int) -> str:
    if score >= 80:
        return "Call immediately and send evaluation fee request."
    if score >= 55:
        return "Send qualification message and schedule consultation."
    return "Ask for more details before billing."


st.set_page_config(page_title="Martialzii LeadFlow", page_icon="LF")
st.title("Martialzii LeadFlow")
st.subheader("Automated Client Onboarding and Billing")

with st.sidebar:
    api_key_override = st.text_input(
        "Gemini API Key override",
        type="password",
        help="Optional. Prefer GEMINI_API_KEY in your .env file.",
    )
    st.metric("Evaluation Fee", f"KES {settings.evaluation_fee}")

with st.form("lead_form"):
    client_name = st.text_input("Client Name / Business")
    contact = st.text_input("Phone Number (M-Pesa)")
    service_request = st.text_area(
        "Describe the service needed",
        placeholder="Example: Laptop repair, Flutter app, payment integration, website fix...",
    )
    submit = st.form_submit_button("Submit Request", type="primary")

if submit:
    if not client_name.strip() or not contact.strip() or not service_request.strip():
        st.warning("Fill in the client name, phone number, and service request.")
    elif not configure_gemini(api_key_override):
        st.error("Add GEMINI_API_KEY to .env or enter it in the sidebar.")
    else:
        with st.spinner("Classifying lead..."):
            try:
                category = categorize_service_request(service_request)
            except Exception as exc:
                st.error(f"AI categorization failed: {exc}")
                category = "Other"

        lead_score = score_lead(service_request, contact)
        next_action = next_action_for_score(lead_score)

        st.success(f"Lead captured. Category: {category}")

        left, middle, right = st.columns(3)
        left.metric("Lead Score", f"{lead_score}/100")
        middle.metric("Category", category)
        right.metric("Evaluation Fee", f"KES {settings.evaluation_fee}")

        st.info(next_action)
        st.caption("Redacted lead preview for logs:")
        st.code(
            redact_sensitive_data(
                f"Client={client_name}; Phone={contact}; Request={service_request}; Category={category}"
            )
        )

        st.write("M-Pesa STK Push is ready for Daraja integration.")
