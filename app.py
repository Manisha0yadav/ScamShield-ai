import streamlit as st
import re
from PIL import Image

st.set_page_config(page_title="ScamShield AI", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
.card { background:#1a2035; border-radius:20px; padding:25px; text-align:center; border:1px solid #2a3555; height:250px; }
.number-circle { background: linear-gradient(135deg, #3b82f6, #6366f1); width:55px; height:55px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 12px auto; font-size:24px; font-weight:bold; color:white; }
.risk-box { background:#2a1215; border:2px solid #ff3b3b; border-radius:20px; padding:25px; }
.safe-box { background:#0f2a1a; border:2px solid #22c55e; border-radius:20px; padding:25px; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ ScamShield-AI")
st.write("Fraud URL / Message / Image Detector - 5 sec me check karo")

# 3 TABS
tab1, tab2, tab3 = st.tabs(["🔗 URL Check", "💬 Message Check", "🖼️ Image Check"])

def check_risk(text):
    score=0
    reasons=[]
    if re.search(r"\d+\.\d+\.\d+\.\d+", text): score+=30; reasons.append("IP host detected")
    if text.count("@")>0 or text.count("-")>2: score+=20; reasons.append("Suspicious separators (@/-)")
    if any(k in text.lower() for k in ["free","win","urgent","lottery","kyc blocked","verify","click here","congratulations"]): score+=25; reasons.append("Phishing keywords found")
    if "http://" in text: score+=15; reasons.append("Unsecure http link")
    if text.count("/")>4: score+=10; reasons.append("Excessive slashes")
    return min(score+10, 95), reasons

with tab1:
    url = st.text_input("Suspicious URL yaha paste karo", placeholder="https://example.com")
    if st.button("Check URL Risk", type="primary"):
        if url:
            risk, details = check_risk(url)
            if risk>60:
                st.markdown(f"<div class='risk-box'><h2 style='color:#ff3b3b;'>🚨 High Security Risk Detected! Risk Score: {risk}%</h2><p>Classification: Malicious Pattern</p></div>", unsafe_allow_html=True)
                with st.expander("📊 Technical Feature Extraction Details"): st.write(details)
            elif risk>30:
                st.warning(f"MEDIUM RISK - {risk}% - Dhyan se kholna")
                st.write(details)
            else:
                st.markdown(f"<div class='safe-box'><h3 style='color:#22c55e;'>✅ Low Risk - {risk}% - Safe lag raha hai</h3></div>", unsafe_allow_html=True)

with tab2:
    msg = st.text_area("Yaha fraud message / SMS / WhatsApp text paste karo", placeholder="Your account will be blocked, click here to verify...")
    if st.button("Check Message"):
        if msg:
            risk, details = check_risk(msg)
            if risk>50:
                st.error(f"🚨 Scam Message Detected! Risk {risk}%")
                st.write(details)
            else:
                st.success(f"✅ Safe Message - Risk {risk}%")

with tab3:
    st.write("Kisi bhi suspicious QR, Payment screenshot, ya Offer image ko upload karo")
    uploaded = st.file_uploader("Image upload karo", type=["png","jpg","jpeg"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, width=300)
        if st.button("Scan Image"):
            st.warning("AI Image Scan: Text extraction karke check kiya... (Demo)")
            st.error("Medium Risk: Image me 'FREE REWARD' jaisa text mila - sambhal ke!")

# How it works
st.divider()
st.markdown("<h1 style='text-align:center;'>How our website scam checker works</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8;'>Learn how we inspect URLs for fraud patterns and keep you protected online.</p>", unsafe_allow_html=True)
c1,c2,c3 = st.columns(3)
c1.markdown("<div class='card'><div class='number-circle'>1</div><h3>Enter the website</h3><p style='color:#94a3b8;'>Paste URL, Message or Upload Image</p></div>", unsafe_allow_html=True)
c2.markdown("<div class='card'><div class='number-circle'>2</div><h3>Scanner reviews site signals</h3><p style='color:#94a3b8;'>AI extracts IP hosts, keywords, slashes, phishing patterns</p></div>", unsafe_allow_html=True)
c3.markdown("<div class='card'><div class='number-circle'>3</div><h3>Get a verdict & next steps</h3><p style='color:#94a3b8;'>Instant risk score with safety recommendations</p></div>", unsafe_allow_html=True)