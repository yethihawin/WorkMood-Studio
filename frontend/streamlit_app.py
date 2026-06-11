import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="WorkMood Studio", page_icon="🎨", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-header {
        text-align: center;
        padding: 2rem;
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        margin-bottom: 2rem;
    }
    .mood-card {
        background: rgba(255,255,255,0.15);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    .color-box {
        border-radius: 12px;
        transition: transform 0.3s;
    }
    .color-box:hover {
        transform: scale(1.05);
    }
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 30px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }
    footer {
        text-align: center;
        padding: 2rem;
        color: rgba(255,255,255,0.7);
    }
</style>
""", unsafe_allow_html=True)

# Dark/Light mode toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

col_mode, col_title = st.columns([1, 4])
with col_mode:
    if st.button("🌙" if not st.session_state.dark_mode else "☀️"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Update background based on mode
if st.session_state.dark_mode:
    st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); }
        .main-header { background: rgba(0,0,0,0.3); }
        .mood-card { background: rgba(255,255,255,0.1); }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎨 WorkMood Studio</h1>
    <p style="font-size: 1.2rem;">Turn workplace communication into visual mood boards</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">⚡ Powered by Microsoft Work IQ + GitHub Copilot</p>
</div>
""", unsafe_allow_html=True)

# Backend URL
BACKEND_URL = "http://localhost:8000"

# Check backend connection
with st.spinner("🔌 Connecting to backend..."):
    try:
        response = requests.get(f"{BACKEND_URL}/")
        if response.status_code == 200:
            st.success("✅ Backend API connected on port 8000")
        else:
            st.error("❌ Backend API not responding")
    except:
        st.error("❌ Cannot connect to backend. Run: uvicorn backend.app:app --reload --port 8000")

st.markdown("---")

# Two column layout for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("📧 Email Threads")
    emails_text = st.text_area(
        "Paste email conversations here", 
        height=200,
        placeholder="Example:\nWe need this urgent, client is waiting!\nGreat job team, confident about this launch\nThe deadline is approaching fast, please prioritize",
        help="One email per line. Work IQ will analyze the sentiment."
    )

with col2:
    st.subheader("🎙️ Meeting Transcripts")
    meeting_text = st.text_area(
        "Paste meeting notes here", 
        height=200,
        placeholder="Example:\nSpeaker 1: We need to deliver this by Friday\nSpeaker 2: Let's stay calm and focused\nManager: I'm confident in this team",
        help="Include speaker names for better context analysis."
    )

# Generate button
st.markdown("<br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    generate_clicked = st.button("🚀 Generate Mood Board", use_container_width=True)

if generate_clicked:
    if not emails_text and not meeting_text:
        st.warning("⚠️ Please enter at least one email or meeting transcript")
    else:
        with st.spinner("🧠 Work IQ is analyzing your communication..."):
            emails = [e.strip() for e in emails_text.split("\n") if e.strip()]
            transcripts = [t.strip() for t in meeting_text.split("\n") if t.strip()]
            
            payload = {
                "emails": emails,
                "meeting_transcripts": transcripts
            }
            
            try:
                response = requests.post(f"{BACKEND_URL}/generate-mood-board", json=payload, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.balloons()
                    st.success("✨ Mood board generated successfully!")
                    
                    # Display results in styled cards
                    st.markdown("---")
                    st.subheader("🎨 Your Mood Board")
                    
                    # Row 1: Mood Keywords
                    with st.container():
                        st.markdown('<div class="mood-card">', unsafe_allow_html=True)
                        st.markdown("### 🎭 Mood Keywords")
                        keywords_html = " ".join([f'<span style="background: rgba(255,255,255,0.2); padding: 5px 15px; border-radius: 20px; margin: 5px; display: inline-block;">{k}</span>' for k in data["mood_keywords"]])
                        st.markdown(keywords_html, unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Row 2: Color Palette
                    with st.container():
                        st.markdown('<div class="mood-card">', unsafe_allow_html=True)
                        st.markdown("### 🎨 Color Palette")
                        
                        cols = st.columns(len(data["color_palette"]))
                        for idx, color in enumerate(data["color_palette"]):
                            with cols[idx]:
                                st.markdown(f'''
                                <div style="background-color:{color}; height:80px; border-radius:12px; margin:5px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);"></div>
                                <p style="text-align:center; font-size:12px;">{color}</p>
                                ''', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Row 3: Style Directions
                    with st.container():
                        st.markdown('<div class="mood-card">', unsafe_allow_html=True)
                        st.markdown("### 🖼️ Style Directions")
                        
                        style_col1, style_col2 = st.columns(2)
                        with style_col1:
                            st.markdown(f"**📷 Imagery**  \n{data['style_directions']['imagery']}")
                            st.markdown(f"**💡 Lighting**  \n{data['style_directions']['lighting']}")
                        with style_col2:
                            st.markdown(f"**🎨 Texture**  \n{data['style_directions']['texture']}")
                            st.markdown(f"**🌟 Example Visuals**  \n{data['style_directions']['example_visuals']}")
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Work IQ Insights
                    st.markdown("---")
                    st.subheader("📊 Work IQ Insights")
                    
                    insight_col1, insight_col2, insight_col3 = st.columns(3)
                    with insight_col1:
                        st.metric("Primary Sentiment", data["primary_sentiment"].replace("_", " ").title())
                    with insight_col2:
                        st.metric("Confidence", f"{data['confidence']*100:.0f}%")
                    with insight_col3:
                        st.metric("Keywords Found", len(data["mood_keywords"]))
                    
                else:
                    st.error(f"❌ Error {response.status_code}: Something went wrong")
                    
            except requests.exceptions.Timeout:
                st.error("⏰ Request timeout. Please try again.")
            except Exception as e:
                st.error(f"🔌 Connection error: {e}")

# Footer
st.markdown("---")
st.markdown("""
<footer>
    <p>💡 <strong>How it works:</strong> WorkMood Studio uses Microsoft Work IQ to detect emotional context from workplace communication. 
    It then generates a visual mood board with colors, imagery, and style directions for creative teams.</p>
    <p>🏆 Built for <strong>Agents League Hackathon 2026</strong> - Creative Apps Track</p>
    <p>🤖 Developed with <strong>GitHub Copilot</strong> + <strong>Microsoft Work IQ</strong></p>
</footer>
""", unsafe_allow_html=True)