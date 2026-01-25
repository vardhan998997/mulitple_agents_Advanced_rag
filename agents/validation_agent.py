from tools.credibility import credibility_score
from tools.cross_reference import cross_validate
from tools.contradiction import detect_contradiction


class ValidationAgent:
    def run(self, state):
        validated = []

        for item in state.analysis_results:
            credibility = credibility_score(item["analysis"])
            cross_ref = cross_validate(item["analysis"])
            contradiction = detect_contradiction(item["analysis"])

            confidence = (credibility + cross_ref) / 2
            if contradiction:
                confidence -= 0.2

            validated.append({
                "claim": item["analysis"],
                "confidence": round(confidence, 2)
            })

        state.validated_claims = validated
