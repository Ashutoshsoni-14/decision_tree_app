# 🌳 Decision Tree Classifier Using Scikit-learn

This project demonstrates the implementation, visualization, and evaluation of a **Decision Tree Classifier** using the **Scikit-learn** library. The model is trained on a structured dataset (Iris dataset) to classify target outcomes based on input features.

---

## 📘 Project Overview

- 📊 Dataset: Iris flower dataset (150 samples, 3 classes)
- 🧠 Model: Decision Tree Classifier (using entropy for splitting)
- 📈 Evaluation: Accuracy, Confusion Matrix, Classification Report
- 🎨 Visualization: Tree plotted using `plot_tree` from Scikit-learn

---

## 🧪 Technologies Used

- Python 3.x
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- scikit-learn

---

## 📊 Dataset Description

The Iris dataset consists of 150 flower samples from 3 species:
- **Features**: Sepal length, Sepal width, Petal length, Petal width
- **Target**: Iris setosa, Iris versicolor, Iris virginica

It is a balanced and clean dataset commonly used for classification benchmarks.

---

## 🛠️ Methodology

1. Data loading and exploration
2. Train-test split (70/30)
3. Decision Tree model training with `criterion='entropy'`
4. Visualization of the tree
5. Performance evaluation using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report

---

## 📈 Results

- ✔️ High accuracy (typically above 90%)
- ✔️ Clear decision paths in the tree
- ✔️ Strong performance for linearly separable classes

*Sample Visualization:*
![Decision Tree](tree_visualization.png)

---

## 🚀 How to Run

1. Clone the repository or download the `.ipynb` file
2. Install dependencies (if needed):
   ```bash
   pip install pandas numpy matplotlib scikit-learn
