# Building an Autonomous RAG Agent for HR Questions - Demo

### Intro

Searching through long, dense HR policy documents to find answers to simple benefits questions can be a frustrating experience for employees. This demo walks you through building a single-agent Retrieval-Augmented Generation (RAG) system that acts as an intelligent HR assistant, retrieving specific policy information from a vector store to provide quick and accurate answers.

### Walkthrough & Code

This demo showcases how to build a single-agent RAG system. The agent will handle employee questions about topics like health insurance, PTO, and 401(k) plans.

The architecture follows a simple but powerful pattern. A user asks a question, and the system retrieves relevant documents from a knowledge base. An LLM then generates an answer based on that context. Crucially, the LLM also evaluates if its own answer is complete. If not, it generates a better search query, retries the retrieval, and then returns a final answer with sources and a confidence level.

First, we set up our environment by importing the necessary libraries and initializing the OpenAI client. We'll use `chromadb` for our vector storage.

Next, we define a data model to structure the agent's responses. This `RAGResponse` class will store the original query, the generated answer, the sources used, and metadata about the retrieval process, such as whether a retry was needed and the confidence level.

With the structure defined, we load our HR policy documents into a Chroma vector database. This process involves finding text files in a data directory, splitting them into smaller, overlapping chunks for better retrieval, and adding them to a Chroma collection. If the collection already exists, the function will use it; otherwise, it creates a new one.

Now we build the core of our system: the `EmployeeBenefitsRAGAgent`. This class orchestrates the entire RAG pipeline. Its main method, `process_query`, handles the full workflow:
1.  **Initial Retrieval**: It calls `retrieve_documents` to find relevant text chunks in Chroma.
2.  **Generate Initial Answer**: It passes the retrieved documents to `generate_answer`, which uses GPT-4 to create a response based *only* on the provided context.
3.  **Decide if Retry is Needed**: The agent uses the `should_retry` method, which asks the LLM to evaluate if the initial answer was sufficient. If the answer is vague or says it lacks information, it will decide to retry.
4.  **Retry**: If a retry is needed, the `improve_query` method is called. This uses the LLM to generate a better, more specific search query. The agent then retrieves documents again with this new query.
5.  **Assess Confidence**: Finally, the `assess_confidence` function determines a confidence score (high, medium, or low) based on the number of retrieved documents and their relevance.

Let's test the system with a few realistic employee questions. The agent successfully answers the questions, providing detailed responses grounded in the policy documents and citing its sources.

A key feature of this agent is its ability to handle out-of-scope questions gracefully. When asked a question outside the knowledge base, the agent correctly concludes that it doesn't have the information.

> This demo shows how to build an intelligent, single-agent RAG system that can autonomously retrieve information, evaluate its own answers, and improve its search queries to handle complex user questions.