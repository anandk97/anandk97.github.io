const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const path = require('path');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'projects/operators/index.html'), 'utf8');
const script = html.split('<script>')[1].split('</script>')[0];
const data = JSON.parse(fs.readFileSync(path.join(root, 'projects/operators/operators-data.json'), 'utf8'));
const elements = {};
let stopped = false;
const context = {
  document: {getElementById(id) {
    if (id === 'eval-tabs') { stopped = true; throw new Error('stop after leaderboard'); }
    return elements[id] ||= {innerHTML: ''};
  }},
  matchMedia: () => ({matches: false}),
  fetch: () => Promise.resolve({json: () => Promise.resolve(data)}),
  console,
};
process.on('unhandledRejection', error => {
  if (error.message !== 'stop after leaderboard') throw error;
});
vm.runInNewContext(script, context);
setTimeout(() => {
  assert(stopped, 'leaderboard generation should complete');
  const cards = elements.families.innerHTML;
  const board = elements['board-table'].innerHTML;
  assert.equal((cards.match(/<details class="architecture-info">/g) || []).length, 10);
  assert.equal((board.match(/<details class="architecture-info">/g) || []).length, data.models.length);
  for (const content of [cards, board]) {
    assert.match(content, /<a[^>]+href="https:\/\/github\.com\/anandk97\/neural-operator-comparison\/blob\/main\//);
    assert.match(content, /<summary aria-label="Architecture details for FNO">Architecture<\/summary>/);
    assert.match(content, /Global convolution on a truncated set of Fourier modes/);
  }
  assert.match(elements['task-cards'].innerHTML, /source ↗/);
  assert.match(board, /<td/);
  console.log('Operator runtime: 10 card and ' + data.models.length + ' header disclosures; source links and result cells generated.');
}, 20);
