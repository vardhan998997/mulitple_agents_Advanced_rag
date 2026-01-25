from core.state import ResearchState
from core.task_manager import prioritize
from core.progress_tracker import log

from agents.retrieval_agent import RetrievalAgent
from agents.analysis_agent import AnalysisAgent
from agents.validation_agent import ValidationAgent
from agents.output_agent import OutputAgent


class ResearchCoordinator:
    def __init__(self):
        self.retrieval = RetrievalAgent()
        self.analysis = AnalysisAgent()
        self.validation = ValidationAgent()
        self.output = OutputAgent()

    def decompose_query(self, query):
        return [
            "COVID-19 economic impacts on developing countries",
            "Renewable energy investment trends 2019-2023",
            "Regional renewable energy regulations",
            "Economic disruption vs energy policy changes",
            "Geographic variation in policy responses"
        ]

    def run(self, query):
        state = ResearchState(query)

        log("Decomposing query")
        state.sub_queries = prioritize(self.decompose_query(query))

        log("Retrieving documents")
        self.retrieval.run(state)

        log("Analyzing documents")
        self.analysis.run(state)

        log("Validating claims")
        self.validation.run(state)

        log("Formatting output")
        self.output.run(state)

        return state.final_report
