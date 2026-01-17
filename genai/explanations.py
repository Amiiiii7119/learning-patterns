import os
import requests
from genai.prompts import (
    STUDENT_EXPLANATION_PROMPT,
    INTERVENTION_PROMPT,
    COUNTERFACTUAL_PROMPT
)

OPENROUTER_API_KEY = "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"  # temporary, move to .env later

MODEL = "mistralai/mistral-7b-instruct"

def call_llm(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.4
        }
    )

    return response.json()["choices"][0]["message"]["content"]


def generate_explanation(cluster, risk, features):
    prompt = STUDENT_EXPLANATION_PROMPT.format(
        cluster=cluster,
        risk=risk,
        features=features
    )
    return call_llm(prompt)


def generate_intervention(cluster, risk):
    prompt = INTERVENTION_PROMPT.format(
        cluster=cluster,
        risk=risk
    )
    return call_llm(prompt)


def generate_counterfactual(features):
    prompt = COUNTERFACTUAL_PROMPT.format(
        features=features
    )
    return call_llm(prompt)
