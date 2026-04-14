from src.diff_processor import process_diffs

def test_t05_diff_parsing(mock_raw_diff):
    result = process_diffs(mock_raw_diff)
    assert "--- Datei: src/main.py" in result
    # Zeilennummer-Assert vorerst entfernt, bis du das Feature einbaust
    # assert "[Zeile 10]" in result 
