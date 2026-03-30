import streamlit as st
import pickle

# 1. Website ki setting aur Parrot icon 🦜
st.set_page_config(page_title="Spam Detector AI", page_icon="🦜")

# 2. Main Title aur Heading
st.title("SMS & Email Spam Detector 🦜")
st.markdown("AI model English messages padh kar bata sakta hai ki wo **Spam** hain ya **Asli**!")

# 3. Model loading (Dabbe load karna)
try:
    # Terminal ke hisaab se filenames check kar liye hain
    cv = pickle.load(open('spam_vc.pkl', 'rb'))
    model = pickle.load(open('spam_model.pkl', 'rb'))
except FileNotFoundError:
    st.error("🚨 Bhai, dabbe (pkl files) nahi mil rahe! Check kar ki files ka naam 'spam_vc.pkl' aur 'spam_model.pkl' hi hai na?")
    st.stop()

# 4. Input Box (Yahan message likho)
input_sms = st.text_area("📝 Apna message yahan type ya paste karo 🦜:", height=150)

# 5. Button dabane par kya hoga
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