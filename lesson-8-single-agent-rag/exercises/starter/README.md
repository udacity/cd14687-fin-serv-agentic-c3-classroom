# Exercise: Single Agent RAG - Banking Policy Assistant

In this exercise, you will build a single-agent RAG system designed to act as a banking policy assistant. Your goal is to create an intelligent agent that can retrieve policy information from a local Chroma vector store, provide accurate answers with citations, and, most importantly, autonomously decide when to search again if the initial results are insufficient. This system will support a bank's customer service team by giving them instant access to information on fees, limits, and procedures.

### Prerequisites

*   Understanding of Retrieval-Augmented Generation (RAG) concepts.
*   Familiarity with the OpenAI API for chat completions.
*   Basic knowledge of vector stores like ChromaDB.
*   Proficiency in Python, including the use of dataclasses.

### Instructions

1.  **Define Response Data Model**: In the `SimpleRAGResponse` dataclass, define fields to structure the agent's response, including the query, answer, sources, retrieval metrics, retry status, and confidence level.

2.  **Load Documents to Chroma**: Implement `load_banking_documents_to_chroma`. Initialize a ChromaDB client and collection, read text files from the data directory, split them into chunks, and add them to the collection with embeddings and metadata.

3.  **Implement Text Splitting**: Implement `split_text_into_chunks` to divide text into overlapping chunks of a specified size to optimize retrieval.

4.  **Implement Embedding Helper**: Create a `get_embedding` function to generate vector embeddings for text using the OpenAI API.

5.  **Retrieve Documents**: Implement the `retrieve_documents` method in `SimpleRAGAgent` to query the Chroma collection for relevant documents based on a user query.

6.  **Generate Answer**: Implement `ask_llm_for_answer`. Construct a prompt with retrieved context and the user's query, then call the OpenAI API to generate an answer based strictly on the provided documents.

7.  **Evaluate Need for Retry**: Implement `should_retry_retrieval`. Use the LLM to evaluate if the initial answer is sufficient or if more information is needed, returning a boolean decision.

8.  **Improve Search Query**: Implement `generate_better_search_query`. If a retry is needed, use the LLM to generate a more specific search query based on the initial attempt's shortcomings.

9.  **Assess Confidence**: Implement `assess_confidence` to determine a confidence level (high, medium, low) based on the answer quality and retrieval metrics.

10. **Orchestrate Workflow**: Implement `process_query` to tie everything together: initial retrieval, answer generation, autonomous retry logic (if needed), final answer generation, confidence assessment, and response formatting.

11. **Test and Analyze**: Run the provided test scenarios (standard queries, ambiguous queries requiring re-retrieval, and out-of-scope queries) to verify the agent's autonomous behavior and analyze its performance metrics.