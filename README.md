# mulitple_agents_Advanced_rag

🧠 Deep Research Assistant
Overview

The Deep Research Assistant is a multi-agent AI system that answers complex research queries using real web scraping, retrieval-augmented generation (RAG), and GPT-4.1 based reasoning.
It is designed with clear orchestration, modular agents, and validation layers to ensure reliable and explainable outputs.

Architecture
User Query
   ↓
Research Coordinator (Orchestrator)
   ↓
Web & Retrieval Agent (RAG)
   ↓
Deep Analysis Agent (LLM)
   ↓
Fact-Checking Agent
   ↓
Output Formatting Agent
   ↓
Final Research Report + Confidence Graph

Agents

Research Coordinator – Decomposes queries, manages execution, and synthesizes results

Web & Retrieval Agent – Scrapes trusted websites and builds the RAG knowledge base

Deep Analysis Agent – Performs comparative, trend, and causal analysis using GPT-4.1

Fact-Checking Agent – Validates claims, detects contradictions, and assigns confidence scores

Output Agent – Generates structured reports, summaries, and visualizations

Key Features

Real web scraping (World Bank, IEA, etc.)

Advanced RAG with chunking and indexing

Multi-hop reasoning across documents

Confidence-based validation to reduce hallucinations

MCP-style tool abstraction

Token and credit-safe LLM usage

Tech Stack

Python

GPT-4.1 (via OpenRouter)

requests, beautifulsoup4

scikit-learn

matplotlib

python-dotenv

How to Run
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Example Query
How did COVID-19 impact renewable energy investment patterns in developing countries, 
and what regulatory changes emerged as a result across different regions?

Output

Structured research report

Executive summary

Confidence score visualization

Notes

The system uses real web data but processes only relevant chunks (RAG best practice).

The architecture is extensible and production-ready in design.


import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system, user):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1"),
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        temperature=0.3,
        max_tokens=800
    )
    return response.choices[0].message.content


