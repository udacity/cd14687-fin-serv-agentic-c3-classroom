# Building Agents with Tools in Python - Demo

### Intro

Financial services companies often need AI-powered assistants to perform specific, deterministic calculations for clients, such as calculating Return on Investment (ROI) or corporate tax deductions. This demo demonstrates how to build an AI agent that can call external Python functions, or "tools," to handle these tasks, ensuring accuracy and integrating the results into a professional, easy-to-understand analysis.

### Walkthrough & Code

In this walkthrough, we'll create an AI agent for a financial services company. This agent will use custom Python functions as tools to perform financial calculations.

First, we set up our environment by importing the necessary libraries and initializing the OpenAI client. The `load_dotenv()` function loads our API key from a local `.env` file for security. We also define a `SYSTEM` prompt to give our agent its persona as a helpful corporate financial advisor.

Next, we define the core business logic in standard Python functions. These functions will serve as our external tools. The first tool, `calculate_roi`, calculates the total and annualized Return on Investment. It includes a `ValueError` for basic input validation. The second tool, `calculate_expense_deduction`, determines tax savings based on department-specific deduction rates, which represent internal corporate tax rules.

To make these functions callable by the OpenAI model, we must describe them using a specific JSON schema. This schema tells the model the function's name, what it does, and what parameters it requires.

Then, we create the core logic that orchestrates the tool call. The `agentic_tool_call` function follows a three-step process:
1.  **Ask the model to call a specific tool**: We make an initial API call, passing the user's prompt and the tool schemas. Crucially, we use the `tool_choice` parameter to force the model to use a specific function, removing any ambiguity.
2.  **Execute the Python function**: We parse the model's response to get the function name and arguments, find the corresponding Python function, and execute it locally.
3.  **Send the result back for analysis**: We make a final API call, sending the entire conversation history, including the tool call and its result. The model then uses this result to generate a final, natural-language analysis.

Finally, let's test our agent. We'll create a simple test function and call it with sample data for an ROI analysis. The agent first calls our `calculate_roi` function to get the numbers, then uses those results to generate a comprehensive analysis and recommendation. We can do the same for our expense deduction tool.

> By defining custom functions and schemas, we can create powerful AI agents that integrate deterministic business logic into their generative capabilities.