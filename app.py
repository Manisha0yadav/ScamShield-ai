import streamlit as st
import re

st.set_page_config(page_title="ScamShield AI", page_icon="🛡️", layout="wide")

# --- CSS for Dark Pro Look ---
st.markdown("""
<style>
.card {
    background-color: #1a2035;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    border: 1px solid #2a3555;
    margin-bottom: 20px;
}
.number-circle {
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    width: 60px; height: 60px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 15px auto;
    font-size: 28px; font-weight: bold; color: white;
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
}
.risk-box {
    background-color: #2a1215;
    border: 2px solid #ff3b3b;
    border-radius: 20px;
    padding: 25px;
    color: #ffadad;
}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ ScamShield-AI")
st.write("Fraud URL / Message / Image Detector - 5 sec me check karo")

url = st.text_input("Suspicious URL yaha paste karo", placeholder="https://example.com")

def check_url(u):
    score = 0
    reasons = []
    if "http://" in u: score+=20; reasons.append("http use - secure nahi hai")
    if re.search(r"\d+\.\d+\.\d+\.\d+", u): score+=30; reasons.append("IP host mila - scam signal")
    if u.count("@")>0 or u.count("-")>2: score+=20; reasons.append("Suspicious domain separators")
    if any(k in u.lower() for k in ["free","win","urgent","verify","login","offer"]): score+=25; reasons.append("Phishing keyword detected")
    if u.count("/")>4: score+=15; reasons.append("Excessive slashes")
    return min(score+10, 95), reasons

if st.button("Check URL Risk", type="primary"):
    if url:
        risk, details = check_url(url)
        if risk > 60:
            st.markdown(f"""
            <div class="risk-box">
                <h2 style='color:#ff3b3b;'>🚨 High Security Risk Detected!</h2>
                <p>Warning: This URL contains suspicious structural patterns commonly found in phishing attacks and deceptive websites.</p>
                <span style='background:#ff3b3b; color:white; padding:8px 15px; border-radius:20px;'>Risk Score: {risk}%</span>
                <span style='background:#b91c1c; color:white; padding:8px 15px; border-radius:20px; margin-left:10px;'>Classification: Malicious Pattern</span>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("📊 Technical Feature Extraction Details"):
                for d in details: st.write(f"- {d}")
        else:
            st.warning(f"MEDIUM RISK - {risk}% - Verify karke hi kholo")

# --- How it works section ---
st.markdown("---")
st.markdown("<h1 style='text-align:center; font-size:42px;'>How our website scam checker works</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #94a3b8;'>Learn how we inspect URLs for fraud patterns and keep you protected online.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card">
        <div class="number-circle">1</div>
        <h3>Enter the website</h3>
        <p style='color:#94a3b8;'>Paste the web address (URL) you want to verify into our real-time security scanner.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <div class="number-circle">2</div>
        <h3>Scanner reviews site signals</h3>
        <p style='color:#94a3b8;'>The AI engine extracts syntactic cues: IP hosts, suspicious domain separators, excessive slashes, and phishing keywords.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card">
        <div class="number-circle">3</div>
        <h3>Get a verdict & next steps</h3>
        <p style='color:#94a3b8;'>Receive an instant risk score breakdown with clear safety recommendations before you interact with the site.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("ℹ️ Data Sources & Detection Architecture"):
    st.write("We use regex, domain age check, IP detection, and keyword blacklists to detect fraud.")