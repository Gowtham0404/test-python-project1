import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import add

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    test_add()
    print("All tests passed.")
