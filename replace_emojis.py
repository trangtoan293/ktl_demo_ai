import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Include Script and CSS
if 'unpkg.com/lucide@latest' not in html:
    html = html.replace('</title>', '</title>\n    <script src="https://unpkg.com/lucide@latest"></script>')
    css_add = """
        /* Lucide SVG Icons sizing */
        .avatar-img .lucide { width: 55%; height: 55%; }
        .timeline-badge .lucide { width: 1.4rem; height: 1.4rem; margin-right: 0.4rem; }
        .card-top-icon { display: block; margin: 0 auto; stroke-width: 1.5px; }
"""
    html = html.replace('.btn:hover {', css_add + '\n        .btn:hover {')

# 2. Timeline badges
html = html.replace('📅 ', '<i data-lucide="calendar"></i> ')
html = html.replace('⏱️ ', '<i data-lucide="clock"></i> ')

# 3. Mappings for avatar icons (stripping out direct font-size inside the tag where possible, or just substituting the char)
html = html.replace('👨‍💼', '<i data-lucide="briefcase"></i>')
html = html.replace('👨‍💻', '<i data-lucide="user-cog"></i>')
html = html.replace('🔍', '<i data-lucide="search"></i>')
html = html.replace('🚰', '<i data-lucide="database"></i>')
html = html.replace('⚙️', '<i data-lucide="settings"></i>')
html = html.replace('📊', '<i data-lucide="bar-chart-2"></i>')
html = html.replace('📋', '<i data-lucide="shield-check"></i>')
html = html.replace('🤖', '<i data-lucide="bot"></i>')
html = html.replace('🧠', '<i data-lucide="brain" style="width:65%; height:65%; color:var(--ai-color); stroke-width: 1.5px;"></i>')

# 4. Section 6 Stats
html = html.replace('<div style="font-size:3.5rem; margin-bottom:1.5rem;">⏳</div>', '<i data-lucide="hourglass" class="card-top-icon" style="width:3.5rem; height:3.5rem; margin-bottom:1.5rem; color:var(--text-secondary);"></i>')
html = html.replace('<div style="font-size:3.5rem; margin-bottom:1.5rem;">💬</div>', '<i data-lucide="message-square-off" class="card-top-icon" style="width:3.5rem; height:3.5rem; margin-bottom:1.5rem; color:var(--text-secondary);"></i>')
html = html.replace('<div style="font-size:3.5rem; margin-bottom:1.5rem;">❌</div>', '<i data-lucide="alert-triangle" class="card-top-icon" style="width:3.5rem; height:3.5rem; margin-bottom:1.5rem; color:var(--text-secondary);"></i>')

# 5. Section 11 Stats
html = html.replace('<div style="font-size:3.5rem; margin-bottom:1.5rem; color:var(--success)">⚡</div>', '<i data-lucide="zap" class="card-top-icon" style="width:3.5rem; height:3.5rem; margin-bottom:1.5rem; color:var(--success);"></i>')
html = html.replace('<div style="font-size:3.5rem; margin-bottom:1.5rem; color:var(--success)">🤖</div>', '<i data-lucide="bot" class="card-top-icon" style="width:3.5rem; height:3.5rem; margin-bottom:1.5rem; color:var(--success);"></i>')
html = html.replace('<div style="font-size:3.5rem; margin-bottom:1.5rem; color:var(--success)">✅</div>', '<i data-lucide="check-circle" class="card-top-icon" style="width:3.5rem; height:3.5rem; margin-bottom:1.5rem; color:var(--success);"></i>')


# 6. Delete inline font sizes which are no longer needed for SVGs
html = re.sub(r'font-size:[^;"]*;?\s*', '', html)
html = html.replace(' style=""', '')

# 7. Add lucide init
if 'lucide.createIcons();' not in html:
    html = html.replace('initDots();', 'lucide.createIcons();\n            initDots();')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Icons replaced seamlessly!")
