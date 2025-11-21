#!/usr/bin/env python3
"""
Generate Golden Dataset for Banking Q&A Agent Evaluation

This script creates a comprehensive labeled dataset of 50 banking policy questions
with ground truth answers, relevant document sources, and evaluation metadata.

Usage:
    python generate_golden_dataset.py

Output:
    - data/banking_qa_golden_dataset.csv
    - data/banking_policy_documents.json
"""

import json
import csv
import random
from typing import List, Dict, Any
from dataclasses import dataclass
import os

@dataclass
class PolicyDocument:
    """Banking policy document for RAG retrieval"""
    doc_id: str
    title: str
    content: str
    category: str
    relevance_keywords: List[str]

@dataclass
class GoldenQA:
    """Golden standard Q&A item for evaluation"""
    question_id: str
    question: str
    correct_answer: str
    relevant_doc_ids: List[str]
    category: str
    difficulty: str
    should_have_citation: bool
    expected_retrieval_keywords: List[str]

class BankingDatasetGenerator:
    """Generate realistic banking Q&A evaluation dataset"""
    
    def __init__(self):
        self.policy_documents = self._create_policy_documents()
        self.golden_qa_items = []
    
    def _create_policy_documents(self) -> List[PolicyDocument]:
        """Create a set of banking policy documents for RAG retrieval"""
        
        documents = [
            PolicyDocument(
                doc_id="wire_transfer_policy",
                title="Wire Transfer Services and Cut-off Times",
                content="Domestic wire transfers must be submitted by 2:00 PM EST for same-day processing. International wires require submission by 12:00 PM EST. Weekend and holiday wires are processed on the next business day. Fees apply: $25 domestic, $45 international outgoing.",
                category="wire_transfers",
                relevance_keywords=["wire", "transfer", "cutoff", "same-day", "international", "domestic", "fee"]
            ),
            PolicyDocument(
                doc_id="premier_checking_benefits",
                title="Premier Checking Account Benefits",
                content="Premier Checking customers receive unlimited ATM fee reimbursements worldwide, free wire transfers, priority customer service, and waived monthly maintenance fees with $25,000 minimum balance or $10,000 direct deposit.",
                category="account_benefits",
                relevance_keywords=["premier", "checking", "atm", "reimbursement", "unlimited", "benefits", "maintenance"]
            ),
            PolicyDocument(
                doc_id="mobile_deposit_limits",
                title="Mobile Check Deposit Limits and Policies",
                content="New accounts (less than 90 days): $2,500 daily limit, $5,000 weekly limit. Established accounts: $10,000 daily limit, $25,000 weekly limit. Business accounts: $50,000 daily limit. Deposits must be made before 9:00 PM EST for next-day availability.",
                category="deposit_services",
                relevance_keywords=["mobile", "deposit", "check", "limit", "daily", "weekly", "new", "established"]
            ),
            PolicyDocument(
                doc_id="overdraft_nsf_fees",
                title="Overdraft and NSF Fee Schedule",
                content="Overdraft fee: $35 per item, maximum 4 fees per day ($140). NSF fee: $35 per returned item. Fees waived for customers with $500+ monthly direct deposit or $1,500 average daily balance. Overdraft protection available for $10/month.",
                category="fees_charges",
                relevance_keywords=["overdraft", "nsf", "fee", "returned", "waived", "direct deposit", "protection"]
            ),
            PolicyDocument(
                doc_id="savings_account_rates",
                title="Savings Account Interest Rates and Terms",
                content="Standard Savings: 0.01% APY on all balances. High-Yield Savings: 4.50% APY on balances up to $50,000, 0.50% APY on amounts above. Premium Savings: 5.00% APY with $100,000 minimum balance. Rates updated monthly.",
                category="savings_products",
                relevance_keywords=["savings", "interest", "rate", "apy", "high-yield", "premium", "balance"]
            ),
            PolicyDocument(
                doc_id="credit_card_rewards",
                title="Credit Card Rewards and Benefits Program",
                content="Earn 2% cash back on all purchases, 3% on gas and groceries, 5% on rotating quarterly categories. No annual fee. Rewards redeemed as statement credit, direct deposit, or gift cards. Foreign transaction fees: 0%. Purchase protection and extended warranty included.",
                category="credit_products",
                relevance_keywords=["credit card", "rewards", "cash back", "categories", "foreign", "protection"]
            ),
            PolicyDocument(
                doc_id="atm_network_fees",
                title="ATM Network Access and Fee Structure",
                content="Free access to 55,000+ ATMs nationwide through our network. Out-of-network ATM fees: $3.50 per transaction. International ATM fees: $5.00 per transaction plus 3% foreign exchange fee. Premier customers receive unlimited fee reimbursements.",
                category="atm_services",
                relevance_keywords=["atm", "network", "fee", "out-of-network", "international", "reimbursement", "access"]
            ),
            PolicyDocument(
                doc_id="loan_interest_rates",
                title="Personal and Auto Loan Interest Rates",
                content="Personal loans: 6.99% - 24.99% APR based on creditworthiness, terms 2-7 years. Auto loans: 3.49% - 18.99% APR for new vehicles, 4.49% - 19.99% APR for used vehicles. Home equity loans: Prime + 0.25% variable rate.",
                category="lending_products",
                relevance_keywords=["loan", "personal", "auto", "interest", "apr", "credit", "home equity"]
            ),
            PolicyDocument(
                doc_id="business_account_fees",
                title="Business Banking Account Fees and Services",
                content="Business Checking: $15/month, waived with $5,000 balance. Transaction fees: $0.50 per debit after 200 free transactions. Wire fees: $30 domestic, $50 international. Cash management services available. Online banking and bill pay included.",
                category="business_services",
                relevance_keywords=["business", "checking", "transaction", "wire", "cash management", "online banking"]
            ),
            PolicyDocument(
                doc_id="security_fraud_protection",
                title="Account Security and Fraud Protection Policies",
                content="24/7 fraud monitoring on all accounts. Zero liability protection for unauthorized transactions reported within 60 days. Account alerts via text, email, or mobile app. Two-factor authentication required for online banking. Identity theft resolution services included.",
                category="security_services",
                relevance_keywords=["security", "fraud", "protection", "unauthorized", "alerts", "authentication", "identity theft"]
            )
        ]
        
        return documents
    
    def _generate_wire_transfer_questions(self) -> List[GoldenQA]:
        """Generate wire transfer related questions"""
        questions = [
            GoldenQA(
                question_id="wire_001",
                question="What's the cut-off time for same-day domestic wire transfers?",
                correct_answer="2:00 PM EST",
                relevant_doc_ids=["wire_transfer_policy"],
                category="wire_transfers",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["wire", "domestic", "cutoff", "same-day"]
            ),
            GoldenQA(
                question_id="wire_002", 
                question="What's the fee for outgoing international wire transfers?",
                correct_answer="$45 for international outgoing wire transfers",
                relevant_doc_ids=["wire_transfer_policy"],
                category="wire_transfers",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["wire", "international", "fee", "outgoing"]
            ),
            GoldenQA(
                question_id="wire_003",
                question="When are weekend wire transfers processed?",
                correct_answer="Weekend and holiday wires are processed on the next business day",
                relevant_doc_ids=["wire_transfer_policy"],
                category="wire_transfers", 
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["wire", "weekend", "holiday", "business day"]
            ),
            GoldenQA(
                question_id="wire_004",
                question="What's the difference between domestic and international wire cut-off times?",
                correct_answer="Domestic wires: 2:00 PM EST, International wires: 12:00 PM EST for same-day processing",
                relevant_doc_ids=["wire_transfer_policy"],
                category="wire_transfers",
                difficulty="medium", 
                should_have_citation=True,
                expected_retrieval_keywords=["wire", "domestic", "international", "cutoff", "time"]
            ),
            GoldenQA(
                question_id="wire_005",
                question="How much does it cost to send a domestic wire transfer?",
                correct_answer="$25 for domestic wire transfers",
                relevant_doc_ids=["wire_transfer_policy"],
                category="wire_transfers",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["wire", "domestic", "fee", "cost"]
            )
        ]
        return questions
    
    def _generate_account_benefits_questions(self) -> List[GoldenQA]:
        """Generate account benefits related questions"""
        questions = [
            GoldenQA(
                question_id="benefits_001",
                question="How many ATM fee reimbursements do Premier Checking customers get?",
                correct_answer="Unlimited ATM fee reimbursements worldwide",
                relevant_doc_ids=["premier_checking_benefits"],
                category="account_benefits",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "atm", "reimbursement", "unlimited"]
            ),
            GoldenQA(
                question_id="benefits_002",
                question="What's the minimum balance requirement to waive Premier Checking monthly fees?",
                correct_answer="$25,000 minimum balance or $10,000 direct deposit",
                relevant_doc_ids=["premier_checking_benefits"],
                category="account_benefits",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "minimum", "balance", "waived", "monthly", "direct deposit"]
            ),
            GoldenQA(
                question_id="benefits_003",
                question="Do Premier Checking customers get free wire transfers?",
                correct_answer="Yes, Premier Checking customers receive free wire transfers",
                relevant_doc_ids=["premier_checking_benefits"],
                category="account_benefits",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "wire", "free", "transfer"]
            ),
            GoldenQA(
                question_id="benefits_004",
                question="What customer service benefits do Premier customers receive?",
                correct_answer="Priority customer service",
                relevant_doc_ids=["premier_checking_benefits"],
                category="account_benefits",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "customer", "service", "priority"]
            ),
            GoldenQA(
                question_id="benefits_005",
                question="What are all the benefits of Premier Checking?",
                correct_answer="Unlimited ATM fee reimbursements worldwide, free wire transfers, priority customer service, and waived monthly maintenance fees",
                relevant_doc_ids=["premier_checking_benefits"],
                category="account_benefits",
                difficulty="hard",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "benefits", "atm", "wire", "service", "maintenance"]
            )
        ]
        return questions
    
    def _generate_deposit_questions(self) -> List[GoldenQA]:
        """Generate mobile deposit related questions"""
        questions = [
            GoldenQA(
                question_id="deposit_001",
                question="What's the daily mobile check deposit limit for new accounts?",
                correct_answer="$2,500 daily limit for new accounts (less than 90 days)",
                relevant_doc_ids=["mobile_deposit_limits"],
                category="deposit_services",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["mobile", "deposit", "daily", "limit", "new"]
            ),
            GoldenQA(
                question_id="deposit_002",
                question="What's the weekly mobile deposit limit for established accounts?",
                correct_answer="$25,000 weekly limit for established accounts",
                relevant_doc_ids=["mobile_deposit_limits"],
                category="deposit_services",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["mobile", "deposit", "weekly", "limit", "established"]
            ),
            GoldenQA(
                question_id="deposit_003",
                question="When do mobile deposits need to be made for next-day availability?",
                correct_answer="Deposits must be made before 9:00 PM EST for next-day availability",
                relevant_doc_ids=["mobile_deposit_limits"],
                category="deposit_services",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["mobile", "deposit", "cutoff", "availability", "next-day"]
            ),
            GoldenQA(
                question_id="deposit_004",
                question="What's the mobile deposit limit for business accounts?",
                correct_answer="$50,000 daily limit for business accounts",
                relevant_doc_ids=["mobile_deposit_limits"],
                category="deposit_services",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["mobile", "deposit", "business", "daily", "limit"]
            ),
            GoldenQA(
                question_id="deposit_005",
                question="How do mobile deposit limits differ between new and established accounts?",
                correct_answer="New accounts: $2,500 daily/$5,000 weekly. Established accounts: $10,000 daily/$25,000 weekly",
                relevant_doc_ids=["mobile_deposit_limits"],
                category="deposit_services",
                difficulty="hard",
                should_have_citation=True,
                expected_retrieval_keywords=["mobile", "deposit", "limit", "new", "established", "daily", "weekly"]
            )
        ]
        return questions
    
    def _generate_fees_questions(self) -> List[GoldenQA]:
        """Generate fee-related questions"""
        questions = [
            GoldenQA(
                question_id="fees_001",
                question="What's the overdraft fee amount?",
                correct_answer="$35 per item, maximum 4 fees per day ($140)",
                relevant_doc_ids=["overdraft_nsf_fees"],
                category="fees_charges",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["overdraft", "fee", "amount"]
            ),
            GoldenQA(
                question_id="fees_002",
                question="When are overdraft fees waived?",
                correct_answer="Fees waived for customers with $500+ monthly direct deposit or $1,500 average daily balance",
                relevant_doc_ids=["overdraft_nsf_fees"],
                category="fees_charges",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["overdraft", "fee", "waived", "direct deposit", "balance"]
            ),
            GoldenQA(
                question_id="fees_003",
                question="What's the NSF fee for returned items?",
                correct_answer="$35 per returned item",
                relevant_doc_ids=["overdraft_nsf_fees"],
                category="fees_charges",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["nsf", "fee", "returned", "item"]
            ),
            GoldenQA(
                question_id="fees_004",
                question="How much does overdraft protection cost?",
                correct_answer="$10 per month for overdraft protection",
                relevant_doc_ids=["overdraft_nsf_fees"],
                category="fees_charges",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["overdraft", "protection", "cost", "monthly"]
            ),
            GoldenQA(
                question_id="fees_005",
                question="What's the maximum overdraft fees per day?",
                correct_answer="Maximum 4 fees per day ($140 total)",
                relevant_doc_ids=["overdraft_nsf_fees"],
                category="fees_charges",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["overdraft", "fee", "maximum", "daily"]
            )
        ]
        return questions
    
    def _generate_atm_questions(self) -> List[GoldenQA]:
        """Generate ATM-related questions"""
        questions = [
            GoldenQA(
                question_id="atm_001",
                question="What's the out-of-network ATM fee?",
                correct_answer="$3.50 per transaction for out-of-network ATMs",
                relevant_doc_ids=["atm_network_fees"],
                category="atm_services",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["atm", "out-of-network", "fee"]
            ),
            GoldenQA(
                question_id="atm_002",
                question="How many ATMs are in the free network?",
                correct_answer="55,000+ ATMs nationwide through our network",
                relevant_doc_ids=["atm_network_fees"],
                category="atm_services",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["atm", "network", "free", "nationwide"]
            ),
            GoldenQA(
                question_id="atm_003",
                question="What are the international ATM fees?",
                correct_answer="$5.00 per transaction plus 3% foreign exchange fee",
                relevant_doc_ids=["atm_network_fees"],
                category="atm_services",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["atm", "international", "fee", "foreign", "exchange"]
            ),
            GoldenQA(
                question_id="atm_004",
                question="Do Premier customers pay ATM fees?",
                correct_answer="No, Premier customers receive unlimited fee reimbursements",
                relevant_doc_ids=["atm_network_fees", "premier_checking_benefits"],
                category="atm_services",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "atm", "fee", "reimbursement"]
            )
        ]
        return questions
    
    def _generate_mixed_difficulty_questions(self) -> List[GoldenQA]:
        """Generate questions with varying difficulty and cross-category requirements"""
        questions = [
            GoldenQA(
                question_id="mixed_001",
                question="What savings account has the highest interest rate?",
                correct_answer="Premium Savings: 5.00% APY with $100,000 minimum balance",
                relevant_doc_ids=["savings_account_rates"],
                category="savings_products",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["savings", "highest", "interest", "rate", "premium"]
            ),
            GoldenQA(
                question_id="mixed_002",
                question="What credit card rewards does the bank offer?",
                correct_answer="2% cash back on all purchases, 3% on gas and groceries, 5% on rotating quarterly categories",
                relevant_doc_ids=["credit_card_rewards"],
                category="credit_products",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["credit card", "rewards", "cash back", "categories"]
            ),
            GoldenQA(
                question_id="mixed_003",
                question="What fraud protection does the bank provide?",
                correct_answer="24/7 fraud monitoring, zero liability protection for unauthorized transactions reported within 60 days, account alerts, two-factor authentication",
                relevant_doc_ids=["security_fraud_protection"],
                category="security_services",
                difficulty="hard",
                should_have_citation=True,
                expected_retrieval_keywords=["fraud", "protection", "monitoring", "unauthorized", "alerts"]
            ),
            GoldenQA(
                question_id="mixed_004",
                question="What's the APR range for personal loans?",
                correct_answer="6.99% - 24.99% APR based on creditworthiness, terms 2-7 years",
                relevant_doc_ids=["loan_interest_rates"],
                category="lending_products",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["personal", "loan", "apr", "rate"]
            ),
            GoldenQA(
                question_id="mixed_005",
                question="What are the business checking account fees?",
                correct_answer="$15/month, waived with $5,000 balance. Transaction fees: $0.50 per debit after 200 free transactions",
                relevant_doc_ids=["business_account_fees"],
                category="business_services",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["business", "checking", "fee", "monthly", "transaction"]
            ),
            GoldenQA(
                question_id="mixed_006",
                question="What cryptocurrency services does the bank offer?",
                correct_answer="I don't have that information",
                relevant_doc_ids=[],
                category="unknown",
                difficulty="easy",
                should_have_citation=False,
                expected_retrieval_keywords=["cryptocurrency", "crypto", "bitcoin"]
            ),
            GoldenQA(
                question_id="mixed_007",
                question="What are the foreign transaction fees on the credit card?",
                correct_answer="0% foreign transaction fees",
                relevant_doc_ids=["credit_card_rewards"],
                category="credit_products",
                difficulty="easy",
                should_have_citation=True,
                expected_retrieval_keywords=["credit card", "foreign", "transaction", "fee"]
            ),
            GoldenQA(
                question_id="mixed_008",
                question="Compare Premier Checking ATM benefits with standard ATM fees",
                correct_answer="Premier Checking: unlimited ATM fee reimbursements. Standard: $3.50 out-of-network, $5.00 international plus 3% exchange fee",
                relevant_doc_ids=["premier_checking_benefits", "atm_network_fees"],
                category="account_comparison",
                difficulty="hard",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "atm", "fee", "reimbursement", "out-of-network"]
            ),
            # Add more complex multi-category questions
            GoldenQA(
                question_id="complex_001",
                question="If I have Premier Checking, what wire transfer and ATM benefits do I get?",
                correct_answer="Free wire transfers and unlimited ATM fee reimbursements worldwide",
                relevant_doc_ids=["premier_checking_benefits"],
                category="account_benefits",
                difficulty="medium",
                should_have_citation=True,
                expected_retrieval_keywords=["premier", "wire", "atm", "free", "reimbursement"]
            ),
            GoldenQA(
                question_id="complex_002",
                question="What's the difference between NSF and overdraft fees?",
                correct_answer="Both are $35 per item. Overdraft covers the transaction, NSF returns it unpaid. Maximum 4 overdraft fees per day.",
                relevant_doc_ids=["overdraft_nsf_fees"],
                category="fees_charges",
                difficulty="hard",
                should_have_citation=True,
                expected_retrieval_keywords=["nsf", "overdraft", "fee", "difference", "returned"]
            )
        ]
        return questions
    
    def generate_complete_dataset(self) -> List[GoldenQA]:
        """Generate the complete 50-item golden dataset"""
        
        all_questions = []
        
        # Generate questions by category
        all_questions.extend(self._generate_wire_transfer_questions())  # 5 questions
        all_questions.extend(self._generate_account_benefits_questions())  # 5 questions  
        all_questions.extend(self._generate_deposit_questions())  # 5 questions
        all_questions.extend(self._generate_fees_questions())  # 5 questions
        all_questions.extend(self._generate_atm_questions())  # 4 questions
        all_questions.extend(self._generate_mixed_difficulty_questions())  # 10 questions
        
        # Generate additional questions to reach 50 total
        additional_questions = self._generate_additional_questions(16)  # 16 more questions
        all_questions.extend(additional_questions)
        
        # Shuffle to avoid category clustering
        random.shuffle(all_questions)
        
        return all_questions[:50]  # Ensure exactly 50 questions
    
    def _generate_additional_questions(self, count: int) -> List[GoldenQA]:
        """Generate additional questions to reach target count"""
        templates = [
            # Savings questions
            ("savings_extra_001", "What's the APY for Standard Savings accounts?", "0.01% APY on all balances", ["savings_account_rates"], "savings_products", "easy", ["savings", "apy", "standard"]),
            ("savings_extra_002", "What's the High-Yield Savings rate for balances over $50,000?", "0.50% APY on amounts above $50,000", ["savings_account_rates"], "savings_products", "medium", ["high-yield", "savings", "balance", "over"]),
            ("savings_extra_003", "How often are savings account rates updated?", "Rates updated monthly", ["savings_account_rates"], "savings_products", "easy", ["savings", "rates", "updated", "monthly"]),
            
            # Credit card questions  
            ("credit_extra_001", "What's the annual fee for the rewards credit card?", "No annual fee", ["credit_card_rewards"], "credit_products", "easy", ["credit card", "annual", "fee"]),
            ("credit_extra_002", "What purchase protections come with the credit card?", "Purchase protection and extended warranty included", ["credit_card_rewards"], "credit_products", "medium", ["credit card", "purchase", "protection", "warranty"]),
            ("credit_extra_003", "How can I redeem credit card rewards?", "Statement credit, direct deposit, or gift cards", ["credit_card_rewards"], "credit_products", "easy", ["credit card", "rewards", "redeem"]),
            
            # Business banking questions
            ("business_extra_001", "What's included with business checking?", "Online banking and bill pay included", ["business_account_fees"], "business_services", "easy", ["business", "checking", "included", "online"]),
            ("business_extra_002", "What are the business wire transfer fees?", "$30 domestic, $50 international wire fees for business accounts", ["business_account_fees"], "business_services", "medium", ["business", "wire", "fee", "domestic", "international"]),
            ("business_extra_003", "How many free transactions do business accounts get?", "200 free transactions, then $0.50 per debit", ["business_account_fees"], "business_services", "medium", ["business", "transaction", "free", "debit"]),
            
            # Loan questions
            ("loan_extra_001", "What's the APR range for auto loans on new vehicles?", "3.49% - 18.99% APR for new vehicles", ["loan_interest_rates"], "lending_products", "easy", ["auto", "loan", "apr", "new", "vehicle"]),
            ("loan_extra_002", "What's the rate for home equity loans?", "Prime + 0.25% variable rate for home equity loans", ["loan_interest_rates"], "lending_products", "medium", ["home", "equity", "loan", "rate", "prime"]),
            ("loan_extra_003", "What are personal loan terms?", "Personal loans: terms 2-7 years", ["loan_interest_rates"], "lending_products", "easy", ["personal", "loan", "terms", "years"]),
            
            # Security questions
            ("security_extra_001", "How long do I have to report unauthorized transactions?", "Within 60 days for zero liability protection", ["security_fraud_protection"], "security_services", "medium", ["unauthorized", "transaction", "report", "days"]),
            ("security_extra_002", "What authentication is required for online banking?", "Two-factor authentication required for online banking", ["security_fraud_protection"], "security_services", "easy", ["authentication", "online", "banking", "two-factor"]),
            ("security_extra_003", "Does the bank provide identity theft services?", "Yes, identity theft resolution services included", ["security_fraud_protection"], "security_services", "easy", ["identity", "theft", "services", "resolution"]),
            
            # Edge cases and unknowns
            ("unknown_extra_001", "What are the mortgage refinancing rates?", "I don't have that information", [], "unknown", "easy", ["mortgage", "refinancing", "rates"]),
        ]
        
        questions = []
        for i in range(min(count, len(templates))):
            template = templates[i]
            questions.append(GoldenQA(
                question_id=template[0],
                question=template[1],
                correct_answer=template[2],
                relevant_doc_ids=template[3],
                category=template[4],
                difficulty=template[5],
                should_have_citation=len(template[3]) > 0,
                expected_retrieval_keywords=template[6]
            ))
        
        return questions
    
    def save_dataset(self, output_dir: str = "data"):
        """Save the complete dataset to CSV and JSON files"""
        
        # Generate the complete dataset
        golden_questions = self.generate_complete_dataset()
        
        # Save questions to CSV
        csv_file = os.path.join(output_dir, "banking_qa_golden_dataset.csv")
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow([
                'question_id', 'question', 'correct_answer', 'relevant_doc_ids', 
                'category', 'difficulty', 'should_have_citation', 'expected_retrieval_keywords'
            ])
            
            # Write data rows
            for qa in golden_questions:
                writer.writerow([
                    qa.question_id,
                    qa.question,
                    qa.correct_answer,
                    '|'.join(qa.relevant_doc_ids),  # Join with | separator
                    qa.category,
                    qa.difficulty,
                    qa.should_have_citation,
                    '|'.join(qa.expected_retrieval_keywords)  # Join with | separator
                ])
        
        # Save policy documents to JSON
        docs_file = os.path.join(output_dir, "banking_policy_documents.json")
        docs_data = []
        for doc in self.policy_documents:
            docs_data.append({
                'doc_id': doc.doc_id,
                'title': doc.title,
                'content': doc.content,
                'category': doc.category,
                'relevance_keywords': doc.relevance_keywords
            })
        
        with open(docs_file, 'w', encoding='utf-8') as f:
            json.dump(docs_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Generated {len(golden_questions)} Q&A pairs")
        print(f"📁 Dataset saved to: {csv_file}")
        print(f"📁 Documents saved to: {docs_file}")
        print(f"📊 Dataset statistics:")
        print(f"   - Categories: {len(set(qa.category for qa in golden_questions))}")
        print(f"   - With citations: {sum(1 for qa in golden_questions if qa.should_have_citation)}")
        print(f"   - Difficulty levels: {len(set(qa.difficulty for qa in golden_questions))}")
        
        return csv_file, docs_file

def main():
    """Main function to generate the golden dataset"""
    print("🏗️ Generating Banking Q&A Golden Dataset...")
    print("=" * 50)
    
    # Create output directory
    os.makedirs("data", exist_ok=True)
    
    # Generate dataset
    generator = BankingDatasetGenerator()
    csv_file, docs_file = generator.save_dataset()
    
    print("\n🎯 Dataset Generation Complete!")
    print("Ready for evaluation framework testing.")

if __name__ == "__main__":
    main()
