# Martialzii LeadFlow

Martialzii LeadFlow is a Streamlit-based lead intake, categorization, onboarding, and payment-assist tool for service businesses. It captures a client's request, classifies the lead, suggests a next action, and prepares the workflow for M-Pesa Daraja billing.

## Features

- Client lead capture form
- Gemini-powered service categorization
- Basic lead scoring and next-action suggestion
- Sensitive-data redaction helpers
- Daraja access-token helper using environment variables
- SOP generation helper for technical reports
- Payment follow-up sentinel

## Project Structure

```text
.
├── leadflow.py          # Main Streamlit app
├── config.py            # Environment-based settings
├── daraja_bridge.py     # Daraja API token helper
├── guardian.py          # Lightweight system monitor
├── scrubber.py          # Sensitive data redaction
├── sentinel.py          # Payment reminder automation
├── sop_genie.py         # SOP generation app/helper
├── requirements.txt
└── .env.example
```

## Setup

1. Create a virtual environment.

```bash
python -m venv .venv
```

2. Activate it.

```bash
.venv\Scripts\activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Create your environment file.

```bash
copy .env.example .env
```

5. Fill in `.env` with your real keys.

## Run

```bash
streamlit run leadflow.py
```

## Important Environment Variables

- `GEMINI_API_KEY`
- `DARAJA_CONSUMER_KEY`
- `DARAJA_CONSUMER_SECRET`
- `DARAJA_ENV`
- `LEADFLOW_EVALUATION_FEE`

## Development Roadmap

1. Add persistent lead storage.
2. Add real Daraja STK Push.
3. Add campaign history.
4. Add admin dashboard metrics.
5. Add tests for scoring, redaction, and Daraja config.
