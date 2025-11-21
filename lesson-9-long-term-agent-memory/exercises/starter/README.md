# Exercise: Long-Term Agent Memory Management

**Objective**: Build a finance assistant that persists client profiles in PostgreSQL and applies intelligent memory policies to maintain relevant context over extended sessions. Your goal is to implement the core logic for a memory system that can store, update, prune, and reweight facts about a user, enabling an AI agent to provide consistent and personalized advice over time.

### Prerequisites

*   Familiarity with Python classes and dataclasses.
*   Understanding of SQLAlchemy ORM for database interactions.
*   Experience making API calls to an LLM, such as the OpenAI API.

### Instructions

1.  **Schema Definition**: Complete the `MemoryEntry` class by defining the database schema. Add columns for core data (topic, fact), metadata (source, timestamps), policies (TTL, weight, pinned status), and stats (frequency count). Implement helper methods to check for expiration and calculate age.

2.  **Policy Configuration**: Define the `MemoryPolicy` dataclass to hold configuration settings for memory management, including Time-To-Live (TTL) rules for different topics, weighting coefficients, and digest size limits.

3.  **Intelligent Memory Manager**: Implement the `FinanceMemoryManager` class. Key methods include:
    *   `canonicalize_fact`: Use the LLM to normalize raw text into consistent statements.
    *   `detect_conflicts`: Use the LLM to find existing memories that contradict new information.
    *   `upsert_memory`: Handle logic to insert new facts or update existing ones, resolving conflicts and duplicates.
    *   `calculate_weight`: Compute dynamic importance scores based on recency, frequency, and pin status.
    *   `prune_memories`: Remove expired or low-value memories to keep the context manageable.
    *   `generate_profile_digest`: Create a summarized view of the top-weighted memories for the agent context.

4.  **Finance Assistant Integration**: Implement the `FinanceAssistant` class to connect the memory system with user interaction.
    *   `_extract_facts`: Use the LLM to parse user input into structured facts.
    *   `process_user_input`: Orchestrate the flow of extracting facts, updating memory, and running maintenance (reweighting/pruning).
    *   `answer_question`: Retrieve relevant context from the memory digest to generate personalized answers.

5.  **Testing and Validation**: Run the provided test scenarios to simulate a multi-session interaction. Verify that the agent correctly stores onboarding info, handles updates (like paying off a loan), respects TTL policies, and uses long-term context to answer financial questions effectively.