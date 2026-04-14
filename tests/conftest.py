import pytest

@pytest.fixture
def mock_mr_metadata():
    return {
        "title": "Test MR für IPA",
        "description": "Das ist eine Testbeschreibung",
        "author": "Calvin.Pfrender"
    }

@pytest.fixture
def mock_raw_diff():
    return [
        {
            "new_path": "src/main.py",
            "diff": "@@ -10,3 +10,4 @@\n def hello():\n-    print('old')\n+    print('new')",
            "deleted_file": False
        }
    ]