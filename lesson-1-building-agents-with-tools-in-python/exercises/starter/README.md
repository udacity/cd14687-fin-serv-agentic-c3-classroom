# Exercise: Building Agents with Tools

This exercise guides you through building an AI agent that can call external tools using OpenAI's function calling capabilities. You will implement a financial assistant that performs calculations like compound interest and currency conversion.

### Prerequisites

*   Basic Python programming knowledge, including functions and dictionaries.
*   Familiarity with the OpenAI Chat Completions API.
*   A basic understanding of JSON schemas for defining data structures.

### Instructions

1.  **Implement Tool Functions**: Locate the `calculate_compound_interest` function in the notebook and implement its logic as described in its docstring.

2.  **Define OpenAI Tool Schemas**: Complete the `TOOLS` list by defining the JSON schemas for `calculate_compound_interest` and `convert_currency`. Ensure all parameters, their types, and descriptions are accurately represented, and required fields are specified.

3.  **Map Functions**: Populate the `FUNCTIONS` dictionary to map the tool names to their corresponding Python function objects.

4.  **Orchestrate Tool Calls (Part 1)**: In the `agentic_tool_call` function, complete the initial OpenAI API call. Ensure you pass the user's prompt, the defined `TOOLS`, and use `tool_choice` to explicitly direct the model to use the specified tool.

5.  **Orchestrate Tool Calls (Part 2)**: In the `agentic_tool_call` function, after the tool execution, complete the `messages` list for the second OpenAI API call. Add a tool message that includes the tool's output back to the model.

6.  **Implement Test Functions**: Complete the `test_compound_interest` and `test_currency_converter` functions by making calls to `agentic_tool_call` with appropriate parameters.

7.  **Run and Verify**: Uncomment the final test line for `test_compound_interest` to run your full implementation and verify its correctness.