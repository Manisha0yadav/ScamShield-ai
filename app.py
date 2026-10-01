import streamlit as st

st.set_page_config(page_title="ScamShield-AI", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
.main { background: #f7f9fc; }
.stButton>button { width:100%; background: #2563eb; color:white; font-weight:700; border-radius:12px; padding:12px; }
.result-high { background:#ffe0e0; padding:20px; border-radius:15px; border-left:6px solid #c92a2a; }
.result-medium { background:#fff3bf; padding:20px; border-radius:15px; border-left:6px solid #e67700; }
.result-low { background:#d3f9d8; padding:20px; border-radius:15px; border-left:6px solid #2b8a3e; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>🛡️ ScamShield-AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray'>Fraud URL / Message / Image Detector - 5 sec me check karo</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔗 URL Check", "💬 Text Check", "🖼️ Image Check"])

def calculate_risk(text):
    text = text.lower()
    score = 15
    reasons = []
    if any(x in text for x in ["urgent","immediately","act now","limited"]):
        score+=30; reasons.append("❌ Urgency trick - jaldi karne ko bol raha hai")
    if any(x in text for x in ["lottery","winner","prize","75% off","free"]):
        score+=35; reasons.append("🎁 Fake Offer / Lottery ka lalach")
    if any(x in text for x in ["shoop","amaz0n","bit.ly","tinyurl"]):
        score+=30; reasons.append("🔗 Typosquatting - nakli domain")
    if "@" in text or len(text)>70:
        score+=10; reasons.append("⚠️ Suspicious characters / bahut lamba URL")
    score = min(max(score,20),95)
    return score, reasons

with tab1:
    url = st.text_input("Suspicious URL yaha paste karo", placeholder="https://shoop-75%off-winner.com")
    if st.button("Check URL Risk"):
        score, reasons = calculate_risk(url)
        if score>=60:
            st.markdown(f"<div class='result-high'><h2>🔴 HIGH RISK - {score}%</h2><p>Is link pe click mat karo!</p></div>", unsafe_allow_html=True)
        elif score>=35:
            st.markdown(f"<div class='result-medium'><h2>🟡 MEDIUM RISK - {score}%</h2><p>Verify karke hi kholo</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-low'><h2>🟢 LOW RISK - {score}%</h2><p>Safe lag raha hai</p></div>", unsafe_allow_html=True)
        for r in reasons: st.write(f"- {r}")

with tab2:
    st.text_area("Message yaha paste karo")
    st.info("Same logic text ke liye bhi kaam karega")
with tab3:
    st.file_uploader("Fraud image upload karo")
    st.info("Future me isme OCR lagega")