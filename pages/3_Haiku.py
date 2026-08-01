import streamlit as st

st.title("Haiku")

haiku = [

{
"title":"Breeze",
"text":"""
An empty wine glass-

A painting left out to dry

A breeze that follows.

"""
},

{
"title":"Late",
"text":"""
Summer rain falling-

The sun shines a single ray

Little Anne runs wild.
"""
},

{
"title":"Goodbye",
"text":"""
You scream at your mother- 

The antique books you handle

Always break at the spine.

"""
},

{
"title":"Summer",
"text":"""
Heat-scorched white roses

Touch Angela’s blistered feet-

The sun still shines bright.
"""
},

{
"title":"One O'clock in the South",
"text":"""
The rain falls down

The sun shines in the distance

Jen’s feet drown in mud.

"""
},

{
"title":"Shower",
"text":"""
The rain- tenderly

Falls from the dark clouds above

And showers the orchids.

"""
},

]

for poem in haiku:

    st.subheader(poem["title"])

    st.markdown(poem["text"])

    st.divider()