# 🔥 Who’s Hot in MLB - Monthly Hitting Dashboard

A live-updating Streamlit dashboard that showcases the **hottest hitters in Major League Baseball** each month, based on real-time performance data. The app highlights top performers in categories like **AVG, HR, OPS, and RBI**, with dynamic filters and clean visualizations.

---

## ⚾️ Features

- 📈 **Top 5 hitters** in AVG, HR, OPS, and RBI
- 🎛 **Dynamic percentile filter** for Plate Appearances (PA)
- 📊 Clean bar charts and sortable leaderboards
- 🔁 Automatically updates daily based on current month
- 🧼 Filters out players with low sample sizes using a smart threshold
- 📦 Built using `pybaseball` for real MLB data

---

## 📸 Link to Streamlit Page

https://mlb-hot-this-month.streamlit.app/

---

## 🧠 How It Works

- Pulls data from [pybaseball](https://github.com/jldbc/pybaseball)'s `batting_stats_range()` for the current month
- Uses the 33rd percentile of PA as the default cutoff (adjustable by slider)
- Displays top players in core hitting categories: AVG, HR, OPS, and RBI
- Built with Streamlit for fast UI and interactivity

---
