from tools.citation import format_citation
from tools.visualization import plot_confidence
from tools.llm import call_llm


class OutputAgent:
    def run(self, state):
        plot_confidence(state.validated_claims)

        summary = call_llm(
            "You are an executive report writer.",
            f"Summarize the following findings:\n{state.validated_claims}"
        )

        report = "EXECUTIVE SUMMARY\n"
        report += summary + "\n\nDETAILED FINDINGS\n"

        for c in state.validated_claims:
            report += f"- {c['claim']} (Confidence: {c['confidence']})\n"

        report += "\nREFERENCES\n"
        report += format_citation("World Bank, IEA")

        state.final_report = report
