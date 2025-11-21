# Building a Financial Advisor Assistant with Short-Term Memory - Demo

### Intro

Standard chatbots often create frustrating user experiences because they are stateless—they forget what you've told them in previous turns. This demo shows how to build a more intelligent AI assistant by implementing a short-term memory system. We'll create a financial advisor that remembers client details throughout a conversation, providing natural, context-aware, and professional advice without asking repetitive questions.

### Walkthrough & Code

This demo walks through creating a financial advisor AI assistant that uses a multi-component memory system to maintain context across a conversation. The goal is to avoid repetitive questions and provide personalized, professional advice. The memory system has three key parts: a sliding window for recent conversation history, a running summary of key facts, and a structured profile for extracted client data.

First, we define the data models that will serve as the foundation for our memory structure. The `ClientProfile` dataclass tracks key financial and demographic information, while the `ConversationTurn` dataclass stores a single client-advisor exchange.

Next, we build the `FinancialAdvisorAssistant` class, which manages the agent's memory. The `__init__` method sets up the three memory components: `profile`, `conversation_history`, and `session_summary`. It also defines `max_history`, which controls the size of our sliding window for conversation history.

The `add_turn` method adds a new exchange to the conversation history and enforces the sliding window, ensuring the history doesn't exceed the `max_history` limit to manage the context window size.

After each turn, we use two functions to update our memory. The `update_session_summary` method sends the existing summary and the latest client input to an LLM, asking it to produce a condensed, running list of 3-5 key facts. This prevents the context from growing too large while retaining essential information.

Simultaneously, the `extract_profile` function uses an LLM to parse the client's input and extract structured information (like age, risk tolerance, etc.) into the `ClientProfile` data model. This allows the agent to use this data for logical operations and personalized recommendations.

The `generate_response` method orchestrates the agent's reply. It constructs a comprehensive prompt that includes the session summary (`memory_context`), recent conversation history (`conversation_context`), and the captured client profile. This ensures the LLM has all the necessary context to generate a helpful and non-repetitive response.

Finally, a `process_input` function ties everything together, calling the memory update, profile extraction, and response generation functions in sequence. To test it, we simulate a multi-turn conversation. As the conversation progresses, the output shows the memory state evolving. The summary condenses key facts, the profile captures structured data like age and risk tolerance, and the history maintains the recent conversational flow.

> This multi-component memory pattern transforms a stateless chatbot into a professional, context-aware assistant capable of maintaining a coherent and personalized dialogue.