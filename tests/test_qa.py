import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class QARegression(unittest.TestCase):
    def test_matbench_source_and_ddrno_provenance(self):
        page = (ROOT / 'projects/leaderboard/index.html').read_text()
        self.assertIn('https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_expt_gap', page)
        self.assertIn('Table 3', page)
        self.assertIn('checkpoint not independently reproduced', page)

    def test_operator_disclosures_in_generated_cards_and_headers(self):
        page = (ROOT / 'projects/operators/index.html').read_text()
        self.assertIn('function architectureInfo(', page)
        self.assertIn('<details class="architecture-info">', page)
        self.assertIn('<summary', page)
        self.assertIn('${architectureInfo(f.base, f.how)}', page)
        self.assertIn('${architectureInfo(f.var, f.how)}', page)
        self.assertIn('${architectureInfo(name, f.how)}', page)

if __name__ == '__main__': unittest.main()
