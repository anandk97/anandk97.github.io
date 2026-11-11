import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'projects/surrogates/index.html'
FAMILIES = ('sparse', 'modal', 'classical', 'operators', 'physics', 'hybrid', 'window')

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids = []; self.links = []; self.text = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
    def handle_data(self, data): self.text.append(data)

class SurrogatesTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PAGE.exists(), 'family guide is missing')
        self.doc = Document(PAGE.read_text())
        self.text = ' '.join(self.doc.text)

    def test_family_navigation(self):
        for family in FAMILIES:
            with self.subTest(family=family):
                self.assertIn(family, self.doc.ids)
                self.assertIn('#' + family, self.doc.links)
        self.assertEqual(len(self.doc.ids), len(set(self.doc.ids)))

    def test_links_resolve(self):
        for link in self.doc.links:
            with self.subTest(link=link):
                url = urlsplit(link)
                if url.scheme or url.netloc: continue
                if not url.path: self.assertIn(url.fragment, self.doc.ids); continue
                target = ROOT / unquote(url.path).lstrip('/') if url.path.startswith('/') else PAGE.parent / unquote(url.path)
                if target.is_dir(): target = target / 'index.html'
                elif not target.suffix and not target.exists(): target = target.with_suffix('.md')
                self.assertTrue(target.exists(), str(target))

    def test_spectral_submanifold_not_confused_with_state_space(self):
        self.assertIn('spectral submanifold', self.text.lower())
        self.assertIn('state-space model', self.text.lower())

    def test_scope_and_provenance(self):
        for phrase in ('SINDy', 'DMD', 'POD', 'SSM', 'Transolver', 'LSTM', 'FEM', 'validation', 'public test', 'planned'):
            with self.subTest(phrase=phrase): self.assertIn(phrase.lower(), self.text.lower())
        self.assertIn('/projects/operators/', self.doc.links)
        self.assertIn('/projects/surrogates/', Document((ROOT / 'projects/index.html').read_text()).links)
        self.assertNotIn('coming soon', self.text.lower())

if __name__ == '__main__': unittest.main()
