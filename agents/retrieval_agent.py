from tools.web_search import web_search
from tools.scraper import scrape
from rag.chunking import semantic_chunk
from rag.indexing import build_index
from rag.retriever import retrieve_chunks


class RetrievalAgent:
    def run(self, state):
        all_chunks = []

        for q in state.sub_queries:
            urls = web_search(q)
            for url in urls:
                text = scrape(url)
                chunks = semantic_chunk(text)
                all_chunks.extend(chunks)

        index = build_index(all_chunks)
        state.documents = retrieve_chunks(index)
