# Exercise Solution: Long-Term Agent Memory Management

### Solution Walkthrough

This exercise builds a finance assistant with a sophisticated long-term memory system. Unlike basic chat history, this system uses a structured PostgreSQL database to store, manage, and intelligently recall client information over time. The goal is to provide consistent, context-aware advice across multiple sessions.

The solution starts by defining the database schema using SQLAlchemy. The `MemoryEntry` class represents a single piece of information, containing core data, temporal metadata for expiration (TTL), and fields for weighting and prioritization. The `MemoryPolicy` dataclass configures the rules for managing these memories, such as how long different topics should be remembered and the coefficients for calculating their importance.

The core logic is encapsulated in the `FinanceMemoryManager`. This class handles all intelligent operations on the memory. Key methods include:
- `upsert_memory`: The main entry point for adding or updating facts. It first uses an LLM to `canonicalize` the fact into a standard format and then `detect_conflicts` with existing memories, also using an LLM. Conflicting facts are removed before the new or updated fact is committed.
- `calculate_weight` and `reweight_all_memories`: These methods implement dynamic reweighting. The weight of each memory is recalculated based on its recency, frequency of use, and whether it's "pinned" as important. This ensures that the most relevant information has the highest priority.
- `prune_memories`: This method cleans up the memory by removing facts that have expired based on their TTL or have a very low weight, keeping the memory store efficient and relevant.
- `generate_profile_digest`: Instead of sending the entire memory to the LLM, this method creates a compact, bullet-point summary of the top-weighted memories. This digest serves as the context for generating personalized advice.

Finally, the `FinanceAssistant` class acts as the user-facing interface. It uses the `FinanceMemoryManager` to process user input, update the memory, and answer questions. When a user asks a question, the assistant generates a profile digest, passes it to the LLM as context, and returns a context-aware answer.

The first session demonstrates this process by taking the client's initial onboarding information, extracting structured facts, and populating the memory. The system intelligently processes the input, creating and weighting new memories. The output shows the actions taken (e.g., adding goals, constraints) and the resulting client profile digest that will be used for future interactions.

### Key Takeaway

> This solution builds a persistent, long-term memory system for an AI agent using a PostgreSQL database, featuring dynamic weighting, conflict resolution, and intelligent pruning to maintain relevant context across user sessions.