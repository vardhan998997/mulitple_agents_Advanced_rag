class ResearchState:
    def __init__(self, query):
        self.query = query
        self.sub_queries = []
        self.documents = []
        self.analysis_results = []
        self.validated_claims = []
        self.final_report = ""
