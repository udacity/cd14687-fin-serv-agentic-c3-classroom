# Implementing Long-Term Memory for AI Agents - Demo

### Intro

How do you build an AI agent that remembers critical information and policies across multiple conversations? A simple chat history isn't enough for enterprise applications that require consistency and compliance. This demo walks through building a sophisticated, long-term memory system for a corporate treasury assistant using PostgreSQL, SQLAlchemy, and an LLM for intelligent processing.

### Walkthrough & Code
In this walkthrough, we will build an AI agent with a persistent memory that can store, update, prune, and retrieve corporate policies intelligently. The agent will act as a corporate treasury assistant, remembering rules about cash management, investments, and compliance.

First, let's set up our environment by importing the necessary libraries and initializing the OpenAI client. We'll be using SQLAlchemy as our Object-Relational Mapper (ORM) to interact with a PostgreSQL database, which will serve as our persistent memory store.

#### Memory Database Schema

Next, we'll define the database schema for our agent's memories. The `MemoryEntry` class maps to a table in our database and includes fields for core data, temporal metadata (like creation date and time-to-live), weighting for prioritization, and organizational tags.

We also define a `MemoryPolicy` dataclass. This class holds the configuration for our memory management logic, such as Time-to-Live (TTL) policies for different topics and the coefficients for our dynamic weighting formula. With the schema and policies defined, we create the database engine and the corresponding table.

#### Intelligent Memory Manager

Now, we build the core `TreasuryMemoryManager` class. A key feature is the `canonicalize_fact` method, which uses an LLM to normalize raw text into a clear, consistent statement. This prevents duplicate or ambiguous entries in our memory.

#### Session Simulation

Let's simulate the assistant in action. In Session A, the CFO provides the initial set of treasury policies. Our assistant processes this input, canonicalizes each fact, and stores them in the database. The system adds new policies and displays a digest of the most important ones.

Days later, in Session B, a team member asks for advice on a new investment opportunity. The agent uses its stored memory to provide a comprehensive, policy-aware recommendation. The assistant correctly identifies any conflicts with stored policies and advises accordingly, demonstrating its ability to recall and apply rules across sessions.

> This structured memory system empowers an AI agent to go beyond simple chat history, enabling it to provide consistent, compliant, and context-aware advice.