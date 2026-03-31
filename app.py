import streamlit as st
import pickle
import os

# 1. Page Configuration
st.set_page_config(page_title="Spam Detector AI", page_icon="🦜")

# 2. Path Handling
base_path = os.path.dirname(__file__)
vec_path = os.path.join(base_path, 'spam_vc.pkl')
model_path = os.path.join(base_path, 'spam_model.pkl')

# 3. Header Section
st.title("SMS & Email Spam Detector 🦜")
st.markdown("### **AI-integrated text analysis for real-time identification of Spam vs. Genuine messages.**")

# 4. Model Loading Logic
try:
    with open(vec_path, 'rb') as f1:
        cv = pickle.load(f1)
    with open(model_path, 'rb') as f2:
        model = pickle.load(f2)
except Exception as e:
    st.error(f"Critical Error: Failed to load model architecture. Details: {e}")
    st.stop()

# 5. User Input Interface
input_sms = st.text_area("Enter the message content for analysis below:", height=150, placeholder="Paste your text here...")

# 6. Prediction Logic
if st.button("Analyze Message 🔍"):
    if not input_sms.strip():
        st.warning("Action Required: Please enter a valid message to proceed with the analysis.")
    else:
        # Transforming input
        transformed_sms = cv.transform([input_sms])
        
        # Model Prediction
        result = model.predict(transformed_sms)[0]
        
        # Output Display
        st.markdown("---")
        if result == 'spam' or result == 1:
            st.error("### 🚨 **Analysis Result: Warning!**")
            st.markdown("This message has been flagged as **Spam/Fraudulent**. Please exercise caution.")
        else:
            st.success("### ✅ **Analysis Result: Verified**")
            st.markdown("This message appears to be **Genuine**. No significant risk detected.")

# Footer Section
st.markdown("---")
st.caption("© 2026 Developed by Suga | Powered by AI-Integrated Text Analysis")
