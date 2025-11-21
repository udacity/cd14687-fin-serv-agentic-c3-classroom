# Exercise: FX Rate Conversion Agent

In this exercise, you'll build an agent that integrates with **external APIs** to provide real-time currency conversion with fee calculations. Your task is to complete an `FXRateAgent` by implementing five key methods: fetching live exchange rates, calculating total costs, extracting information from user input, asking clarifying questions for missing details, and formatting the final result. The agent should be able to provide itemized breakdowns and handle missing information intelligently.

### Prerequisites

*   Making API requests with the `requests` library.
*   Working with JSON data.
*   Calling the OpenAI API for text generation and structured data extraction.
*   Basic Python concepts: f-strings, classes, methods, dictionaries, and lists.

### Instructions

1.  **Fetch Exchange Rates**: In the `get_fx_rate` method, implement the logic to call the Frankfurter API to fetch the current exchange rate for the given currency pair. Handle potential API errors gracefully.

2.  **Calculate Costs**: In the `calc_total` method, implement the financial calculations to determine the base amount, FX fee, sales tax, and total cost in USD. Return a populated `ConversionResult` object.

3.  **Extract Information**: In the `extract_purchase_info` method, use the OpenAI API to parse user input and extract structured data (price, currencies, fees) into a `PurchaseRequest` object. Ensure the prompt guides the model to return valid JSON.

4.  **Handle Missing Data**: In the `ask_clarifying_question` method, implement logic to identify missing required fields and return a specific, prioritized clarifying question to the user.

5.  **Format Output**: In the `format_result` method, construct a detailed, user-friendly string that presents the full breakdown of the conversion, including the spot rate, fees, and grand total.

6.  **Test**: Uncomment and run the `test_scenarios()` function to verify your agent's performance against various test cases.