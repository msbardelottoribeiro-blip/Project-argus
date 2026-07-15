#  Project Argus - Frontend & UI Blueprint

This document guides frontend developers on how to build the public transparency dashboard for Project Argus.

## Proposed Tech Stack
- **Framework:** React.js / Next.js
- **Styling:** Tailwind CSS (Dark Mode preferred for a security/audit feel)
- **Charts & Maps:** Chart.js, D3.js, or React-Simple-Maps for the global tracking module

##  Core Screens & Components

### 1. Global Risk Dashboard (Home)
- **Interactive World Map:** Visualizes UN humanitarian fund distribution and highlights high-risk areas in real-time.
- **Counter Widgets:** Live ticker for Total USD Audited, Contracts Scraped, and High-Risk Alerts Triggered.

### 2. Live Audit Feed
- A clean, searchable feed displaying flagged contracts with a dynamic "Risk Score Badge" (0 to 10 scale).
- Tooltips explaining the mathematical reasons behind the AI flag (e.g., "Short Description Detected", "Supplier Country Anomaly").

### 3. Entity Graph Viewer
- A visual network chart connecting UN Agencies to Suppliers and Ultimate Beneficial Owners (UBOs) using data from our Neo4j graph pipeline.
