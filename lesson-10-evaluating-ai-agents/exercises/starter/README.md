# Exercise: Evaluating an AI RAG Agent

In this exercise, you will implement a comprehensive evaluation framework for an AI agent that uses both persistent memory and Retrieval-Augmented Generation (RAG). You will start with a notebook containing several "TODO" sections and complete the code to measure the agent's performance using three industry-standard metrics: Factual Accuracy, Citation Compliance, and Retrieval Relevance.

Your goal is to transform the starter notebook into a complete evaluation suite that can run tests, calculate scores, and analyze the results to provide actionable insights.

### Prerequisites

*   Understanding of Retrieval-Augmented Generation (RAG) principles.
*   Familiarity with Python, pandas, and calling APIs.
*   Completion of the "Finance Memory Agent" exercise.

### Instructions

1.  **Setup and Configuration**: Update the configuration for the LlamaIndex `OpenAIEmbedding` to ensure it uses the correct API base URL for your environment.

2.  **Update Core Components**: Refactor the agent's core classes and methods (`FinanceMemoryManager`, `EvaluationAgent`) to align with the new evaluation framework naming conventions. Ensure the method for retrieving memories and answering questions are correctly updated.

3.  **RAG and Agent Initialization**: Update the data loading and agent initialization logic to use the new class names and method calls. Verify that the test call executes successfully.

4.  **Implement Evaluation Metrics**: Implement the `AgenticRAGEvaluationMetrics` class, which encapsulates the logic for three key metrics:
    *   **Factual Accuracy**: Use an LLM to score the agent's answer against a ground truth answer.
    *   **Citation Compliance**: Use regex patterns to verify if the agent's answer includes citations and calculate a score based on requirements.
    *   **Retrieval Relevance**: Calculate precision, recall, and F1-score by comparing retrieved document IDs with expected ones.
    *   **Composite Score**: Create a method to combine these metrics into a single weighted score.

5.  **Run Comprehensive Evaluation**: Implement the logic to iterate through a subset of the evaluation dataset. For each item, generate an agent response, evaluate it using your new metrics class, and aggregate the results.

6.  **Performance Analysis**: Implement analysis logic to calculate average scores across all metrics. Generate a summary report that breaks down performance by category and difficulty, and identifies specific areas for improvement, such as questions with poor retrieval relevance.