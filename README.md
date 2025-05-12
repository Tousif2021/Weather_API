# 🌐 My Flask API

This is my first-ever custom API built using **Python + Flask**!  
It features:
- 🌤 Real-time **weather updates** (using WeatherAPI)
- 📝 A simple **item manager** with GET/POST routes
- ⚡ Clean, beginner-friendly code

## 🚀 Endpoints

### `GET /`
- Welcome message

### `GET /weather/<city>`
- Example: `/weather/Stockholm`
- Returns temperature, condition, country

### `GET /items`
- Returns a list of items added

### `POST /items`
- Accepts JSON: `{"item": "Milk"}`
- Adds item to the list

## 🛠 Technologies Used
- Flask
- Python Requests
- JSON
- WeatherAPI

## 📦 How to Run
```bash
pip install flask requests
python app.py
