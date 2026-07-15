"""
RAG Service

Enterprise Knowledge Retrieval Service.
"""

from __future__ import annotations

from tools.rag.rag_tool import (
    list_corpora,
    create_corpus,
    get_corpus,
    delete_corpus,
    upload_file,
    import_files,
    list_files,
    delete_file,
    search_knowledge,
)


class RAGService:

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Corpus
    # ---------------------------------------------------------

    def corpora(self):

        return list_corpora()

    def create(

        self,

        display_name: str = "followup-agent-rag",

    ):

        return create_corpus(

            display_name,

        )

    def get(

        self,

        corpus_name: str,

    ):

        return get_corpus(

            corpus_name,

        )

    def delete(

        self,

        corpus_name: str,

    ):

        return delete_corpus(

            corpus_name,

        )

    # ---------------------------------------------------------
    # Files
    # ---------------------------------------------------------

    def upload(

        self,

        corpus_name: str,

        file_path: str,

    ):

        return upload_file(

            corpus_name,

            file_path,

        )

    def import_documents(

        self,

        corpus_name: str,

        paths: list[str],

    ):

        return import_files(

            corpus_name,

            paths,

        )

    def files(

        self,

        corpus_name: str,

    ):

        return list_files(

            corpus_name,

        )

    def remove_file(

        self,

        file_name: str,

    ):

        return delete_file(

            file_name,

        )

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

    def search(

        self,

        corpus_name: str,

        query: str,

        top_k: int = 5,

    ):

        return search_knowledge(

            corpus_name,

            query,

            top_k,

        )

    # ---------------------------------------------------------
    # Customer Context
    # ---------------------------------------------------------

    def customer_context(

        self,

        corpus_name: str,

        customer: str,

    ):

        query = f"""
Customer: {customer}

Retrieve:

- Previous proposals
- Meeting notes
- Contracts
- Technical discussions
- Implementation documents
- Support history
"""

        return self.search(

            corpus_name,

            query,

        )