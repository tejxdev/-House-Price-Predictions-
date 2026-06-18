# 🏠 House Price Prediction System

A Machine Learning-based web application that predicts house prices using important housing features. The project is built using Python, Flask, Scikit-Learn, HTML, and CSS.

## 📌 Project Overview

This project predicts house prices based on various housing-related features. Users can enter housing details through a web interface and get an estimated house price instantly.

## 🚀 Features

- User-friendly web interface
- Real-time house price prediction
- Machine Learning model using Linear Regression
- Flask-based backend
- Responsive design
- Fast and accurate predictions

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Web Development
- Flask
- HTML
- CSS

## 📂 Project Structure

```
House_Price_Prediction/
│
├── app.py
├── train_model.py
├── model/
│   └── model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/House_Price_Prediction.git
```

### 2. Go to Project Directory

```bash
cd House_Price_Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or

```bash
pip install flask pandas numpy scikit-learn
```

## ▶️ Run the Project

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## 🧠 Model Training

To train the model again:

```bash
python train_model.py
```

The trained model will be saved in:

```
model/model.pkl
```

## 📊 Input Features

- RM (Average Number of Rooms)
- AGE (Age of Building)
- DIS (Distance to Employment Centers)
- TAX (Property Tax Rate)
- PTRATIO (Pupil-Teacher Ratio)

## 🔄 Working Process

1. User enters house details.
2. Flask receives the input data.
3. Trained Machine Learning model processes the data.
4. Predicted house price is generated.
5. Result is displayed on the webpage.

## 🎯 Future Improvements

- Add more machine learning algorithms
- Improve model accuracy
- Deploy on Render or Railway
- Add data visualization dashboard
- Mobile-friendly UI

## 👨‍💻 Author

**Tej Pratap Singh**

MCA Student | Software Developer Enthusiast

