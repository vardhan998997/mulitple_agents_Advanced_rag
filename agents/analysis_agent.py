"""
Agent 3: Deep Analysis Agent

Responsibilities:
- Perform comparative analysis
- Detect trends
- Perform causal reasoning
- Run light statistical analysis
- Stay within token / credit limits
"""

from tools.llm import call_llm
from tools.statistics import basic_stats


class AnalysisAgent:
    def run(self, state):
        results = []

        MAX_CHARS = 3000  # Credit-safe input limit

        # Limit number of documents to analyze
        for doc in state.documents[:5]:
            # Trim document to avoid token overflow
            trimmed_doc = doc[:MAX_CHARS]

            # LLM-based deep analysis
            analysis = call_llm(
                system="You are a research analyst.",
                user=f"""
Perform comparative analysis, trend analysis,
and causal reasoning on the following text.
Keep the answer concise and factual.

TEXT:
{trimmed_doc}
"""
            )

            # Simple statistical analysis (lightweight)
            stats = basic_stats(trimmed_doc)

            results.append({
                "analysis": analysis,
                "statistics": stats
            })

        # Save results to shared state
        state.analysis_results = results
