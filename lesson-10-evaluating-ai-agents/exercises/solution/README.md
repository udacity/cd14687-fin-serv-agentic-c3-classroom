# Exercise Solution: Evaluating AI Agents

### Solution Walkthrough

This solution builds a production-grade evaluation framework to assess our AI agent's performance. We implement three key industry-standard metrics within a single `AgenticRAGEvaluationMetrics` class: Factual Accuracy, Citation Compliance, and Retrieval Relevance.

First, we implement the **Factual Accuracy** metric. This function uses a powerful technique called LLM-as-a-judge, where we prompt another LLM to score the agent's response against the ground truth. The key is a well-structured prompt that requests a JSON output containing the score and reasoning.

Next, for regulatory and trust purposes, we evaluate **Citation Compliance**. This metric uses regular expressions to check if the agent's answer includes source citations when required. The scoring logic handles all four scenarios, such as when a citation is required and present versus when it's not required but is still provided.

To measure the RAG system's effectiveness, we implement **Retrieval Relevance**. This function calculates precision and recall to determine if the agent retrieved the correct documents. The F1-score provides a single, balanced measure of retrieval quality, which we scale to 100 for consistency.

With the individual metrics defined, the `evaluate_complete_response` method calculates a weighted **composite score** (40% for accuracy, 30% for citation, and 30% for retrieval), giving a holistic view of the agent's performance.

Finally, we run the evaluation suite. The code iterates through our golden dataset, gets a response from the agent for each question, and uses our framework to generate a detailed evaluation result. After running the evaluation, the results are collected into a DataFrame, providing a clear summary of the agent's performance on each question.

### Key Takeaway

> You have successfully implemented a comprehensive, multi-metric evaluation framework to objectively measure and analyze the performance of an agentic RAG system.