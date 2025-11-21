"""
Simple test script for validating the RAG agent implementation.
Run this after completing your implementation to check if it works correctly.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_environment():
    """Test if environment is properly set up"""
    print("🔧 Testing Environment Setup...")
    
    # Check OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("❌ OpenAI API key not configured properly")
        print("   Please set OPENAI_API_KEY in your .env file")
        return False
    else:
        print("✅ OpenAI API key configured")
    
    # Check data directory
    if not os.path.exists("./data"):
        print("❌ Data directory not found")
        return False
    
    # Check for banking documents
    data_files = [f for f in os.listdir("./data") if f.endswith('.txt')]
    if len(data_files) < 5:
        print(f"❌ Expected at least 5 banking documents, found {len(data_files)}")
        return False
    else:
        print(f"✅ Found {len(data_files)} banking policy documents")
    
    return True

def test_imports():
    """Test if required packages can be imported"""
    print("\n📦 Testing Package Imports...")
    
    try:
        import openai
        print("✅ OpenAI package imported")
    except ImportError:
        print("❌ Failed to import openai")
        return False
    
    try:
        import chromadb
        print("✅ ChromaDB package imported")
    except ImportError:
        print("❌ Failed to import chromadb")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv package imported")
    except ImportError:
        print("❌ Failed to import python-dotenv")
        return False
    
    return True

def test_basic_functionality():
    """Test basic RAG functionality if implementation exists"""
    print("\n🧪 Testing Basic Functionality...")
    
    try:
        # Try to import from the notebook/implementation
        # This is a basic check - students would run the actual notebook
        print("✅ Ready for implementation testing")
        print("   Run your notebook to test the full RAG system")
        return True
    except Exception as e:
        print(f"❌ Error in basic functionality: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 RAG Agent Starter Code Validation\n")
    
    env_ok = test_environment()
    imports_ok = test_imports()
    basic_ok = test_basic_functionality()
    
    print("\n" + "="*50)
    if env_ok and imports_ok and basic_ok:
        print("🎉 All checks passed! You're ready to implement your RAG agent.")
        print("\nNext steps:")
        print("1. Open banking_rag_agent.ipynb")
        print("2. Complete the 'YOUR CODE HERE' sections")
        print("3. Test with the provided test queries")
        print("4. Analyze your agent's performance")
    else:
        print("❌ Some checks failed. Please fix the issues above before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main()
