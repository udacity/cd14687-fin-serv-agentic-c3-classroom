# Exercise Solution: Structured Outputs with Pydantic

### Solution Walkthrough

This exercise demonstrates a robust pipeline for processing raw data and generating structured, validated insights using Pydantic and the OpenAI API. We begin by defining Pydantic models that act as a schema, enforcing strict data types and validation rules for our financial data.

First, we define the `UserProfile`, `FinancialTransaction`, and `FinancialSummary` models. These classes use Pydantic's `Field` to set validation rules, such as string length, numeric ranges, and regex patterns for emails. This ensures that any data used to create these objects is clean and conforms to our expectations. Notice how `FinancialSummary` nests the other models, allowing for complex, type-safe data structures.

Next, we implement the `generate_user_profile_structured` function. The key change here is using the `response_format={"type": "json_object"}` parameter in the OpenAI API call. This instructs the model to return a guaranteed valid JSON string, which eliminates the parsing errors seen in the naive approach. The JSON response is then parsed and validated by instantiating the `UserProfile` model.

With our models defined, we process the `sample_financial_data.csv` file. The `load_and_process_financial_csv` function reads the data using pandas, groups it by user, and then iterates through each user's transactions. For each row of data, it creates validated instances of our `UserProfile` and `FinancialTransaction` models. This ensures data integrity from the start. Finally, it calculates totals and aggregates everything into a `FinancialSummary` object for each user.

Finally, we use the validated `FinancialSummary` objects to generate AI-powered insights. The `analyze_financial_data_with_ai` function takes a `FinancialSummary` object, serializes it into a JSON string to form a detailed prompt, and asks the AI to provide analysis in a new, specified JSON structure. This structured data is then used to present a personalized financial health report for each user.

This demonstrates an end-to-end workflow where structured data ensures reliability at every step, from initial processing to final AI-driven analysis.

### Key Takeaway

> Pydantic models enable robust, type-safe data processing by defining clear validation schemas that can be used to parse raw data and reliably structure outputs from AI models.