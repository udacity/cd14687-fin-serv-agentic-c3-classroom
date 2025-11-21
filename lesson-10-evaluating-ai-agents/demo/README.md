# Evaluating an Agentic RAG System for Insurance Claims - Demo

### Intro
Building reliable AI agents for regulated industries like insurance is challenging. They must be accurate, compliant, and their reasoning must be transparent. This demo walks through a production-grade framework for evaluating an insurance claims assistant, using industry-standard metrics to measure performance, identify weaknesses, and ensure the agent is ready for real-world deployment.

### Walkthrough & Code
We'll evaluate an AI claims assistant using three key metrics: factual accuracy, citation compliance, and retrieval relevance. The setup configures our environment to use LlamaIndex for Retrieval-Augmented Generation (RAG) and specifies these metrics as our focus.

First, we define the core components of our insurance claims assistant. This includes classes for managing persistent memory and an `EvaluationClaimsAssistant` that integrates this memory with a LlamaIndex RAG retriever.

Next, we load our "golden" Q&A dataset and policy documents. We then use these documents to initialize our LlamaIndex RAG system, which creates a vector index for efficient document retrieval. `similarity_top_k=3` tells the retriever to fetch the top three most relevant documents for any given query.

Now, we define the functions for our three core evaluation metrics.
*   **Factual accuracy** uses an LLM to score how correct the agent's answer is compared to the ground truth answer.
*   **Citation compliance** checks whether the agent provided source citations, which is critical for regulatory compliance in insurance.
*   **Retrieval relevance** measures how well our LlamaIndex RAG system retrieved the correct documents using classic information retrieval metrics like precision and recall.

Finally, a wrapper function combines these three scores into a single weighted composite score, giving us a holistic view of the agent's performance.

With our metrics defined, we loop through the golden dataset, get a response from our agent for each question, and evaluate it. To understand the results, we calculate and display a comprehensive performance analysis. This aggregates the scores to give us a high-level overview. The analysis clearly shows high factual accuracy and perfect citation compliance, but very poor retrieval relevance. This pinpoints exactly where we need to improve the system.

Based on these results, we can automatically generate actionable recommendations. The system identifies the low retrieval score and suggests specific ways to fix it.

> By systematically evaluating an agent against weighted metrics for accuracy, citation, and retrieval, we can precisely identify weaknesses—like poor document retrieval—and generate targeted improvements.