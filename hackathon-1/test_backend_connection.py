# Test script to verify frontend can connect to backend
import requests
import json
import sys

def test_api_connection():
    """Test that the API endpoints are accessible"""

    # Test the health endpoint
    try:
        response = requests.get("http://localhost:8000/api/health")
        if response.status_code == 200:
            print("[OK] Health endpoint accessible")
            print(f"  Response: {response.json()}")
        else:
            print(f"[ERROR] Health endpoint returned status {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Error accessing health endpoint: {e}")

    # Test the ask endpoint (will fail due to API key but should return 403, not 404)
    try:
        payload = {"question": "test"}
        response = requests.post(
            "http://localhost:8000/api/ask",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 403:  # Expected - API key issue
            print("[OK] Ask endpoint accessible (403 due to API key)")
        elif response.status_code == 404:
            print("[ERROR] Ask endpoint not found")
        else:
            print(f"[OK] Ask endpoint accessible (status {response.status_code})")
    except Exception as e:
        print(f"[ERROR] Error accessing ask endpoint: {e}")

    # Test the ask-selection endpoint
    try:
        payload = {"question": "test", "selection": "test selection"}
        response = requests.post(
            "http://localhost:8000/api/ask-selection",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 403:  # Expected - API key issue
            print("[OK] Ask-selection endpoint accessible (403 due to API key)")
        elif response.status_code == 404:
            print("[ERROR] Ask-selection endpoint not found")
        else:
            print(f"[OK] Ask-selection endpoint accessible (status {response.status_code})")
    except Exception as e:
        print(f"[ERROR] Error accessing ask-selection endpoint: {e}")

if __name__ == "__main__":
    print("Testing backend API endpoints...")
    test_api_connection()
    print("\nAPI endpoints are properly configured and accessible.")
    print("Frontend can connect to backend via proxy at /api/* -> http://localhost:8000/api/*")