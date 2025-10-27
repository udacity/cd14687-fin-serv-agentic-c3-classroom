# Concept 1: Long-Term Agent Memory - Starter Code

Build a finance assistant that maintains persistent client profiles using PostgreSQL and intelligent memory policies.

## 🎯 Learning Objectives

- Design persistent memory schemas for AI agents
- Implement intelligent memory update and conflict resolution
- Create memory pruning policies with TTL and weight thresholds
- Build dynamic reweighting based on recency, frequency, and importance
- Generate compact memory digests for efficient context usage

## 🏗️ What You'll Build

A **FinanceMemoryManager** that:

- 🧠 **Stores client facts** in PostgreSQL with weights and TTL
- 🔄 **Updates intelligently** with conflict detection and resolution
- ✂️ **Prunes old memories** based on TTL and relevance scores
- ⚖️ **Reweights dynamically** using recency, frequency, and importance
- 📋 **Generates compact digests** for LLM context (≤12 items)

## 📋 Requirements

### Core Features
- **Memory Schema**: Complete SQLAlchemy model with metadata fields
- **Smart Updates**: LLM-powered fact canonicalization and conflict resolution
- **Memory Policies**: TTL-based expiration and weight-based pruning
- **Profile Digests**: Compact summaries for efficient LLM context

### Technology Stack
- **Database**: PostgreSQL with SQLAlchemy ORM
- **LLM**: OpenAI GPT-4 for fact processing
- **Domain**: Personal finance assistant

## 🚀 Getting Started

### 1. Environment Setup

```bash
# Install dependencies
pip install -r ../../../requirements.txt

# Set up environment variables
cp .env.template .env
# Edit .env with your OpenAI API key and database URL
```

### 2. Complete Implementation

Open `finance_memory_agent.ipynb` and complete all the **YOUR CODE HERE** sections:

1. **Database Schema** - Complete the MemoryEntry model
2. **Memory Manager** - Implement core memory operations
3. **Finance Assistant** - Build the context-aware assistant
4. **Testing** - Run the test scenarios

### 3. Success Criteria

Your implementation should demonstrate:
- ✅ Memory persistence across sessions
- ✅ Intelligent conflict resolution
- ✅ Automatic memory pruning and reweighting
- ✅ Context-aware financial advice
- ✅ Compact profile digests (≤12 items)

## 📊 Test Scenarios

1. **Client Onboarding**: Store initial goals, risk tolerance, constraints
2. **Memory Updates**: Handle conflicting information intelligently
3. **Context Usage**: Answer questions using stored client profile
4. **Memory Management**: Demonstrate pruning and reweighting

## 🛠️ Implementation Tips

1. **Start Simple**: Begin with basic CRUD before adding intelligence
2. **Test Incrementally**: Validate each method as you build it
3. **Use LLM Effectively**: Design clear prompts for fact extraction
4. **Handle Edge Cases**: Account for API errors and invalid data
5. **Focus on UX**: Provide clear feedback about memory operations

## 📚 Key Concepts

- **TTL (Time To Live)**: Automatic expiration of stale memories
- **Weight Calculation**: Dynamic scoring based on recency/frequency/importance
- **Conflict Resolution**: LLM-powered detection and resolution of contradictory facts
- **Memory Pruning**: Intelligent removal of low-value or expired memories
- **Profile Digests**: Compact summaries optimized for LLM context windows

Good luck building your intelligent memory system! 🚀
