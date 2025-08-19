#!/usr/bin/env python3
"""
TDS Data Analyst Agent - Setup Verification Script
This script helps verify your deployment is working correctly.
"""

import requests
import json
import sys

def test_deployed_app(base_url):
    """Test the deployed Vercel application"""
    print(f"🧪 Testing deployed app at: {base_url}")
    print("=" * 60)

    # Test 1: Check if the main page loads
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            print("✅ Main page loads successfully")
        else:
            print(f"❌ Main page returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Could not reach main page: {e}")

    # Test 2: Check the simple API endpoint
    api_url = f"{base_url}/api/simple"
    test_question = "What is your purpose?"

    try:
        response = requests.post(
            api_url, 
            json={"question": test_question},
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        print(f"\n🔍 Testing API endpoint: {api_url}")
        print(f"Question: {test_question}")
        print(f"Status: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()
                answer = data.get('answer', data.get('result', 'No answer field'))
                print(f"✅ API working! Response: {answer[:100]}...")
            except json.JSONDecodeError:
                print(f"❌ API returned non-JSON response: {response.text[:200]}")
        else:
            print(f"❌ API returned error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"❌ API request failed: {e}")

    print("\n" + "=" * 60)
    print("🎯 Next Steps:")
    print("1. If tests pass: Update promptfooconfig.yaml with your URL")
    print("2. Run: npx promptfoo eval")
    print("3. Check results: npx promptfoo view")
    print("4. Your TDS agent is ready! 🚀")

def main():
    print("🤖 TDS Data Analyst Agent - Setup Verification")
    print("=" * 60)

    if len(sys.argv) != 2:
        print("Usage: python setup_verification.py <your-vercel-url>")
        print("Example: python setup_verification.py https://my-app.vercel.app")
        sys.exit(1)

    base_url = sys.argv[1].rstrip('/')
    test_deployed_app(base_url)

if __name__ == "__main__":
    main()
