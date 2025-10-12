<div align="center">

<!-- Animated Wave Header with Lavender–Pink–Mint Ombre -->

<picture>
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20&height=280&section=header&text=Earthquake%20Project&fontSize=72&animation=fadeIn&fontAlignY=36&desc=Patterns%20in%20Seismic%20Data%20%E2%80%94%20Mapped%2C%20Measured%2C%20Made%20Beautiful&descAlignY=66&descSize=22&fontColor=FFF8FD" alt="Header"/>
</picture>

<br>

<!-- Animated Typing Subtitle -->

<picture>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=900&color=D8B5D8&center=true&vCenter=true&multiline=true&width=900&height=90&lines=I%20turn%20earthquake%20streams%20into%20clear%2C%20decision-ready%20insights;Human-first%20explanations%20with%20maps%2C%20clustering%2C%20and%20b-value%20analysis" alt="Typing SVG" />
</picture>

<!-- Soft Pastel Badge Row -->

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFE0F5?style=for-the-badge&labelColor=E6E0FF&logo=python&logoColor=6B5B95" alt="Python"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Geospatial-GeoPandas%20%7C%20Shapely-D4FFE4?style=for-the-badge&labelColor=E6E0FF" alt="Geo"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Viz-Plotly%20%26%20Folium-FFE5CC?style=for-the-badge&labelColor=FFE0F5" alt="Viz"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Models-Statsmodels%20%7C%20scikit--learn-E6E0FF?style=for-the-badge&labelColor=FFE5CC" alt="Models"/>
</p>

<!-- Pastel Gradient Divider -->

<picture>
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,4,6,8,10,12,14,16,18,20&height=4" alt="Divider" width="100%"/>
</picture>

</div>

## Why I built this 

I’m obsessed with turning messy, high-volume data into patterns people can actually use. Earthquake catalogs are perfect for this: time, location, magnitude, depth — enough structure to be rigorous, enough chaos to be interesting. My goal here is simple: **make seismic activity readable**. That means honest statistics, interactive maps, and plain-language summaries that non-seismologists can trust.

## What’s inside

* **Clean ingestion & schema checks** for earthquake catalogs (date windows, mag thresholds, UTC normalization).
* **Exploratory analysis** of frequency, magnitude, depth, and geography.
* **Gutenberg–Richter** fits and **b-value** stability checks (tail behavior matters).
* **Sequence detection** with density-based clustering (DBSCAN/HDBSCAN) over space–time.
* **Interactive maps** (Folium) + **filterable timelines** (Plotly) for quick, human-friendly exploration.
* **Lightweight count baselines** (Poisson / AR models) to frame “what’s normal right now?” — not early warning, just context.

## Project structure I’m using

```
Earthquake_project/
├─ data/
│  ├─ raw/               # original API downloads (GeoJSON/CSV)
│  ├─ interim/           # cleaned intermediates
│  └─ processed/         # analysis-ready parquet/csv
├─ notebooks/
│  ├─ 01_ingest_and_clean.ipynb
│  ├─ 02_eda_spatiotemporal.ipynb
│  ├─ 03_gutenberg_richter_b_value.ipynb
│  ├─ 04_clustering_sequences.ipynb
│  └─ 05_maps_and_report.ipynb
├─ src/
│  ├─ io.py              # downloading, caching, schema validation
│  ├─ prep.py            # cleaning + feature engineering
│  ├─ eda.py             # summaries + visual helpers
│  ├─ models.py          # b-value fits, count baselines
│  └─ viz.py             # folium/plotly builders
├─ reports/
│  ├─ figures/           # exported images/maps
│  └─ summary.md         # narrative findings for humans
└─ README.md
```

> If your local structure differs, keep the headings and update paths — the README is intentionally adaptable.

## Quickstart

```bash
# clone and enter the folder containing Earthquake_project/
pip install -r requirements.txt
# or: conda env create -f environment.yml && conda activate quakes

# run notebooks in order (recommended)
jupyter lab  # open notebooks/01_ingest_and_clean.ipynb
```

