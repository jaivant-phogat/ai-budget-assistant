# AI Budget Assistant

A web app that uses AI to analyze your bank transactions and generate spending insights, charts, and personalized financial summaries.

## What It Does

Upload a CSV export from your bank and the app automatically:
- Categorizes every transaction using Google Gemini AI
- Generates a personalized AI insight about your spending habits
- Breaks down spending into categories like Food & Dining, Shopping, Transportation, and more
- Displays an interactive doughnut chart and bar chart
- Lists every transaction with its AI-assigned category

## Demo

<img width="3420" height="1962" alt="image" src="https://github.com/user-attachments/assets/136a99fc-3ac5-4995-a3b3-eb53681836a0" />

## Example With A Real CSV

<img width="708" height="1426" alt="image" src="https://github.com/user-attachments/assets/5e6cce48-aaea-44bf-9ef9-bb53cc8ae7dd" />


## Tech Stack

- **Python** — Flask backend, Pandas for CSV processing
- **HTML/CSS** — Frontend UI with Chart.js for data visualization
- **Google Gemini AI** — Transaction categorization and insight generation
- **Yahoo Finance (yfinance)** — Financial data support

## How to Run

1. Clone the repository
2. Install dependencies:
pip install flask pandas google-genai
3. Add your Google Gemini API key to `main.py`:
```python
   client = genai.Client(api_key="YOUR_API_KEY_HERE")
```
4. Run the app:
python main.py
5. Open your browser and go to `http://127.0.0.1:5001`
6. Upload a CSV export from your bank and get instant AI-powered insights

## CSV Format

Works with any Canadian bank CSV export including TD, RBC, Scotiabank, and BMO. The file should contain columns for date, description, and amount.

## Built By

Jaivant Phogat
