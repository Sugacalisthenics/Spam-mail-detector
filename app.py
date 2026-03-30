import streamlit as st
import pickle
import os

# 1. Page setting aur Parrot icon 🦜
st.set_page_config(page_title="Spam Detector AI", page_icon="🦜")

# 2. Files ka sahi rasta (Path) nikalne ke liye
base_path = os.path.dirname(__file__)
vec_path = os.path.join(base_path, 'spam_vc.pkl')
model_path = os.path.join(base_path, 'spam_model.pkl')

# 3. Title aur Heading
st.title("SMS & Email Spam Detector 🦜")
st.markdown("AI model English messages padh kar bata sakta hai ki wo **Spam** hain ya **Asli**!")

# 4. Model loading logic
try:
    with open(vec_path, 'rb') as f1:
        cv = pickle.load(f1)
    with open(model_path, 'rb') as f2:
        model = pickle.load(f2)
except FileNotFoundError:
    st.error("🚨 Error: 'spam_vc.pkl' ya 'spam_model.pkl' nahi mil rahi! Check karo ki files GitHub ke main folder mein hain.")
    st.stop()
except Exception as e:
    st.error(f"🚨 Kuch gadbad ho gayi: {e}")
    st.stop()

# 5. Input Box
input_sms = st.text_area("📝 Apna message yahan type ya paste karo 🦜:", height=150)

# 6. Button dabane par prediction
if st.button("Check Spam 🔍"):
    if input_sms.strip() == "":
        st.warning("Arre! Pehle koi message toh type karoooo!")
    else:
        # Text ko machine ki language me badalna
        transformed_sms = cv.transform([input_sms])
        
        # AI se guess karwana
        result = model.predict(transformed_sms)[0]
        
        # Result dikhana
        if result == 'spam':
            st.error("🚨 SAAVDHAN! Yeh ek scam ya SPAM message hai!")
        else:
            st.success("✅ CHILL! Yeh ek safe message hai 🦜.")

# Footer
st.markdown("---")
st.caption("Made by Suga 🦜")
