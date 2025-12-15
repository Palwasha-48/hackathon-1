#!/usr/bin/env python3
"""
Test script to verify authentication functionality
"""
import subprocess
import sys

def run_tests():
    """Run the authentication tests"""
    print("Running authentication tests...")
    result = subprocess.run([
        sys.executable, "-m", "pytest", "test_auth.py", "-v"
    ], cwd="chat-bot/backend")

    if result.returncode == 0:
        print("✓ All authentication tests passed!")
    else:
        print("✗ Some authentication tests failed!")

    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)