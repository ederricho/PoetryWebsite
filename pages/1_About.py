import streamlit as st

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

st.title("About")

#st.image("images/headshot.jpeg", width=275)

st.divider()

st.markdown("""
My name is **Edgar Derricho**.

I am a poet, statistician, and teacher living in Georgia.

Many of these poems explore

- loneliness
- faith
- memory
- hope
- beauty
- ordinary life

Thank you for reading.
""")