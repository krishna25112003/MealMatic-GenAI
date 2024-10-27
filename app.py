from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Your OpenAI API key
openai.api_key = "sk-rIAmYADOAzcLZbaOxxn9KyYWFN_E2-bktd7cUN6wRwT3BlbkFJPP0hDoXxFXKZg-O59Xt7anFtvHHaJgf2MPpijZELcA"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        # Get user inputs from the form
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        preference = request.form['preference']
        cuisine = request.form['cuisine']
        
        # Prompt for OpenAI API
        prompt = (
    f"Create a balanced diet meal plan for {name}, aged {age}, with a height of {height} cm and weight of {weight} kg. "
    f"Their dietary preference is {preference}, and they prefer {cuisine} cuisine. The meal plan should focus on healthy, "
    f"nutrient-dense, and low-calorie options aimed at supporting weight management. "
    f"Include five structured meals with the following format: breakfast, morning snack, lunch, afternoon snack, and dinner. "
    f"For each meal, list the dish and provide a detailed nutritional breakdown including calories, carbs, proteins, and fats. "
    f"Ensure that the meals are appropriate for a diet-friendly regimen and visually organized for a professional website. "
    f"Conclude with a total daily nutritional summary in the format 'Total: calories | carbs | proteins | fats' "
    f"to support a healthy weight loss or maintenance goal. "
    f"The output format should be as follows:\n\n"
    f"Meal Time: [Meal Name]\n"
    f"Dish: [Dish Name]\n"
    f"Nutrition: calories | carbs | proteins | fats\n\n"
    f"Total for the Day: calories | carbs | proteins | fats"
)
        
        try:
            # Call the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates detailed diet meal plans with nutritional information."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
            # Get the generated meal plan
            result = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            result = f"An error occurred: {str(e)}"
        
        # Render the result page with the generated meal plan
        return render_template('result.html', result=result)

    # Render the form page if the method is GET
    return render_template('generate.html')

if __name__ == '__main__':
    app.run(debug=True)
