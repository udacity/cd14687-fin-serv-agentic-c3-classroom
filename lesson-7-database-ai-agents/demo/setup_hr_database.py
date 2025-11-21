#!/usr/bin/env python3
"""
Database Setup Script for HR Recruitment AI Agent Demo

This script creates a comprehensive SQLite database with realistic HR recruitment data
for testing the Database AI Agent. Run this script to generate the hr_recruitment.db
file that will be used by the notebook.

Usage:
    python setup_hr_database.py
"""

import sqlite3
from datetime import datetime, timedelta
import random
import os

def create_hr_recruitment_database():
    """Create a comprehensive HR recruitment database with realistic test data"""
    
    # Remove existing database if it exists
    if os.path.exists("hr_recruitment.db"):
        os.remove("hr_recruitment.db")
    
    # Connect to SQLite database
    conn = sqlite3.connect("hr_recruitment.db")
    cursor = conn.cursor()
    
    print("🔧 Creating HR recruitment database tables...")
    
    # Create tables
    cursor.execute("""
    CREATE TABLE departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL,
        hiring_manager TEXT NOT NULL,
        budget_usd INTEGER NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE positions (
        position_id INTEGER PRIMARY KEY,
        department_id INTEGER NOT NULL,
        job_title TEXT NOT NULL,
        level TEXT NOT NULL,
        salary_min INTEGER NOT NULL,
        salary_max INTEGER NOT NULL,
        status TEXT NOT NULL,
        posted_date DATE NOT NULL,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE candidates (
        candidate_id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        years_experience INTEGER NOT NULL,
        current_company TEXT,
        source TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE applications (
        application_id INTEGER PRIMARY KEY,
        candidate_id INTEGER NOT NULL,
        position_id INTEGER NOT NULL,
        application_date DATE NOT NULL,
        status TEXT NOT NULL,
        resume_score INTEGER,
        FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
        FOREIGN KEY (position_id) REFERENCES positions(position_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE interviews (
        interview_id INTEGER PRIMARY KEY,
        application_id INTEGER NOT NULL,
        interview_date DATETIME NOT NULL,
        interview_type TEXT NOT NULL,
        interviewer_name TEXT NOT NULL,
        rating INTEGER,
        feedback_summary TEXT,
        FOREIGN KEY (application_id) REFERENCES applications(application_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE offers (
        offer_id INTEGER PRIMARY KEY,
        application_id INTEGER NOT NULL,
        offer_date DATE NOT NULL,
        salary_offered INTEGER NOT NULL,
        signing_bonus INTEGER,
        status TEXT NOT NULL,
        response_date DATE,
        FOREIGN KEY (application_id) REFERENCES applications(application_id)
    )
    """)
    
    print("📊 Inserting comprehensive HR test data...")
    
    # Insert departments
    departments_data = [
        (1, 'Engineering', 'Sarah Chen', 5000000),
        (2, 'Product Management', 'Michael Brown', 2000000),
        (3, 'Sales', 'Jennifer Davis', 3000000),
        (4, 'Marketing', 'David Wilson', 1500000),
        (5, 'Data Science', 'Emily Rodriguez', 2500000),
        (6, 'Customer Success', 'James Anderson', 1200000),
        (7, 'Finance', 'Lisa Taylor', 1000000),
        (8, 'HR', 'Robert Martinez', 800000)
    ]
    cursor.executemany("INSERT INTO departments VALUES (?, ?, ?, ?)", departments_data)
    
    # Job titles by department and level
    job_templates = {
        1: {  # Engineering
            'Junior': ['Junior Software Engineer', 'Software Engineer I'],
            'Mid': ['Software Engineer II', 'Backend Engineer', 'Frontend Engineer'],
            'Senior': ['Senior Software Engineer', 'Staff Engineer', 'Principal Engineer'],
            'Lead': ['Engineering Manager', 'Tech Lead']
        },
        2: {  # Product Management
            'Junior': ['Associate Product Manager'],
            'Mid': ['Product Manager'],
            'Senior': ['Senior Product Manager', 'Principal Product Manager'],
            'Lead': ['Director of Product', 'VP of Product']
        },
        3: {  # Sales
            'Junior': ['Sales Development Representative'],
            'Mid': ['Account Executive', 'Sales Manager'],
            'Senior': ['Senior Account Executive', 'Enterprise Sales'],
            'Lead': ['Sales Director', 'VP of Sales']
        },
        4: {  # Marketing
            'Junior': ['Marketing Coordinator'],
            'Mid': ['Marketing Manager', 'Content Marketing Manager'],
            'Senior': ['Senior Marketing Manager', 'Growth Marketing Lead'],
            'Lead': ['Director of Marketing', 'CMO']
        },
        5: {  # Data Science
            'Junior': ['Junior Data Analyst'],
            'Mid': ['Data Scientist', 'ML Engineer'],
            'Senior': ['Senior Data Scientist', 'Staff ML Engineer'],
            'Lead': ['Lead Data Scientist', 'Director of Data Science']
        }
    }
    
    # Salary ranges by level
    salary_ranges = {
        'Junior': (60000, 90000),
        'Mid': (90000, 140000),
        'Senior': (140000, 200000),
        'Lead': (180000, 300000)
    }
    
    # Insert positions
    positions_data = []
    position_id = 1
    statuses = ['Open', 'Open', 'Open', 'In Progress', 'Filled', 'On Hold']
    
    for days_ago in range(180, 0, -15):  # Create positions over 180 days
        for dept_id in range(1, 6):  # First 5 departments
            if random.random() < 0.7:  # 70% chance of posting
                level = random.choice(['Junior', 'Mid', 'Senior', 'Lead'])
                job_title = random.choice(job_templates[dept_id][level])
                salary_min, salary_max = salary_ranges[level]
                salary_min += random.randint(-10000, 10000)
                salary_max += random.randint(-10000, 10000)
                status = random.choice(statuses)
                posted_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
                
                positions_data.append((
                    position_id, dept_id, job_title, level,
                    salary_min, salary_max, status, posted_date
                ))
                position_id += 1
    
    cursor.executemany("INSERT INTO positions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", positions_data)
    
    # Generate candidate names
    first_names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Avery', 'Quinn',
                   'Sam', 'Jamie', 'Drew', 'Blake', 'Cameron', 'Dakota', 'Skylar', 'Logan',
                   'Parker', 'Reese', 'Hayden', 'Kendall', 'Peyton', 'Ryan', 'Sage', 'River']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                  'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
                  'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White']
    
    companies = ['Google', 'Microsoft', 'Amazon', 'Apple', 'Meta', 'Netflix', 'Uber', 'Airbnb',
                 'Stripe', 'Salesforce', 'Oracle', 'IBM', 'Adobe', 'LinkedIn', 'Twitter', 'Zoom',
                 'Dropbox', 'Slack', 'Asana', 'Atlassian', 'GitHub', 'GitLab', 'Square', 'PayPal']
    
    sources = ['LinkedIn', 'Indeed', 'Referral', 'Company Website', 'Recruiter', 'Glassdoor', 'AngelList']
    
    # Insert candidates
    candidates_data = []
    for candidate_id in range(1, 201):  # 200 candidates
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{full_name.lower().replace(' ', '.')}@example.com"
        phone = f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        years_exp = random.randint(0, 15)
        current_company = random.choice(companies) if random.random() < 0.8 else None
        source = random.choice(sources)
        
        candidates_data.append((
            candidate_id, full_name, email, phone,
            years_exp, current_company, source
        ))
    
    cursor.executemany("INSERT INTO candidates VALUES (?, ?, ?, ?, ?, ?, ?)", candidates_data)
    
    # Insert applications
    applications_data = []
    application_id = 1
    app_statuses = ['Applied', 'Phone Screen', 'Interview', 'Offer', 'Hired', 'Rejected', 'Withdrawn']
    
    # Each position gets 3-10 applications
    for position in positions_data:
        pos_id = position[0]
        num_applications = random.randint(3, 10)
        pos_posted_date = datetime.strptime(position[7], '%Y-%m-%d')
        
        for _ in range(num_applications):
            candidate_id = random.randint(1, 200)
            days_after_posting = random.randint(0, 60)
            app_date = (pos_posted_date + timedelta(days=days_after_posting)).strftime('%Y-%m-%d')
            status = random.choice(app_statuses)
            resume_score = random.randint(60, 100)
            
            applications_data.append((
                application_id, candidate_id, pos_id,
                app_date, status, resume_score
            ))
            application_id += 1
    
    cursor.executemany("INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?)", applications_data)
    
    # Insert interviews
    interviews_data = []
    interview_id = 1
    interview_types = ['Phone Screen', 'Technical', 'Behavioral', 'System Design', 'Cultural Fit', 'Final Round']
    interviewers = ['Sarah Chen', 'Michael Brown', 'Jennifer Davis', 'David Wilson', 'Emily Rodriguez',
                    'James Anderson', 'Lisa Taylor', 'Robert Martinez', 'Tom Hughes', 'Maria Lopez']
    
    # Only applications beyond 'Applied' status get interviews
    for app in applications_data:
        app_id = app[0]
        app_status = app[4]
        app_date = datetime.strptime(app[3], '%Y-%m-%d')
        
        if app_status in ['Phone Screen', 'Interview', 'Offer', 'Hired']:
            num_interviews = random.randint(1, 4)
            
            for i in range(num_interviews):
                days_after_app = random.randint(3, 30)
                interview_date = (app_date + timedelta(days=days_after_app)).strftime('%Y-%m-%d %H:%M:%S')
                interview_type = interview_types[min(i, len(interview_types)-1)]
                interviewer = random.choice(interviewers)
                rating = random.randint(1, 5)
                feedback = random.choice([
                    'Strong technical skills',
                    'Good cultural fit',
                    'Needs improvement in communication',
                    'Excellent problem solver',
                    'Limited experience but high potential',
                    'Outstanding candidate'
                ])
                
                interviews_data.append((
                    interview_id, app_id, interview_date,
                    interview_type, interviewer, rating, feedback
                ))
                interview_id += 1
    
    cursor.executemany("INSERT INTO interviews VALUES (?, ?, ?, ?, ?, ?, ?)", interviews_data)
    
    # Insert offers
    offers_data = []
    offer_id = 1
    offer_statuses = ['Pending', 'Accepted', 'Declined', 'Negotiating']
    
    # Only 'Offer' and 'Hired' applications get offers
    for app in applications_data:
        if app[4] in ['Offer', 'Hired']:
            app_id = app[0]
            app_date = datetime.strptime(app[3], '%Y-%m-%d')
            offer_date = (app_date + timedelta(days=random.randint(20, 45))).strftime('%Y-%m-%d')
            
            # Find the position to get salary range
            pos_id = app[2]
            position = next(p for p in positions_data if p[0] == pos_id)
            salary_min, salary_max = position[4], position[5]
            salary_offered = random.randint(salary_min, salary_max)
            signing_bonus = random.randint(5000, 20000) if random.random() < 0.5 else 0
            
            status = 'Accepted' if app[4] == 'Hired' else random.choice(offer_statuses)
            response_date = None
            if status in ['Accepted', 'Declined']:
                response_date = (datetime.strptime(offer_date, '%Y-%m-%d') + timedelta(days=random.randint(1, 10))).strftime('%Y-%m-%d')
            
            offers_data.append((
                offer_id, app_id, offer_date, salary_offered,
                signing_bonus, status, response_date
            ))
            offer_id += 1
    
    cursor.executemany("INSERT INTO offers VALUES (?, ?, ?, ?, ?, ?, ?)", offers_data)
    
    # Commit all changes
    conn.commit()
    
    # Print summary statistics
    cursor.execute("SELECT COUNT(*) FROM departments")
    dept_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM positions")
    pos_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM candidates")
    cand_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM applications")
    app_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM interviews")
    int_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM offers")
    off_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(salary_offered) FROM offers")
    avg_salary = cursor.fetchone()[0]
    
    print(f"\n✅ Database creation complete!")
    print(f"📊 Summary Statistics:")
    print(f"   • {dept_count} departments")
    print(f"   • {pos_count} open/filled positions")
    print(f"   • {cand_count} candidates in pipeline")
    print(f"   • {app_count} job applications")
    print(f"   • {int_count} interviews conducted")
    print(f"   • {off_count} offers made")
    print(f"   • Average salary offered: ${avg_salary:,.0f}")
    print(f"   • Database file: hr_recruitment.db ({os.path.getsize('hr_recruitment.db'):,} bytes)")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    create_hr_recruitment_database()
