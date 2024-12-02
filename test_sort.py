import pytest
from sort import sort

def test_package_sorting():
    # Test case 1: Both bulky and heavy (rejected)
    assert sort(200, 200, 200, 30) == "REJECTED"

    # Test case 2: Bulky but not heavy (special)
    assert sort(200, 200, 50, 10) == "SPECIAL"

    # Test case 3: Heavy but not bulky (special)
    assert sort(50, 50, 50, 25) == "SPECIAL"

    # Test case 4: Neither bulky nor heavy (standard)
    assert sort(50, 50, 50, 10) == "STANDARD"

    # Test case 5: Exactly bulky but not heavy (special)
    assert sort(200, 50, 50, 15) == "SPECIAL"

    # Test case 6: Exactly heavy but not bulky (special)
    assert sort(50, 50, 50, 20) == "SPECIAL"

    # Test case 7: Maximum volume limit (bulky)
    assert sort(200, 200, 10, 5) == "SPECIAL"

    # Test case 8: Very small package (standard)
    assert sort(10, 10, 10, 5) == "STANDARD"

    # Test case 9: Package with one dimension large enough (bulky)
    assert sort(150, 50, 50, 10) == "SPECIAL"

    # Test case 10: Package with mass on the boundary (heavy but not bulky)
    assert sort(50, 50, 50, 20) == "SPECIAL"

    print("All test cases passed successfully.")

if __name__ == "__main__":
    test_package_sorting()
