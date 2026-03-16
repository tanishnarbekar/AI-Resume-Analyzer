// ── DOM Refs ──────────────────────────────────────────────────
const form        = document.getElementById('analyzeForm');
const dropzone    = document.getElementById('dropzone');
const fileInput   = document.getElementById('resumeFile');
const filePreview = document.getElementById('filePreview');
const fileName    = document.getElementById('fileName');
const fileSize    = document.getElementById('fileSize');
const removeFile  = document.getElementById('removeFile');
const analyzeBtn  = document.getElementById('analyzeBtn');
const btnText     = analyzeBtn.querySelector('.btn-text');
const spinner     = document.getElementById('spinner');
const results     = document.getElementById('results');
const reanalyzeBtn= document.getElementById('reanalyzeBtn');

// ── Drag & Drop ───────────────────────────────────────────────
dropzone.addEventListener('dragover',  e => { e.preventDefault(); dropzone.classList.add('drag-over'); });
dropzone.addEventListener('dragleave', ()=> dropzone.classList.remove('drag-over'));
dropzone.addEventListener('drop', e => {
  e.preventDefault(); dropzone.classList.remove('drag-over');
  const file = e.dataTransfer.files[0];
  if (file) setFile(file);
});
dropzone.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', () => { if (fileInput.files[0]) setFile(fileInput.files[0]); });

function setFile(file) {
  fileName.textContent = file.name;
  fileSize.textContent = formatBytes(file.size);
  filePreview.classList.remove('hidden');
  dropzone.classList.add('hidden');

  // Attach to input
  const dt = new DataTransfer();
  dt.items.add(file);
  fileInput.files = dt.files;
}

removeFile.addEventListener('click', () => {
  fileInput.value = '';
  filePreview.classList.add('hidden');
  dropzone.classList.remove('hidden');
});

function formatBytes(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024*1024) return (bytes/1024).toFixed(1) + ' KB';
  return (bytes/(1024*1024)).toFixed(1) + ' MB';
}

// ── Form Submit ───────────────────────────────────────────────
form.addEventListener('submit', async e => {
  e.preventDefault();

  if (!fileInput.files[0]) {
    alert('Please upload a resume first.');
    return;
  }

  setLoading(true);

  const formData = new FormData(form);

  try {
    const res  = await fetch('/analyze', { method: 'POST', body: formData });
    const data = await res.json();

    if (data.error) {
      alert('Error: ' + data.error);
      setLoading(false);
      return;
    }

    renderResults(data);
    results.classList.remove('hidden');
    results.scrollIntoView({ behavior: 'smooth', block: 'start' });
  } catch (err) {
    alert('Something went wrong. Make sure the Flask server is running.');
    console.error(err);
  } finally {
    setLoading(false);
  }
});

function setLoading(on) {
  analyzeBtn.disabled = on;
  btnText.classList.toggle('hidden', on);
  spinner.classList.toggle('hidden', !on);
}

// ── Render Results ────────────────────────────────────────────
function renderResults(d) {

  // Score Ring
  animateScore(d.score);

  // Grade
  const gradeBadge = document.getElementById('gradeBadge');
  gradeBadge.textContent = `${d.grade} — ${d.grade_label}`;
  gradeBadge.style.cssText = gradeStyle(d.grade);

  document.getElementById('scoreHeading').textContent = getScoreHeading(d.score);
  document.getElementById('roleLabel').textContent = `Target Role: ${d.role_title}`;

  // Stats
  document.getElementById('statRequired').textContent = `${d.stats.required_matched}/${d.stats.required_total}`;
  document.getElementById('statBonus').textContent    = `${d.stats.bonus_matched}/${d.stats.bonus_total}`;
  document.getElementById('statSections').textContent = d.sections_found.length;
  document.getElementById('statWords').textContent    = d.word_count;

  // Skills
  renderPills('matchedSkills', d.matched_required, 'pill-green');
  renderPills('missingSkills', d.missing_required, 'pill-red');
  renderPills('bonusSkills',   d.matched_bonus,    'pill-yellow');

  // Keyword Density
  renderDensity(d.keyword_density);

  // Suggestions
  renderSuggestions(d.suggestions);

  // Sections
  renderSections(d.sections_found);
}

