# Concept 2: Evaluating AI Agents - Starter Code

**Objective**: Learn to evaluate AI agents using industry-standard agentic RAG metrics by building upon the finance memory agent from Concept 1.

## 🎯 Learning Focus

This exercise focuses on the **evaluation methodology** rather than agent building. You'll learn:
- **Industry-standard evaluation metrics** for agentic AI systems
- **RAG evaluation techniques** using LlamaIndex
- **Metric implementation** and scoring systems
- **Production-ready assessment** frameworks

## 📊 Top 3 Agentic RAG Metrics (Learn to Implement)

1. **🎯 Factual Accuracy** (40% weight) - LLM-based correctness scoring
2. **📝 Citation/Source Compliance** (30% weight) - Source attribution quality  
3. **🔍 Retrieval Relevance** (30% weight) - Document retrieval effectiveness

## 📂 Starter Files Structure

```
starter/
├── agent_evaluation.ipynb          # YOUR MAIN NOTEBOOK (with TODO sections)
├── requirements.txt                # Dependencies 
├── .env.template                   # Environment setup
├── README.md                      # This file
└── data/
    ├── generate_golden_dataset.py # Script to create evaluation dataset
    ├── banking_qa_golden_dataset.csv # 50 labeled Q&A pairs  
    └── banking_policy_documents.json # Banking knowledge base
```

## 🔧 Golden Dataset Generation

### About `data/generate_golden_dataset.py`

This script creates a **comprehensive labeled dataset** for evaluating banking Q&A agents:

**What it generates:**
- **50 carefully crafted questions** across banking domains
- **Ground truth answers** for each question
- **Relevant document mappings** for retrieval evaluation
- **Metadata** for comprehensive analysis

**Dataset Fields (banking_qa_golden_dataset.csv):**
- `question_id`: Unique identifier (e.g., "wire_001", "fees_003")
- `question`: The banking question to ask the agent
- `correct_answer`: Ground truth response for comparison
- `relevant_doc_ids`: Which documents should be retrieved (for RAG evaluation)
- `category`: Banking domain (wire_transfers, fees_charges, etc.)
- `difficulty`: easy, medium, hard (for stratified analysis)
- `should_have_citation`: Whether the answer requires source attribution
- `expected_retrieval_keywords`: Keywords that should trigger document retrieval

**Banking Categories Covered:**
- Wire transfers and cut-off times
- Account benefits and Premier Checking
- Mobile deposit limits and policies  
- Overdraft and NSF fees
- ATM network and fees
- Credit card rewards
- Savings account rates
- Business banking services
- Security and fraud protection
- Lending products

### How to Use the Dataset Generator

```bash
# Navigate to data directory
cd data/

# Run the generator (creates the evaluation dataset)
python generate_golden_dataset.py

# Output files:
# ✅ banking_qa_golden_dataset.csv (50 Q&A pairs)
# ✅ banking_policy_documents.json (10 policy documents)
```

**Sample Dataset Entry:**
```csv
question_id,question,correct_answer,relevant_doc_ids,category,difficulty,should_have_citation,expected_retrieval_keywords
wire_001,"What's the cut-off time for same-day domestic wire transfers?","2:00 PM EST",wire_transfer_policy,wire_transfers,easy,true,"wire|domestic|cutoff|same-day"
```

## 🚀 Quick Start

### Prerequisites
**Note**: All dependencies are managed in the project root requirements.txt file.

- Complete **Concept 1** (Finance Memory Agent) 
- OpenAI API key
- Basic understanding of RAG systems

### Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r ../../../requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.template .env
   # Edit .env and add your OPENAI_API_KEY
   ```

3. **Generate Dataset** (if not already present)
   ```bash
   cd data/
   python generate_golden_dataset.py
   cd ..
   ```

4. **Open Notebook**
   ```bash
   jupyter notebook agent_evaluation.ipynb
   ```

## 📝 What You'll Implement

The notebook contains **TODO sections** focusing on key evaluation concepts:

### 🔧 Section 1: Metric Implementation
- **TODO**: Implement factual accuracy scoring using LLM evaluation
- **TODO**: Build citation compliance checker with regex patterns
- **TODO**: Create retrieval relevance evaluator with precision/recall

### 📊 Section 2: Evaluation Framework  
- **TODO**: Load and structure the golden dataset
- **TODO**: Run comprehensive evaluation pipeline
- **TODO**: Generate evaluation reports and insights

### 💡 Section 3: Production Insights
- **TODO**: Implement cost/token efficiency analysis
- **TODO**: Create A/B testing framework structure
- **TODO**: Design monitoring metrics for production deployment

## 🎯 Expected Learning Outcomes

After completing this exercise, you will:

1. **Master Industry Metrics**: Understand the top 3 agentic AI evaluation metrics used in production
2. **RAG Evaluation Skills**: Know how to assess retrieval quality with precision/recall
3. **Financial Compliance**: Understand citation requirements for banking applications  
4. **Performance Analysis**: Analyze results by category, difficulty, and efficiency
5. **Production Readiness**: Design evaluation frameworks for real-world deployment

## 📋 Evaluation Categories

Your implementation will test the agent across these banking domains:

| Category | Questions | Example |
|----------|-----------|---------|
| wire_transfers | 5 | "What's the cut-off time for same-day domestic wires?" |
| account_benefits | 5 | "How many ATM fee reimbursements do Premier customers get?" |
| deposit_services | 5 | "What's the daily mobile deposit limit for new accounts?" |
| fees_charges | 5 | "What's the overdraft fee amount?" |
| atm_services | 4 | "What's the out-of-network ATM fee?" |
| credit_products | 3 | "What credit card rewards does the bank offer?" |
| savings_products | 3 | "What savings account has the highest interest rate?" |
| lending_products | 3 | "What's the APR range for personal loans?" |
| business_services | 3 | "What are the business checking account fees?" |
| security_services | 3 | "What fraud protection does the bank provide?" |

## 🔗 Integration with Concept 1

This evaluation validates your finance memory agent from Concept 1:
- **Memory Enhancement**: See how persistent memory improves RAG performance
- **Complete System**: Evaluate end-to-end agentic AI capabilities
- **Production Path**: Bridge from development to deployment readiness

## 💼 Why These Metrics Matter

- **Factual Accuracy**: Ensures reliable financial advice (regulatory requirement)
- **Citation Compliance**: Critical for audit trails and regulatory compliance
- **Retrieval Relevance**: Validates that the right documents are found for questions

**Time Investment**: ~15-20 minutes (focusing on evaluation concepts)
**Skill Level**: Intermediate (assumes completion of Concept 1)
**Real-world Application**: Production-ready evaluation framework for financial services