**Core dependencies**: `pandas`, `numpy`, `geopandas`, `shapely`, `pyproj`, `scikit-learn`, `statsmodels`, `plotly`, `folium`, `matplotlib`, `requests`, `tqdm`.

### Configure your data window

In `notebooks/01_ingest_and_clean.ipynb`, set:

* `START_DATE`, `END_DATE` (UTC ISO)
* `MIN_MAG` (e.g., 2.5 or 4.5 if you want fewer, larger events)
* Optional: region bounding boxes for focused analysis

All pulls cache to `data/raw/` and standardize to `data/processed/earthquakes.parquet`.

## Methods

* **Cleaning & validation**: deduplicate events, enforce UTC times, coerce types, drop invalid coords, handle missing depths.
* **Spatiotemporal EDA**: rolling counts, inter-event times, kernel density heatmaps, depth profiles by region.
* **Frequency–Magnitude**: maximum-likelihood b-value, goodness-of-fit, sensitivity by magnitude of completeness.
* **Clustering**: DBSCAN/HDBSCAN on (lat, lon, time) with tunable spatial eps and temporal windows to surface swarms/aftershock sequences.
* **Baselines**: Poisson or AR count models to contextualize recent activity vs. expected variability.

## What you can do quickly

* **Open 02\_eda\_spatiotemporal.ipynb** for ready-made plots: distributions, timelines, and geo heatmaps.
* **Open 04\_clustering\_sequences.ipynb** to highlight sequences and inspect cluster metrics.
* **Open 05\_maps\_and\_report.ipynb** to export an interactive Folium map and a short human-readable summary.

## Screens I love 

* **Interactive Folium map** with popups (time, mag, depth) and subtle pastel markers.
* **Plotly timelines** you can filter (region, magnitude bins) — clean, readable, and shareable.
* **One-page report** (Markdown/HTML) distilling b-value shifts, cluster counts, and tail behavior into language anyone can understand.

<div align="center">

<!-- Soft header for visuals -->

<picture>
  <img src="https://capsule-render.vercel.app/api?type=transparent&fontColor=D8B5D8&text=Visual%20Style&height=80&fontSize=36&animation=blinking" alt="Visual Style" />
</picture>

<!-- Gentle gradient card -->

<table width="92%" style="margin:auto;border-collapse:separate;border-spacing:0 18px;">
<tr>
<td style="background: linear-gradient(135deg,#FFE0F5 0%,#E6E0FF 33%,#FFE5CC 66%,#D4FFE4 100%);padding:22px;border-radius:22px;box-shadow:0 16px 32px rgba(214, 202, 255, 0.25);text-align:center;">
  <i style="color:#A98FB0;">Design notes:</i>
  <br/>
  <span style="color:#6F6577;">
    Pastel ombré palette, high contrast labels, readable fonts, and motion used sparingly to guide attention (no distracting progress bars).
  </span>
</td>
</tr>
</table>

</div>

## Ethical scope (what this is *not*)

This is **not** an early-warning system and **not** a real-time operational tool. It’s an exploration and communication project: understand patterns, summarize them honestly, and make the findings accessible.

## Reproducibility & versioning

* Deterministic seeds for clustering and bootstraps where used.
* Data query manifests saved with parameters (dates, mags) next to outputs.
* Environments pinned with `environment.yml` or locked `requirements.txt`.

## Roadmap

* Region presets + plate boundary overlays
* Sliding-window b-value diagnostics
* HDBSCAN parameter sweeps with small-multiple visual comparisons
* One-click HTML “brief” export for stakeholders

## Attribution & license

* **Code**: MIT
* **Data**: respect the terms of the source catalog(s). Always cite query windows and parameters in reports.

---

### Maintainer

**Cazzy (Cazandra) Aporbo**
I make complex data readable — and a little bit beautiful — so real people can use it.

<div align="center">

<!-- Footer Gradient Line -->

<picture>
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=20,18,16,14,12,10,8,6,4,2,0&height=3" alt="Divider" width="100%"/>
</picture>

</div>

 palette.

