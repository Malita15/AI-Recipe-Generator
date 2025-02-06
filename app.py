import requests  
from flask import Flask, request, jsonify  

app = Flask(__name__)  

# 🔥 Replace this with your real Spoonacular API Key
API_KEY = '2149626efdd845e4b44e2443c37e32de'  

@app.route('/')
def home():
    return "AI Recipe Generator is Live!"

@app.route('/get_recipe', methods=['GET'])
def get_recipe():
    ingredients = request.args.get('ingredients')  # Get ingredients from user input  
    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400  

    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=3&apiKey={API_KEY}"
    response = requests.get(url)  
    data = response.json()  

    if response.status_code != 200:
        return jsonify({"error": "API request failed"}), 500  

    return jsonify(data)  

if __name__ == '__main__':
    app.run(debug=True)
