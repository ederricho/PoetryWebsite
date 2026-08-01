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


st.set_page_config(
    page_title="Cobble Stones in Quebec City",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Cobble Stones in Quebec City")

st.markdown("""
Welcome.

This website is a collection of my poetry.

Use the navigation menu on the left to explore:

- About
- Poems
- Haiku
""")

st.divider()

st.markdown(
"""
> *"Poetry is simply the truth concentrated."*
>
> — Robert Frost
"""
)