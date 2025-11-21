# Integrating External APIs: Building a Stock Price Agent - Demo

This demo showcases how to integrate external, real-time data into an AI agent. We'll build a stock investment assistant that fetches live stock prices from a public API, calculates the total purchase cost including fees, and intelligently asks for clarification when the user's request is incomplete.

### Walkthrough & Code
We begin by setting up the environment and importing the necessary libraries. This includes `requests` for making API calls and `dataclasses` to structure our data.

Before building the agent, we first test the connection to the Alpha Vantage API to ensure it's working. We'll make a request for a common stock ticker, like IBM, to verify that we can receive a valid response. The output confirms a successful connection with a status code of 200 and provides the current price for IBM, indicating the API is ready to use.

Next, we define two data models using Python's `dataclass` feature. The `InvestmentRequest` class will hold the information extracted from the user's prompt, such as the stock ticker and number of shares. The `InvestmentResult` class will store the final calculated breakdown, including the fetched price, fees, and total cost. Using dataclasses helps enforce a clear, type-safe structure for our data.

Now, we build the `StockPriceAgent` class, which contains the core logic. This class will integrate multiple tools to handle the entire workflow.

The first tool, `get_stock_price`, is responsible for fetching live data from the Alpha Vantage API. It takes a stock ticker, makes the HTTP request, and parses the JSON response to return the current price. It also includes a simple fallback to demo prices if the API rate limit is hit.

The second tool, `calculate_total_cost`, performs the financial calculations. It takes the fetched price and user-provided details to compute the base cost, broker fee, and finally the total investment amount.

The third tool, `extract_investment_info`, uses an LLM to parse the user's natural language query and extract structured data like the ticker, shares, and fees. This is done by creating a detailed prompt that instructs the model to return a JSON object.

Finally, the `process_investment_request` method orchestrates the entire workflow. It calls the tools in sequence: first extracting information, then checking for missing fields and asking clarifying questions if necessary, then fetching the stock price, calculating the cost, and finally formatting the output for the user.

With the agent fully defined, we can test it with a variety of scenarios. We'll use a set of predefined test cases that include both complete and incomplete user queries to see how the agent responds. The output demonstrates the agent successfully handling different requests. For complete queries, it fetches the price and provides a full cost breakdown. For incomplete queries, it correctly identifies the missing information and asks a relevant clarifying question, creating an interactive and helpful user experience.

> This demonstrates how to build a multi-tool agent that integrates external APIs, processes natural language, and performs multi-step calculations to provide a complete, user-friendly response.