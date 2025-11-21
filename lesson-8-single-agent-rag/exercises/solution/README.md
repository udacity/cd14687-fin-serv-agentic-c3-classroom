# Exercise Solution: Single Agent RAG: Banking Policy Assistant

### Solution Walkthrough

This solution builds a minimal, autonomous RAG agent capable of retrieving banking policy information, assessing the quality of its initial findings, and automatically re-querying the knowledge base with an improved search term if necessary.

First, we define a data structure, `SimpleRAGResponse`, to hold the agent's output in a structured format. This includes the final answer, the sources used, and metadata about the retrieval process, such as whether a retry was needed and the confidence level of the answer.

Next, we implement the `load_banking_documents_to_chroma` function to set up our knowledge base. This function initializes a persistent Chroma client, checks if our `banking_policies_simple` collection already exists, and if not, creates it. It then reads text files from the `/data` directory, splits them into manageable chunks using the `split_text_into_chunks` helper function, and adds them to the Chroma collection, which automatically handles embedding generation.

The core of the solution is the `SimpleRAGAgent` class. Its `process_query` method orchestrates the entire autonomous workflow.

1.  **Initial Retrieval**: It starts by calling `retrieve_documents` to query the Chroma vector store.
2.  **Generate Answer**: The retrieved documents are passed to `ask_llm_for_answer`, which prompts GPT-4 to generate an answer based *only* on the provided context.
3.  **Autonomous Decision**: The agent then calls `should_retry_retrieval`. This is a key step where the LLM is prompted to evaluate its own generated answer. It responds with "YES" or "NO" to indicate whether the information was sufficient or if another search is required.
4.  **Self-Improving Search**: If a retry is needed, `generate_better_search_query` is called. Here, the LLM creates a new, improved search query based on the original question and the shortcomings of the first answer. The agent then re-retrieves documents with this new query.
5.  **Confidence Assessment**: Finally, `assess_confidence` uses a simple heuristic to determine the confidence level (low, medium, or high) based on the number of retrieved documents and their relevance (distance score).

Finally, we test the agent with a series of queries. The loop processes each question and prints the structured response, showing the agent's answer, the sources it used, and a summary of the retrieval process.

### Key Takeaway

> This solution demonstrates how to build a minimal, autonomous RAG agent that uses an LLM to evaluate its own retrieval results and generate improved search queries when the initial context is insufficient.