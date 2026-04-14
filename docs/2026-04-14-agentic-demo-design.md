# Agentic Data Platform Demo — Design Spec

## Purpose
Demo website for presenting to clients/partners. Shows how Agentic AI transforms
traditional data team workflows. Sequential storytelling: manual flow → AI flow → comparison.

## Scenario
Manager requests: "Tôi cần dashboard theo dõi doanh thu theo vùng, theo tháng"

## Team Roles
- Data Platform Lead — orchestrator, receives & analyzes requests
- Data Profiling Specialist — profiles source data
- Data Ingestion Engineer — builds ingestion pipelines
- Data Transformation Engineer — transforms data (Data Vault 2.0 + marts)
- Data Visualization Analyst — creates dashboards
- Data Governance Specialist — cataloging, lineage, governance

## Aesthetic
- Dark futuristic theme: #0a0a1a background
- Manual flow: warm orange (#ff6b35)
- AI flow: electric cyan (#00d4ff)
- Glassmorphism cards, glow effects, connection lines
- Fonts: Outfit (display) + DM Sans (body) — Google Fonts

## Interaction
- Click to navigate between sections (arrows/dots/keyboard)
- Auto-play animations within each section
- Progress bar at top

## Sections (13 slides)

1. **Hero** — Title + particle background
2. **The Request** — Manager sends message bubble
3. **Manual: Analysis** — Leader analyzes, creates task list + 🎬 VIDEO PLACEHOLDER
4. **Manual: Assignment** — Sequential task assignment to team
5. **Manual: Execution** — Sequential work, waiting, bottlenecks + 🎬 VIDEO PLACEHOLDER
6. **Manual: Pain Points** — Summary: ~2-3 weeks, infographic
7. **Transition** — "What if AI could orchestrate this?"
8. **AI: Instant Analysis** — AI Leader auto-analysis + 🎬 VIDEO PLACEHOLDER
9. **AI: Parallel Dispatch** — All agents activated at once + 🎬 VIDEO PLACEHOLDER
10. **AI: Execution** — Parallel work streams + 🎬 VIDEO PLACEHOLDER
11. **AI: Results** — Completed in hours, quality checks
12. **Comparison** — Side-by-side metrics animation
13. **Conclusion** — Key takeaways

## Tech Stack
- Single HTML file, vanilla CSS, vanilla JS
- Zero dependencies (except Google Fonts CDN)
- Portable: open file = works, share via USB/email
