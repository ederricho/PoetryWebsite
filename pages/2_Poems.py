import streamlit as st
from poems import poems

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container{
    max-width:700px;
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

st.title("Poems")

for poem in poems:

    st.subheader(poem["title"])

    st.markdown(poem["text"])

    st.divider()