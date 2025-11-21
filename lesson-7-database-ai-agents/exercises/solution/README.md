# Exercise Solution: Database AI Agents: Text-to-SQL for Finance Operations

### Solution Walkthrough

This exercise focuses on building a robust AI agent that can safely convert natural language questions into executable SQL queries for a finance database. We begin by defining the data models that will structure our system's inputs and outputs. The `QueryResult` dataclass holds all information related to a single query, while `DatabaseSchema` represents the database structure for validation and LLM context.

Next, we implement the `FinanceTextToSQLAgent` class. Its core is the `process_question` method, which orchestrates a four-step pipeline: generating the initial SQL, applying safety checks, executing the sanitized query, and generating a final summary.

To make the agent robust, the `_generate_sql_with_retry` method attempts to generate and validate SQL up to three times. If a validation fails, the error message is fed back into the prompt for the next attempt, helping the LLM correct its mistake.

The `_generate_sql` method constructs a detailed prompt for the LLM. It includes the database schema, important rules (e.g., use only `SELECT`, add a `LIMIT`), SQLite-specific function usage, and any feedback from a previous failed attempt.

A critical component is the `_apply_safety_checks` method, which acts as a guardrail. It enforces several rules: ensuring the query is a `SELECT` statement, checking for forbidden keywords like `INSERT` or `DELETE`, and automatically adding a `LIMIT` clause and a default 90-day time filter for transaction queries to prevent excessive data retrieval and ensure performance.

The `_execute_query` method uses the SQLAlchemy engine to run the safe SQL, handling potential database or execution errors gracefully.

Finally, `_generate_summary` uses another LLM call to create a professional, natural-language summary of the results, making the data accessible to non-technical users.

When tested, the agent successfully processes a natural language question, generates the correct SQL, executes it, and provides a formatted table of results along with an insightful summary.

### Key Takeaway

> You have built a robust Text-to-SQL agent that converts natural language questions into safe, executable SQL queries, complete with retry logic, safety guardrails, and AI-generated summaries.