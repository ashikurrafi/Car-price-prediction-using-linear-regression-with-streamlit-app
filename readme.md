# <center>Car price prediction using Linear Regression with Streamlit app</center>

## Overview

A simple yet powerful web application built with Streamlit and Python, designed to predict car prices using linear regression. With a minimal and intuitive user interface, this app makes predicting car prices easy and accessible to everyone. Whether you're a car enthusiast or looking to make informed buying/selling decisions, this user-friendly tool delivers accurate results with just a few inputs. No technical expertise required — just enter the details, and let the app do the rest!

## Features

- **Minimal** user interface
- **Easy** to use
- **User friendly** web application

## Project Structure

```
📦 Car-price-prediction-using-linear-regression-with-streamlit-app
├── 📂 dataset
├── ├── 📂 car_data.csv
│   📂 models
│   ├── 📂 model.pkl
│   ├── car.py
│   ├── main.ipynb
```

## Download in local

1. Clone the repository:
   ```bash
   https://github.com/ashikurrafi/Car-price-prediction-using-linear-regression-with-streamlit-app.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Car-price-prediction-using-linear-regression-with-streamlit-app
   ```

## Creating environment and install dependencies

1. Clone the repository:

   ```bash
   conda create --name <env-name> python=3.9
   ```

2. Activate the environment:

   ```bash
   conda activate <env-name>
   ```

3. Install uv for faster installation:
   ```bash
   pip install uv
   ```
4. Install requirements files:

   ```bash
   uv pip install -r requirements.txt
   ```

5. Run Streamlit app:

   ```bash
   streamlit run car.py
   ```

   The server should be running at:
   <br/>
   Local URL: `http://localhost:8501`
   <br/>
   Network URL: `http://192.168.1.101:8501`
