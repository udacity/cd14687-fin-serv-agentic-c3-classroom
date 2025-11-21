# Exercise: Web Search Agent for HYSA Rate Finder

In this exercise, you will build a sophisticated agent designed to find the best High-Yield Savings Account (HYSA) rates. This agent will integrate with a real web search API (Tavily), filter search results for credible financial sources, use a Large Language Model (LLM) to extract structured data from unstructured text, and synthesize its findings into a professional, user-ready summary.

### Prerequisites

*   Familiarity with Python classes and methods.
*   Understanding of how to make API requests using libraries like `requests`.
*   Basic experience with the OpenAI Chat Completions API.
*   Knowledge of using environment variables to manage API keys securely.

### Instructions

1.  **Tavily Client Integration**: Import the Tavily client, handle potential import errors, and update status checks.

2.  **Expand Reputable Sources**: Update the `reputable_domains` list in the `WebSearchAgent` class to include a comprehensive list of trusted financial sources.

3.  **Implement Web Search**: Complete the `search_web` method to query the Tavily API. Construct the API request payload, handle the response, and convert the results into `SearchResult` objects. Include robust error handling.

4.  **Filter Results**: Implement `filter_reputable_sources` to filter search results based on the whitelist of trusted domains.

5.  **Extract Structured Data**: Implement `extract_hysa_data`. Use the OpenAI API with a specific prompt to extract bank names, APYs, and minimum deposits from search snippets into structured JSON. Convert this data into `HYSARecord` objects.

6.  **Merge and Deduplicate**: Implement helper methods to merge duplicate records for the same bank and prioritize data from the most credible sources.

7.  **Synthesize Summary**: Complete `synthesize_summary` to generate a final report. Select the top rates, prompt the LLM to create an intro and takeaway, and compile a list of sources into a `HYSASummary` object.

8.  **Orchestrate Workflow**: Update `find_top_hysa_rates` to include the new merging and deduplication steps and ensure comprehensive search queries.

9.  **Format Output**: Implement a formatting function to present the final `HYSASummary` as a clean, professional Markdown report.