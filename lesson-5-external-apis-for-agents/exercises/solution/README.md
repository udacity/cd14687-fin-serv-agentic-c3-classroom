# Exercise Solution: FX Rate Conversion Agent with External API Integration

### Solution Walkthrough

This exercise focuses on building a currency conversion agent that integrates with an external API to fetch live exchange rates. The agent uses several tools to handle the entire workflow, from understanding a user's natural language request to providing a formatted breakdown of the final cost.

First, we implement the `get_fx_rate` method. This tool makes a `GET` request to the Frankfurter API to fetch the latest exchange rate between a source (`from_ccy`) and target (`to_ccy`) currency. The implementation includes robust error handling using a `try...except` block to gracefully manage API request failures or issues with parsing the response.

Next, the `calc_total` method performs the financial calculations. It takes the original price, the fetched exchange rate, and percentage-based fees to compute a final cost. This multi-step process first converts the base amount, then calculates the FX fee and sales tax separately, and finally sums these components to produce the grand total, which is returned in a structured `ConversionResult` object.

To understand the user's intent, the `extract_purchase_info` method uses an LLM to parse a natural language query. A detailed prompt instructs the model to extract key details—price, currencies, and fees—and return them in a structured JSON format. The code then cleans up the LLM's response, parses the JSON, and populates a `PurchaseRequest` object.

If the user's request is incomplete, the `ask_clarifying_question` method generates a targeted follow-up question. It prioritizes the missing information (e.g., asking for the price before the FX fee) to ensure a logical and user-friendly conversation flow.

Finally, the `format_result` method presents the `ConversionResult` in a clean, professional, and itemized breakdown, making the final cost transparent to the user.

Running the `test_scenarios` function demonstrates the agent's full capabilities. It handles a complete request correctly, identifies missing information and asks clarifying questions, and orchestrates all tools to deliver an accurate and informative response.

### Key Takeaway

> This exercise demonstrates how to build a robust agent that integrates external APIs for live data, uses an LLM for natural language understanding, and handles multi-step calculations with graceful error handling.