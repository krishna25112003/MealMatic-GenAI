# MealMatic

## Overview
MealMatic is a web-based meal planning application that provides personalized meal plans based on user input. The application allows users to enter their dietary preferences and health details to generate meal recommendations with nutritional information.

## Features
- User-friendly web interface
- Meal plan generation based on dietary preferences
- Nutritional information display
- Interactive UI with images and styles
- Flask-based backend for processing user inputs

## Project Structure
```
MealMatic/
│── static/
│   ├── css/
│   │   ├── home.css
│   │   ├── result.css
│   ├── images/
│   │   ├── 14-days-clean-eating-meal-plan.jpg
│   │   ├── EW-Group-Meal-Plans-Day-06.jpg
│   │   ├── istockphoto-876656394-612x612.jpg
│   │   ├── pexels-photo-1640775.jpg
│── templates/
│   ├── generate.html
│   ├── home.html
│   ├── result.html
│── app.py
│── requirements.txt
```

## Installation
### Prerequisites
- Python 3.x
- Flask

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/MealMatic.git
   cd MealMatic
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`.

## Technologies Used
- **Frontend:** HTML, CSS
- **Backend:** Flask (Python)
- **Database:** Not specified (could be added for future enhancements)

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

