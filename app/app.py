import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.detector import detect
import pandas as pd

st.set_page_config(page_title="AI Attack Detection", layout="centered")

st.title("🔐 AI Web Attack Detection System")
st.write("🟢 System Active")

req = st.text_area("Enter HTTP Request")

log_file = "logs/request_logs.csv"

# Ensure log file exists
if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
    pd.DataFrame(columns=["request", "result", "type"]).to_csv(log_file, index=False)

# ✅ ONLY ONE BUTTON
if st.button("Analyze", key="analyze_btn"):

    if req.strip() == "":
        st.warning("Enter request first")
    else:
        result = detect(req)

        st.subheader("Result")
        st.success(result["result"])
        st.write("Attack Type:", result["type"])
        st.write("Confidence:", str(result["confidence"]) + "%")

        # 🔥 SAVE LOG
        df = pd.read_csv(log_file)
        new_row = pd.DataFrame([[req, result["result"], result["type"]]], columns=["request", "result", "type"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(log_file, index=False)

        st.success("✅ Logged successfully")

# 🔥 ALWAYS SHOW LOGS (OUTSIDE BUTTON)
st.subheader("📜 Logs")

logs = pd.read_csv(log_file)
st.dataframe(logs)