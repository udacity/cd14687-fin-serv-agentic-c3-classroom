# Exercise Solution: Customer Support Dispute Intake Assistant

### Solution Walkthrough

This solution builds a customer support assistant capable of managing short-term memory across a multi-turn conversation. The core logic is encapsulated within the `DisputeIntakeAssistant` class, which orchestrates state, conversation history, and a running summary to handle a customer dispute intake process efficiently.

The assistant separates two key concepts: **state** and **memory**.
- **State** is managed by the `DisputeData` dataclass, which holds structured, factual information (e.g., `card_last4`, `merchant`, `amount`).
- **Memory** is handled through two components:
  1.  `conversation_history`: A raw log of the last *k* turns.
  2.  `session_summary`: A condensed, running list of key facts extracted from the entire conversation.

The `add_conversation_turn` function is the first piece of memory management. It adds the latest user-assistant exchange to the history and implements a sliding window to keep the history bounded. This prevents the context from growing indefinitely, which saves tokens and keeps the focus on recent events.

To maintain long-term context without an overflowing history, the `update_session_summary` function generates a running list of key facts. After each user turn, it prompts the LLM to update the existing summary with new information, ensuring that crucial details from early in the conversation are not lost.

The assistant progressively fills its structured state (`DisputeData`) using the `extract_dispute_info` function. The prompt provides the LLM with the currently captured data and instructs it to return *only new or updated information* in a strict JSON format. This prevents redundant work and ensures the state is always current.

Finally, the `generate_response` method synthesizes all memory components—the session summary, recent conversation history, and current state (captured vs. missing fields)—to create a coherent and context-aware response. By checking what it already knows, the assistant avoids re-asking for information, demonstrating memory-driven consistency.

When all required information is collected, `generate_final_summary` creates a professional handoff report for a human agent.

Running the simulation demonstrates this entire process in action. The assistant intelligently gathers information turn by turn, updates its internal memory and state, and never asks for the same piece of information twice.

### Key Takeaway

> By integrating a sliding conversation window, a running session summary, and a structured state, an agent can maintain context in long conversations, avoid repetition, and progressively build understanding.