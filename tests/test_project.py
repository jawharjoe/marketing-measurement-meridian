"""Fast, non-Meridian project checks. Run: python -m unittest discover -s tests."""
import unittest
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


class ProjectDataChecks(unittest.TestCase):
    def test_weekly_data_and_inputs(self):
        df = pd.read_csv(ROOT / 'data' / 'synthetic_weekly_mmm.csv')
        required = {'week','revenue','google_search_spend','google_search_impressions',
                    'meta_spend','meta_impressions','youtube_spend','youtube_impressions',
                    'consumer_demand_index','promotion'}
        self.assertEqual(set(df.columns), required)
        self.assertEqual(len(df), 156)
        self.assertEqual(df.isna().sum().sum(), 0)
        date = pd.to_datetime(df['week'])
        self.assertTrue(date.is_monotonic_increasing)
        self.assertTrue((date.diff().dropna().dt.days == 7).all())
        self.assertTrue((df[['revenue','google_search_spend','meta_spend','youtube_spend']] >= 0).all().all())
        self.assertTrue(set(df.promotion.unique()).issubset({0,1}))

    def test_notebook_code_compiles(self):
        notebook = json.loads((ROOT / 'notebooks' / '01_meridian_mmm_workshop.ipynb').read_text())
        for idx, cell in enumerate(notebook['cells']):
            if cell['cell_type'] == 'code':
                src = ''.join(cell['source'])
                compile(src, f'cell_{idx}', 'exec')
                self.assertEqual(cell.get('outputs'), [])


if __name__ == '__main__':
    unittest.main()
