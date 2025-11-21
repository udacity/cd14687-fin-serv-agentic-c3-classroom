#!/usr/bin/env python3
"""
Database Setup Script for Finance AI Agent Demo

This script creates a comprehensive SQLite database with realistic financial data
for testing the Database AI Agent. Run this script to generate the finance_demo.db
file that will be used by the notebook.

Usage:
    python setup_database.py
"""

import sqlite3
from datetime import datetime, timedelta
import random
import os

def create_comprehensive_finance_database():
    """Create a comprehensive finance database with realistic test data"""
    
    # Remove existing database if it exists
    if os.path.exists("finance_demo.db"):
        os.remove("finance_demo.db")
    
    # Connect to SQLite database
    conn = sqlite3.connect("finance_demo.db")
    cursor = conn.cursor()
    
    print("🔧 Creating finance database tables...")
    
    # Create tables
    cursor.execute("""
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        department TEXT NOT NULL,
        cost_center TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE departments (
        department TEXT PRIMARY KEY,
        cost_center_manager TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE merchants (
        merchant_id INTEGER PRIMARY KEY,
        merchant_name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE cards (
        card_id INTEGER PRIMARY KEY,
        employee_id INTEGER NOT NULL,
        last4 TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE transactions (
        txn_id INTEGER PRIMARY KEY,
        card_id INTEGER NOT NULL,
        merchant_id INTEGER NOT NULL,
        txn_time DATETIME NOT NULL,
        amount_usd REAL NOT NULL,
        currency_code TEXT DEFAULT 'USD',
        city TEXT,
        channel TEXT,
        FOREIGN KEY (card_id) REFERENCES cards(card_id),
        FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id)
    )
    """)
    
    print("📊 Inserting comprehensive test data...")
    
    # Insert departments
    departments_data = [
        ('Engineering', 'Alice Johnson'),
        ('Marketing', 'Bob Smith'),
        ('Sales', 'Carol Davis'),
        ('Finance', 'Eva Brown'),
        ('Operations', 'Frank Wilson'),
        ('HR', 'Grace Lee'),
        ('Product', 'Henry Chen'),
        ('Legal', 'Ivy Rodriguez')
    ]
    cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments_data)
    
    # Insert employees (more comprehensive list)
    employees_data = [
        (1, 'Alice Johnson', 'Engineering', 'ENG-001'),
        (2, 'Bob Smith', 'Marketing', 'MKT-001'),
        (3, 'Carol Davis', 'Sales', 'SAL-001'),
        (4, 'David Wilson', 'Engineering', 'ENG-001'),
        (5, 'Eva Brown', 'Finance', 'FIN-001'),
        (6, 'Frank Wilson', 'Operations', 'OPS-001'),
        (7, 'Grace Lee', 'HR', 'HR-001'),
        (8, 'Henry Chen', 'Product', 'PRD-001'),
        (9, 'Ivy Rodriguez', 'Legal', 'LEG-001'),
        (10, 'Jack Thompson', 'Engineering', 'ENG-001'),
        (11, 'Karen Miller', 'Marketing', 'MKT-001'),
        (12, 'Liam O\'Connor', 'Sales', 'SAL-001'),
        (13, 'Maya Patel', 'Finance', 'FIN-001'),
        (14, 'Noah Kim', 'Operations', 'OPS-001'),
        (15, 'Olivia Zhang', 'Product', 'PRD-001')
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees_data)
    
    # Insert merchants (comprehensive list)
    merchants_data = [
        (1, 'Uber', 'Travel'),
        (2, 'Delta Airlines', 'Travel'),
        (3, 'Starbucks', 'Dining'),
        (4, 'Amazon', 'Office Supplies'),
        (5, 'Marriott', 'Travel'),
        (6, 'Southwest Airlines', 'Travel'),
        (7, 'Hertz', 'Travel'),
        (8, 'Expedia', 'Travel'),
        (9, 'McDonald\'s', 'Dining'),
        (10, 'Subway', 'Dining'),
        (11, 'Office Depot', 'Office Supplies'),
        (12, 'Best Buy', 'Electronics'),
        (13, 'Zoom', 'Software'),
        (14, 'Microsoft', 'Software'),
        (15, 'Google Cloud', 'Software'),
        (16, 'Slack', 'Software'),
        (17, 'Salesforce', 'Software'),
        (18, 'WeWork', 'Office Space'),
        (19, 'FedEx', 'Shipping'),
        (20, 'UPS', 'Shipping')
    ]
    cursor.executemany("INSERT INTO merchants VALUES (?, ?, ?)", merchants_data)
    
    # Insert cards (one per employee)
    cards_data = []
    for emp_id in range(1, 16):
        card_last4 = f"{random.randint(1000, 9999)}"
        cards_data.append((emp_id, emp_id, card_last4, 'Active'))
    cursor.executemany("INSERT INTO cards VALUES (?, ?, ?, ?)", cards_data)
    
    # Generate comprehensive transaction data
    print("💳 Generating realistic transaction data...")
    
    # Transaction patterns by merchant category
    category_patterns = {
        'Travel': {'min_amount': 50.0, 'max_amount': 2500.0, 'frequency': 0.3},
        'Dining': {'min_amount': 8.0, 'max_amount': 150.0, 'frequency': 0.5},
        'Office Supplies': {'min_amount': 15.0, 'max_amount': 500.0, 'frequency': 0.2},
        'Electronics': {'min_amount': 100.0, 'max_amount': 3000.0, 'frequency': 0.1},
        'Software': {'min_amount': 50.0, 'max_amount': 1000.0, 'frequency': 0.4},
        'Office Space': {'min_amount': 200.0, 'max_amount': 5000.0, 'frequency': 0.1},
        'Shipping': {'min_amount': 10.0, 'max_amount': 200.0, 'frequency': 0.3}
    }
    
    cities = ['San Francisco', 'New York', 'Los Angeles', 'Chicago', 'Boston', 
              'Seattle', 'Austin', 'Denver', 'Miami', 'Atlanta']
    channels = ['Online', 'In-person', 'Mobile']
    
    transactions_data = []
    txn_id = 1
    
    # Generate transactions over the past 120 days
    for days_ago in range(120, 0, -1):
        transaction_date = datetime.now() - timedelta(days=days_ago)
        
        # Generate 3-8 transactions per day
        daily_txns = random.randint(3, 8)
        
        for _ in range(daily_txns):
            # Random employee and corresponding card
            card_id = random.randint(1, 15)
            
            # Random merchant
            merchant_id = random.randint(1, 20)
            merchant = next(m for m in merchants_data if m[0] == merchant_id)
            category = merchant[2]
            
            # Amount based on category pattern
            pattern = category_patterns.get(category, {'min_amount': 20.0, 'max_amount': 200.0})
            amount = round(random.uniform(pattern['min_amount'], pattern['max_amount']), 2)
            
            # Add some high-value transactions for testing
            if random.random() < 0.05:  # 5% chance of high-value transaction
                amount = round(random.uniform(500.0, 2000.0), 2)
            
            # Random city and channel
            city = random.choice(cities)
            channel = random.choice(channels)
            
            # Add some time variation to the date
            hours_offset = random.randint(0, 23)
            minutes_offset = random.randint(0, 59)
            txn_datetime = transaction_date.replace(hour=hours_offset, minute=minutes_offset)
            
            transactions_data.append((
                txn_id, card_id, merchant_id, 
                txn_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                amount, 'USD', city, channel
            ))
            txn_id += 1
    
    # Insert transactions in batches for better performance
    cursor.executemany(
        "INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        transactions_data
    )
    
    # Commit all changes
    conn.commit()
    
    # Print summary statistics
    cursor.execute("SELECT COUNT(*) FROM transactions")
    txn_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT SUM(amount_usd) FROM transactions")
    total_amount = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM employees")
    emp_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM merchants")
    merchant_count = cursor.fetchone()[0]
    
    print(f"\n✅ Database creation complete!")
    print(f"📊 Summary Statistics:")
    print(f"   • {emp_count} employees across {len(departments_data)} departments")
    print(f"   • {merchant_count} merchants across various categories")
    print(f"   • {txn_count:,} transactions generated")
    print(f"   • Total transaction volume: ${total_amount:,.2f}")
    print(f"   • Database file: finance_demo.db ({os.path.getsize('finance_demo.db'):,} bytes)")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    create_comprehensive_finance_database()
