# github-demo

Simple Python LLM chat app using GitHub Models, OpenAI SDK, and Streamlit.

## Prerequisites

- Python 3.10+
- A GitHub token with access to GitHub Models

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
cp .env.example .env
```

Then set `GITHUB_TOKEN` in `.env`.

## Run

```bash
streamlit run web.py
```

The app includes:
- A text input for your prompt
- A submit button
- Default prompt: "Tell me a dad joke today"