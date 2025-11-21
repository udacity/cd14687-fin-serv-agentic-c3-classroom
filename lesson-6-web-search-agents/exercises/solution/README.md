# Exercise Solution: Web Search Agents: High-Yield Savings Account (HYSA) Rate Finder

### Solution Walkthrough

This exercise walks through building a complete web search agent that finds, extracts, and summarizes financial data in real-time. The agent uses the Tavily Search API to find current High-Yield Savings Account (HYSA) rates and an LLM to process the unstructured text into a professional summary.

First, we expand the `__init__` method to include a more comprehensive set of reputable financial domains. This list will be used to filter our search results and ensure we only process information from trusted sources.

The `search_web` method is implemented to connect to the Tavily API. It first checks for an API key, falling back to mock data if one isn't found. The core logic constructs a JSON payload that includes a `fresh_query` to get recent results and uses `include_domains` to focus the search on our reputable sources.

Next, the `filter_reputable_sources` method ensures source credibility by checking each search result's domain against our pre-defined whitelist. This step is crucial for financial applications where accuracy and trustworthiness are paramount.

The `extract_hysa_data` method uses an LLM to parse unstructured text from search snippets into structured `HYSARecord` objects. We design a detailed `extraction_prompt` that instructs the model to act as a financial expert and return a JSON array containing the bank name, APY, and minimum deposit.

Since multiple reputable sources might report slightly different information for the same bank, the `merge_and_dedupe` method is added. It groups records by bank name and selects the most authoritative entry, prioritizing the highest APY and then a credibility score. This ensures a clean, de-duplicated list.

The `synthesize_summary` function generates the final, user-facing report. It prepares the top 5 records, crafts a `synthesis_prompt` instructing the LLM to create a professional summary with an intro and key takeaway, and compiles a list of sources for attribution.

Finally, the main orchestration method, `find_top_hysa_rates`, is updated to include the new `merge_and_dedupe` step, completing the agent's five-step pipeline. Running the agent with a test query now produces a detailed and professionally formatted summary.

### Key Takeaway

> This solution builds a multi-step financial agent that uses a real-time web search API to gather data, an LLM to extract and structure it, and another LLM call to synthesize a professional, user-ready summary.