# Building a Text-to-SQL AI Agent for HR Analytics - Demo

### Intro

Unlock the power of your database for everyone on your team, not just engineers. This demo shows how to build a smart AI agent that allows non-technical users, like an HR team, to ask questions in plain English and get back clear, summarized insights from a recruitment database. We'll focus on creating a robust agent that not only translates language to SQL but also enforces critical safety rules to protect your data.

### Walkthrough & Code

In this walkthrough, we'll build a database AI agent that can understand natural language questions, convert them to safe SQL queries, execute them, and return professional summaries. We'll use SQLAlchemy, a database toolkit that lets our agent work with various database systems like SQLite, PostgreSQL, or MySQL.

First, we define the data structures for our agent using Python's `dataclasses`. The `QueryResult` class will hold all the information from a single transaction, including the original question, the generated SQL, the final executed SQL, and the data itself. The `DatabaseSchema` class will represent the structure of our database, which is crucial for both validating queries and giving the LLM context.

With the schema defined, we create utility functions to interact with the database. The `get_schema_description` function formats our schema into a clear, readable string. This text-based representation is what we'll feed to the LLM so it understands the database structure. The `check_database_exists` function establishes a connection to our SQLite database using a SQLAlchemy engine and runs a few initial queries to gather basic statistics, confirming everything is working correctly.

Now, we build the core of our application: the `HRTextToSQLAgent`. This class orchestrates the entire process, from understanding the user's question to delivering a safe, summarized answer.

The main workflow is handled by the `process_question` method, which follows a clear, multi-step process:
1.  **Generate SQL**: It first attempts to generate a SQL query from the user's natural language question.
2.  **Apply Safety Checks**: The raw SQL from the LLM is then passed through a rigorous safety check to prevent any dangerous operations.
3.  **Execute Query**: Only the verified, "safe" SQL is executed against the database.
4.  **Generate Summary**: Finally, the results are summarized back into natural language for the end-user.

To make the agent robust, we implement a retry mechanism. The `_generate_sql_with_retry` function will try up to three times to generate a valid SQL query. If a generated query fails our syntax validation, the error is fed back to the LLM in the next attempt, helping it self-correct.

The most critical part is our safety layer, implemented in `_apply_safety_checks`. This function acts as a guardrail. First, it ensures the query is a `SELECT` statement, blocking any attempts to modify data with `INSERT`, `UPDATE`, or `DELETE`. Second, it checks for these forbidden keywords. Third, it ensures a `LIMIT` clause is present to prevent accidentally running a query that returns millions of rows, which could be slow and costly.

Finally, let's test our agent. We ask a typical HR question and see the agent in action. The agent successfully generates the correct SQL, executes it, and returns the results. We can also run a safety test to confirm our guardrails are working. As expected, the agent refuses to perform dangerous operations like delete.

> This demo illustrates how to construct an intelligent and secure AI agent that bridges the gap between natural language questions and structured database queries.