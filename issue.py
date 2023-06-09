import streamlit as st

if 'proof' not in st.session_state:
	st.session_state["proof"]=1
	st.write("st.session_state = ",st.session_state["proof"])
	st.stop()
else:
	st.session_state["proof"]+=1
	st.write("st.session_state = ",st.session_state["proof"])
reset_button=st.button("Reset session_state")
if reset_button:
	st.session_state={}
	st.experimental_rerun()
