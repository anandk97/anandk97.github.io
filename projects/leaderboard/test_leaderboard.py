from pathlib import Path
from html.parser import HTMLParser

PAGE = Path(__file__).with_name('index.html')
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.sections=[]; self.links=[]; self.novelty=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag == 'section': self.sections.append(a.get('id'))
        if tag == 'a': self.links.append(a.get('href'))
        if 'novelty' in a.get('class','').split(): self.novelty.append((tag,a))

def test_six_linked_datasets_and_reference_results():
    text=PAGE.read_text(); p=Parser(); p.feed(text)
    assert set(p.sections)=={'airfrans','matbench','rmd17','matten','trl','mhd'}
    assert all('#'+section in p.links for section in p.sections)
    for score in ('0.2693','0.1306','4.52','3.32','0.0831','0.1956','0.0580'):
        assert score in text

def test_novelty_is_linked_and_accessible():
    p=Parser(); p.feed(PAGE.read_text())
    assert p.novelty
    assert all(tag=='a' and a.get('href','').startswith('https://') and a.get('data-novelty') for tag,a in p.novelty)
