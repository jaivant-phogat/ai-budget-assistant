from flask import Flask, render_template, request, jsonify
import pandas as pd
from google import genai
import json

app = Flask(__name__)

client = genai.Client(api_key="Insert your API key here.")

def analyze_transactions(df):
    transactions_text = df.to_string(index=False)
    
    prompt = f"""
    You are a personal finance expert. Analyze these bank transactions and return a JSON response with exactly this structure:
    {{
        "summary": "2-3 sentence overview of spending patterns",
        "total_spent": <number>,
        "top_category": "<category name>",
        "insight": "One specific interesting insight about their spending",
        "categories": {{
            "Food & Dining": <amount>,
            "Transportation": <amount>,
            "Shopping": <amount>,
            "Entertainment": <amount>,
            "Bills & Utilities": <amount>,
            "Health": <amount>,
            "Other": <amount>
        }},
        "transactions": [
            {{"description": "<name>", "amount": <number>, "category": "<category>"}}
        ]
    }}
    
    Transactions:
    {transactions_text}
    
    Return ONLY the JSON, no other text.
    """
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    
    text = "".join(part.text for part in response.candidates[0].content.parts if hasattr(part, 'text'))
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    df = pd.read_csv(file)
    
    result = analyze_transactions(df)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)