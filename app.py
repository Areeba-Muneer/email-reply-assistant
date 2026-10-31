import streamlit as st
from prompts import PURPOSES, TONES, build_prompt
from llm_client import generate_reply
from validator import validate_reply, ValidationError

st.set_page_config(page_title="AI Email Reply Assistant", page_icon="✉️")
st.title("✉️ AI-Powered Email Reply Assistant")
st.write("Paste an email, choose your goal and tone, then generate a reply.")

with st.form("reply_form"):
    email = st.text_area("Original email", placeholder="Paste the email you received here...", height=200)
    c1,c2 = st.columns(2)
    with c1: purpose = st.selectbox("Reply purpose", PURPOSES)
    with c2: tone = st.selectbox("Reply tone", TONES)
    custom = ""
    if purpose == "Custom / general":
        custom = st.text_input("Describe your goal")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.4, 0.1)
    submitted = st.form_submit_button("✨ Generate email reply", use_container_width=True)

if submitted:
    if not email.strip():
        st.error("Please paste the original email first.")
    elif purpose == "Custom / general" and not custom.strip():
        st.error("Please describe what you want the reply to do.")
    else:
        try:
            with st.spinner("Generating your reply..."):
                prompt = build_prompt(email, purpose, tone, custom)
                reply = generate_reply(prompt, temperature)
                validate_reply(reply)
                st.session_state["reply"] = reply
        except ValidationError as e:
            st.error(f"Reply validation failed: {e}")
        except Exception as e:
            st.error(str(e))

if st.session_state.get("reply"):
    st.subheader("Your AI-generated reply")
    st.text_area("Review and copy your reply", st.session_state["reply"], height=230)
    st.download_button("⬇️ Download reply as TXT", st.session_state["reply"], "email_reply.txt", "text/plain", use_container_width=True)
    st.info("Review names, dates, promises, and facts before sending.")

with st.expander("How to use"):
    st.markdown("1. Paste an email.\n2. Choose purpose and tone.\n3. Adjust creativity if needed.\n4. Click Generate email reply.\n5. Review and copy or download the draft.")
