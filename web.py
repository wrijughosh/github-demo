import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_MODEL = os.getenv("GITHUB_MODEL", "gpt-4o-mini")
GITHUB_BASE_URL = os.getenv("GITHUB_BASE_URL", "https://models.inference.ai.azure.com")


def get_client() -> OpenAI:
    if not GITHUB_TOKEN:
        raise ValueError("GITHUB_TOKEN is not set. Add it to your environment or .env file.")

    return OpenAI(
        base_url=GITHUB_BASE_URL,
        api_key=GITHUB_TOKEN,
    )


def get_completion(prompt: str) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model=GITHUB_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content or "No response from model."


st.set_page_config(page_title="GitHub Models Chat Demo", page_icon="💬")
st.title("GitHub Models Chat Demo")
st.write("Enter a prompt and get a response from the model.")

with st.form("chat_form"):
    prompt = st.text_input("Prompt", value="Tell me a dad joke today")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Calling model..."):
            try:
                answer = get_completion(prompt)
                st.subheader("Response")
                st.write(answer)
            except Exception as exc:  # noqa: BLE001
                st.error(f"Request failed: {exc}")
