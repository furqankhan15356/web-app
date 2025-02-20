import streamlit as st
import random
from datetime import datetime

# App Configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🧠",
    layout="wide"
)

# Session State Initialization
if 'entries' not in st.session_state:
    st.session_state.entries = []
if 'challenge' not in st.session_state:
    st.session_state.challenge = None

# App Content
def main():
    st.title("🧠 Growth Mindset Challenge")
    st.markdown("---")
    
    # Hero Section
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.header("Unlock Your Potential")
            st.markdown("""
            **Develop a growth mindset** with daily practice!
            - Embrace challenges
            - Learn from setbacks
            - Celebrate progress
            - Cultivate resilience
            """)
            
        with col2:
            st.image("https://images.unsplash.com/photo-1494173853739-c21f58b16055?auto=format&fit=crop&w=800", 
                    caption="Growth Mindset Journey")

    # Features
    st.markdown("---")
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Learn", "🎯 Challenge", "📝 Journal", "📈 Progress"])

    with tab1:
        st.header("What is Growth Mindset?")
        with st.expander("Core Principles"):
            st.markdown("""
            - **Intelligence can be developed**
            - **Embrace challenges**
            - **Persist through obstacles**
            - **Learn from criticism**
            - **Find inspiration in others' success**
            """)
        
        with st.expander("Daily Affirmation"):
            affirmation = random.choice([
                "Today I embrace learning opportunities!",
                "Mistakes are my stepping stones to success!",
                "My effort is the path to mastery!",
                "Challenges help me grow stronger!"
            ])
            st.subheader(affirmation)

    with tab2:
        st.header("Daily Challenge")
        challenges = [
            "Learn something new for 30 minutes",
            "Reframe a mistake as a learning opportunity",
            "Try a different approach to a problem",
            "Give constructive feedback to someone",
            "Practice a skill you want to improve"
        ]
        
        if st.button("Generate New Challenge"):
            st.session_state.challenge = random.choice(challenges)
        
        if st.session_state.challenge:
            st.subheader("Your Challenge:")
            st.markdown(f"### 🚀 {st.session_state.challenge}")
            st.write("Share your progress with #GrowthMindsetChallenge")

    with tab3:
        st.header("Reflection Journal")
        reflection = st.text_area("Today's Reflection (What did you learn? How did you grow?)", 
                                height=150)
        
        if st.button("Save Entry"):
            entry = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "content": reflection
            }
            st.session_state.entries.append(entry)
            st.success("Entry saved!")
        
        st.subheader("Past Entries")
        for entry in reversed(st.session_state.entries):
            st.markdown(f"**{entry['date']}**")
            st.write(entry['content'])
            st.markdown("---")

    with tab4:
        st.header("Progress Tracker")
        if st.session_state.entries:
            st.subheader(f"Total Reflections: {len(st.session_state.entries)}")
            st.line_chart({
                'Reflections': [i+1 for i in range(len(st.session_state.entries))]
            })
        else:
            st.info("Start journaling to track your progress!")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center">
        <p>🔁 Remember: Growth is a continuous journey, not a destination</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()