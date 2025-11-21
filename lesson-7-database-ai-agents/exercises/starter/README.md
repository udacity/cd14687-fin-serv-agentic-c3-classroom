# Exercise: Database AI Agent: Text-to-SQL

Build an AI agent that converts natural language questions into safe SQL queries for finance operations. You will support a Finance Ops team by helping them get quick answers about corporate card spend without writing SQL. This involves designing data models, building robust LLM prompts, implementing safety guardrails, adding retry logic, and generating professional summaries.

### Prerequisites

*   Python programming, including classes and dataclasses.
*   Familiarity with the OpenAI API.
*   Basic understanding of SQL and database concepts.
*   Experience with Pandas DataFrames.

### Instructions

1.  **Define Data Models**: In the `QueryResult` dataclass, define the attributes to store the original question, generated and executed SQL, result data, row count, summary, applied filters, and assumptions. Initialize assumptions in the `__post_init__` method. Similarly, define the `DatabaseSchema` dataclass attributes for tables, relationships, and time columns.

2.  **Implement Processing Pipeline**: In the `FinanceTextToSQLAgent.process_question` method, implement the main logic flow: generate SQL (with retry), apply safety checks, execute the query, and generate a summary. Return a populated `QueryResult` object.

3.  **Generate SQL**: In the `_generate_sql` method, construct a prompt that includes the schema information and any error feedback from previous attempts. Call the OpenAI API to generate the SQL query and clean the response.

4.  **Apply Safety Checks**: In the `_apply_safety_checks` method, implement guardrails to ensure the query is strictly a `SELECT` statement and contains no forbidden keywords (like `INSERT`, `UPDATE`, `DELETE`).

5.  **Execute Query**: In the `_execute_query` method, execute the safe SQL query against the database and convert the results into a Pandas DataFrame.

6.  **Generate Summary**: In the `_generate_summary` method, use the OpenAI API to generate a natural language summary of the query results, providing context to the user.

7.  **Test Scenarios**: Update and run the provided test cases (Test Case 1, 3, and 4) with specific date ranges (e.g., "last 120 days", "last 90 days") to verify the agent's functionality and display the SQL outputs.