# Exercise: Build a Customer Support Dispute Intake Assistant

In this exercise, you'll implement short-term memory management for multi-turn conversations in a customer support context.

Your task is to build a customer support assistant that helps customers file card transaction disputes. The assistant must:
- Remember details from previous turns without re-asking.
- Maintain a sliding window of conversation history (last k turns).
- Keep a running session summary (3-5 key facts).
- Extract structured dispute information progressively.

### Prerequisites

*   Basic Python programming, including classes and methods.
*   Familiarity with the OpenAI API structure.
*   Understanding of basic prompt engineering principles.

### Instructions

1.  **Conversation History**: Implement logic in `add_conversation_turn` to store conversation turns and maintain a sliding window of history.

2.  **Session Summary**: Complete `update_session_summary` to generate and update a running summary of key facts using the OpenAI API.

3.  **Information Extraction**: Implement `extract_dispute_info` to progressively extract structured dispute details (like amount, merchant, date) from user input into the `DisputeData` model.

4.  **Response Generation**: Complete `generate_response` to construct a prompt that uses memory context (summary + history) and captured data to generate natural, context-aware responses.

5.  **Final Summary**: Implement `generate_final_summary` to produce a concise handover report for human agents once the interaction is complete.

6.  **Testing**: Run the provided test conversation to verify that the assistant remembers context and doesn't ask repetitive questions.