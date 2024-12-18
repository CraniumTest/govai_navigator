from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'your_openai_api_key'

@app.route('/ask', methods=['POST'])
def ask_question():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({'error': 'Query must be provided'}), 400
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_query,
        max_tokens=150
    )
    
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run()
