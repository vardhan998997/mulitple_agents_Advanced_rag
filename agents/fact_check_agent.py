
"""
Agent 4: Fact-Checking & Validation Agent

Responsibilities:
- Validate analytical claims
- Check source credibility
- Cross-reference information
- Detect contradictions
- Assign confidence scores
- Enable self-reflection signals
"""

from tools.credibility import credibility_score
from tools.cross_reference import cross_validate
from tools.contradiction import detect_contradiction


class FactCheckAgent:
    def run(self, state):
        validated_claims = []

        for item in state.analysis_results:
            claim_text = item["analysis"]

            # 1. Source credibility check
            credibility = credibility_score(claim_text)

            # 2. Cross-reference validation
            cross_ref_score = cross_validate(claim_text)

            # 3. Contradiction detection
            has_contradiction = detect_contradiction(claim_text)

            # 4. Confidence scoring (simple, explainable formula)
            confidence = (credibility + cross_ref_score) / 2

            if has_contradiction:
                confidence -= 0.2  # penalty for conflicting info

            confidence = round(max(confidence, 0.0), 2)

            validated_claims.append({
                "claim": claim_text,
                "credibility": credibility,
                "cross_reference": cross_ref_score,
                "contradiction": has_contradiction,
                "confidence": confidence
            })

        # Store validated output in shared state
        state.validated_claims = validated_claims

