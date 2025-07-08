# Customer Orders ETL Pipeline 🛒

This is a beginner-friendly data engineering project that demonstrates a basic ETL (Extract, Transform, Load) pipeline using Python and SQLite.

## 🔧 Tools Used
- Python 3
- Pandas
- SQLite

## 🚀 Project Flow
1. **Extract** data from a CSV file
2. **Transform** it by cleaning and formatting
3. **Load** it into an SQLite database

## 🗂️ Folder Structure
- `data/raw/` – Original CSV file
- `data/processed/` – Cleaned CSV output
- `scripts/` – ETL logic
- `database/` – SQLite DB file

## 📦 How to Run
```bash
pip install -r requirements.txt
python main.py
```

## 📚 Output
- `cleaned_orders.csv` in `data/processed/`
- SQLite database file: `orders.db`

## 💡 Future Improvements
- Replace SQLite with PostgreSQL
- Schedule ETL with Apache Airflow
- Push data to AWS S3
