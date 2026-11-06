from pathlib import Path
def test_leaderboard_is_discoverable():
    root = Path(__file__).resolve().parents[1]
    assert (root / "projects/leaderboard/index.html").exists()
    assert "/projects/leaderboard/" in (root / "projects/operators/index.html").read_text()
