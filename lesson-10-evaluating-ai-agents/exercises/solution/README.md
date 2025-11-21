# Concept 2: Evaluating AI Agents with Memory + RAG Integration

**Objective**: Evaluate the finance memory agent from Concept 1 using industry-standard agentic AI metrics with LlamaIndex RAG capabilities.

## 🎯 Integration Approach

This exercise builds upon **Concept 1** (Finance Memory Agent) by adding comprehensive evaluation capabilities:

- **Foundation**: Uses the finance memory agent from Concept 1 as the base system
- **Enhancement**: Adds LlamaIndex RAG for document retrieval and indexing  
- **Evaluation**: Implements the top 3 agentic AI metrics used in production

## 📊 Top 3 Agentic RAG Metrics

1. **🎯 Factual Accuracy** (40% weight)
   - LLM-based correctness scoring against golden standard answers
   - Critical for ensuring reliable financial advice

2. **📝 Citation/Source Compliance** (30% weight) 
   - Source attribution and evidence quality assessment
   - Essential for regulatory compliance in financial services

3. **🔍 Retrieval Relevance** (30% weight)
   - Quality of document retrieval using LlamaIndex
   - Measured with precision/recall metrics

## �️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Finance Memory │    │  LlamaIndex RAG │    │  Evaluation     │
│  Agent (C1)     │───▶│  Document       │───▶│  Metrics        │
│                 │    │  Retrieval      │    │  (Top 3)        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                        │                        │
        ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Persistent     │    │  Banking Policy │    │  Performance    │
│  Memory Store   │    │  Documents      │    │  Analytics      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## � Files Overview

- **enhanced_agent_evaluation.ipynb**: Complete evaluation framework integrating Concept 1
- **generate_golden_dataset.py**: Creates 50 labeled Q&A pairs for evaluation
- **data/banking_qa_golden_dataset.csv**: Golden standard questions and answers
- **data/banking_policy_documents.json**: Banking policy knowledge base
- **requirements.txt**: Dependencies including LlamaIndex
- **.env.template**: Environment variables setup

## 🚀 Quick Start

### Prerequisites
- Complete **Concept 1** (Finance Memory Agent)
- OpenAI API key

### Setup
**Note**: This lesson uses the consolidated requirements.txt from the project root directory.

```bash
# Install dependencies
pip install -r ../../../requirements.txt

# Configure environment
cp .env.template .env
# Add your OPENAI_API_KEY to .env

# Generate golden dataset (if not already done)
python generate_golden_dataset.py

# Run evaluation
jupyter notebook enhanced_agent_evaluation.ipynb
```

## 📈 What You'll Learn

1. **Production Evaluation**: Industry-standard metrics for agentic AI systems
2. **RAG Integration**: How to combine memory with document retrieval
3. **Performance Analysis**: Comprehensive analytics and improvement recommendations
4. **Financial Compliance**: Citation requirements for banking applications
5. **Memory + RAG Synergy**: Benefits of persistent memory with dynamic retrieval

## 🧪 Evaluation Process

1. **Memory Integration**: Import finance agent from Concept 1
2. **RAG Setup**: Initialize LlamaIndex with banking policy documents
3. **Golden Dataset**: Load 50 carefully crafted Q&A pairs
4. **Metric Evaluation**: Run all three metrics on each question
5. **Performance Analysis**: Generate insights and recommendations

## � Expected Outcomes

- **Composite Score**: Weighted average across all three metrics
- **Category Analysis**: Performance breakdown by banking domain
- **Retrieval Analytics**: Precision/recall for document retrieval
- **Improvement Recommendations**: Actionable suggestions for optimization
- **Token Efficiency**: Cost analysis for production deployment

## 🔗 Integration Benefits

By building on Concept 1, students will:
- See how memory enhances RAG performance
- Understand evaluation in context of complete systems
- Learn production-ready assessment techniques
- Experience end-to-end agentic AI development

## 💡 Production Considerations

This evaluation framework is designed for real-world deployment:
- **Regulatory Compliance**: Citation tracking for financial services
- **Cost Optimization**: Token usage monitoring and efficiency metrics
- **A/B Testing**: Framework supports comparing different agent configurations
- **Continuous Improvement**: Metrics can be used for ongoing optimization

**Time Investment**: ~15-20 minutes (assuming Concept 1 is complete)
**Domain**: Banking policies with persistent memory integration
**Framework**: LlamaIndex + OpenAI + Custom evaluation metrics