function animateScore(score) {
  const ring   = document.getElementById('ringFill');
  const numEl  = document.getElementById('scoreNumber');
  const circum = 314;
  const offset = circum - (score / 100) * circum;

  let current = 0;
  const step  = score / 60;
  const timer = setInterval(() => {
    current = Math.min(current + step, score);
    numEl.textContent = Math.round(current);
    if (current >= score) clearInterval(timer);
  }, 16);

  // Ring color
  const color = score >= 70 ? '#22d3a0' : score >= 50 ? '#ffc94d' : '#ff5e7a';
  ring.style.stroke = color;

  setTimeout(() => { ring.style.strokeDashoffset = offset; }, 50);
}

function gradeStyle(grade) {
  const map = {
    A: 'background:rgba(34,211,160,.15);color:#22d3a0;border:1px solid rgba(34,211,160,.3)',
    B: 'background:rgba(124,106,255,.15);color:#7c6aff;border:1px solid rgba(124,106,255,.3)',
    C: 'background:rgba(255,201,77,.15);color:#ffc94d;border:1px solid rgba(255,201,77,.3)',
    D: 'background:rgba(255,94,122,.15);color:#ff5e7a;border:1px solid rgba(255,94,122,.3)',
    F: 'background:rgba(255,94,122,.15);color:#ff5e7a;border:1px solid rgba(255,94,122,.3)',
  };
  return (map[grade] || '') + ';display:inline-block;padding:.3rem .9rem;border-radius:8px;font-family:var(--font-display);font-size:1rem;font-weight:800;margin-bottom:.75rem';
}

function getScoreHeading(score) {
  if (score >= 85) return '🏆 Outstanding Resume!';
  if (score >= 70) return '👍 Strong Resume';
  if (score >= 55) return '📈 Decent — Room to Grow';
  if (score >= 40) return '⚠️ Needs Significant Work';
  return '🔴 Major Improvements Needed';
}

function renderPills(containerId, items, cls) {
  const el = document.getElementById(containerId);
  if (!items || items.length === 0) {
    el.innerHTML = `<span style="color:var(--muted);font-size:.85rem">None found</span>`;
    return;
  }
  el.innerHTML = items.map(s =>
    `<span class="skill-pill ${cls}">${capitalize(s)}</span>`
  ).join('');
}

function renderDensity(density) {
  const el  = document.getElementById('densityList');
  const entries = Object.entries(density).sort((a,b) => b[1]-a[1]).slice(0, 10);

  if (!entries.length) {
    el.innerHTML = `<span style="color:var(--muted);font-size:.85rem">No keyword data</span>`;
    return;
  }

  const max = entries[0][1];
  el.innerHTML = entries.map(([kw, cnt]) => `
    <div class="density-item">
      <span style="min-width:110px;font-size:.82rem">${capitalize(kw)}</span>
      <div class="density-bar-wrap">
        <div class="density-bar" style="width:${(cnt/max)*100}%"></div>
      </div>
      <span class="density-count">${cnt}×</span>
    </div>
  `).join('');
}

function renderSuggestions(suggestions) {
  const el = document.getElementById('suggestionsList');
  if (!suggestions || !suggestions.length) {
    el.innerHTML = `<p style="color:var(--muted)">No suggestions — great resume!</p>`;
    return;
  }
  el.innerHTML = suggestions.map(s => `
    <div class="suggestion sug-${s.type}">
      <div class="sug-icon">${s.icon}</div>
      <div>
        <div class="sug-title">${s.title}</div>
        <div class="sug-detail">${s.detail}</div>
      </div>
    </div>
  `).join('');
}

function renderSections(sections) {
  const el = document.getElementById('sectionsList');
  if (!sections.length) {
    el.innerHTML = `<span style="color:var(--muted);font-size:.85rem">No standard sections detected</span>`;
    return;
  }
  el.innerHTML = sections.map(s => `<span class="section-tag">✓ ${s}</span>`).join('');
}

// ── Re-analyze ────────────────────────────────────────────────
reanalyzeBtn.addEventListener('click', () => {
  results.classList.add('hidden');
  fileInput.value = '';
  filePreview.classList.add('hidden');
  dropzone.classList.remove('hidden');
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ── Helpers ───────────────────────────────────────────────────
function capitalize(str) {
  return str.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}
