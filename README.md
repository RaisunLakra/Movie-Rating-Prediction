# 🚀 Movie Rating Prediction

## 📌 Introduction

This project focuses on performing data analysis on movie ratings and building a regression model to predict ratings accurately.

## 📁 Dataset - IMDb India Movies

Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies/code). It contains Indian movies with the following columns:

- **Name**: Movie title
- **Year**: Release year
- **Duration**: Length of the movie (minutes)
- **Genre**: Movie genre(s)
- **Rating**: IMDb rating
- **Votes**: Number of votes on IMDb
- **Director**: Director of the movie
- **Actor 1, Actor 2, Actor 3**: Main actors in the movie

## 📂 Repository Structure

```bash
📦 Movie-Rating-Prediction
 ┣ 📜 app.py
 ┣ 📂 datasets
 ┃ ┣ 📜 IMDb_Movies_India.csv
 ┃ ┣ 📜 processed_data.pkl                   # Cleaned dataset
 ┣ 📂 notebooks                              # Jupyter notebooks for analysis & experimentation
 ┃ ┣ 📜 MyNotebook.ipynb                     # Contains data cleaning, feature engineering, and modeling
 ┣ 📂 models                                 # Stores trained models
 ┃ ┣ 📜 random_forest_regressor_model        # Trained model file
 ┣ 📜 README.md                              # Project documentation
 ┣ 📜 requirements.txt                       # Dependencies list
 ┣ 📜 .gitignore
 ┣ 📜 LICENSE                                # MIT License
```

## 🔧 Approach & Methodology

### **1️⃣ Data Cleaning**

- Removed duplicates.
- Filled missing values with "Unknown."
- Converted `Year`, `Duration`, and `Votes` to integer data types.

### **2️⃣ Feature Engineering**

- Applied **One-Hot Encoding** on `Genre`.
- Extracted key features from **Genres, Actors, and Directors**.

### **3️⃣ Model Training**

- Used **Random Forest Regressor** for training.
- Prepared data for modeling and evaluated performance using:
  - **Mean Absolute Error (MAE)**
  - **Root Mean Squared Error (RMSE)**
  - **R² Score**

## 💻 Installation & Usage

```bash
# Create virtual environment
python -m venv env
source env/bin/activate  # On MacOS/Linux
env\Scripts\activate     # On Windows

# Clone the repository
git clone https://github.com/RaisunLakra/Movie-Rating-Prediction
cd Movie-Rating-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 app.py
```

## 📊 Results & Performance

| Metric       | Validation Set | Test Set |
| ------------ | -------------- | -------- |
| **MAE**      | 0.5428         | 0.5148   |
| **RMSE**     | 0.7873         | 0.7558   |
| **R² Score** | 0.6814         | 0.6931   |

## 📜 License

**MIT Licensed** © 2025 [Raisun Lakra](https://github.com/RaisunLakra)

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
