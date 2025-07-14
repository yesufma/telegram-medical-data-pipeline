# 🚀 Telegram Medical Data Pipeline

Welcome to the **Telegram Medical Data Pipeline**, a data engineering project built for the **10 Academy Week 7 Challenge: "Shipping a Data Product"**. This pipeline extracts medical-related messages from public Telegram channels, transforms them into clean, analytics-ready data using **dbt**, and stores everything in a **PostgreSQL** database.



---

## 🌐 Project Overview

**Goal**: Build a complete ELT data pipeline to support data analysis and public health monitoring using scraped Telegram data.

**Source Channels:**
- CheMed123
- Lobelia for Cosmetics ([@lobelia4cosmetics](https://t.me/lobelia4cosmetics))
- Tikvah Pharma ([@tikvahpharma](https://t.me/tikvahpharma))

---

## ✅ Completed Tasks

### ✅ Task 1: Extract and Load Telegram Data
- Connected to the **Telegram API**
- Scraped **messages and images** from 3 health-related channels
- Stored raw JSON data and images in a local data lake:
- Loaded messages into PostgreSQL table: `raw.telegram_messages`

---

### ✅ Task 2: Transform with dbt
- Initialized dbt project: `ethiomed_dbt`
- Built the following models:
  - `stg_telegram_messages`: staging model for raw messages
  - `dim_channels`: dimension table for channel names
  - `dim_dates`: dimension table for message dates
  - `fct_messages`: fact table joining all relevant data
- Added **tests**: `not_null`, `unique` for key fields
- Generated **documentation** with `dbt docs`
- All models tested and documented successfully.

---


## 📂 Repo Structure
```bash
├── data
│ └── raw/telegram_messages/
├── dbt
│ └── ethiomed_dbt/
│ ├── models/
│ │ ├── staging/
│ │ └── marts/
│ └── dbt_project.yml
├── scripts
│ ├── load_to_postgres.ipynb
│ └── test_postgres.ipynb
```

---

## 🚪 Requirements

- Python 3.9+
- PostgreSQL 13+
- Docker (for PostgreSQL container)
- dbt (v1.10+)

---

## 📅 Timeline

| Date      | Task                    | Status       |
|-----------|-------------------------|--------------|
| July 13   | Task 1 - Extract & Load | ✅ Completed |
| July 14   | Task 2 - Transform      | ✅ Completed |


---

## 👤 Author

**Yusuf**  
10 Academy Fellow - Week 7 Challenge

---

## ✨ Acknowledgements

- Thanks to **10 Academy** for this incredible learning opportunity
- Inspired by real-world public health data problems and solutions

---

## 🌟 Show Some Love

If you found this project helpful or interesting, feel free to **⭐ the repo** or connect with me!

