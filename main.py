import streamlit as st
from gtts import gTTS
from IPython.display import Audio
import streamlit_custome_css as leo


leo.header_hide()
leo.bg_image("https://64.media.tumblr.com/6c528dab5498d431a101acd4398160b4/tumblr_o7vrxl8Uk11runoqyo10_540.gifv")
# Streamlit UI



st.markdown("""<center><h1 style="color: #FFFF00;">Text to Speech Converter in Indian Language</h1></center>""",unsafe_allow_html=True)
# Text input for the user to enter text
text_input = st.text_area("Enter Text", "வணக்கம், எப்படி இருக்கின்றீர்கள்?")
html_code = """
<html>
<head>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            padding: 20px;
            color: #333;
        }
        h2 {
            text-align: center;
            color: #007bff;
        }
        .languages {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 20px;
        }
        .language {
            font-size: 18px;
            font-weight: bold;
            margin: 10px;
            padding: 8px 12px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        .language:hover {
            background-color: #007bff;
            color: white;
        }
        .en { background-color: #4caf50; }
        .hi { background-color: #f44336; }
        .ta { background-color: #ff9800; }
        .te { background-color: #9c27b0; }
        .kn { background-color: #03a9f4; }
        .ml { background-color: #8bc34a; }
        .bn { background-color: #ff5722; }
        .mr { background-color: #607d8b; }
        .gu { background-color: #795548; }
        .pa { background-color: #e91e63; }
        .or { background-color: #cddc39; }
        .as { background-color: #9e9e9e; }
    </style>
</head>
<body>
    <h2>Supported Languages</h2>
    <div class="languages">
        <div class="language ta">ta: Tamil</div>
        <div class="language en">en: English</div>
        <div class="language hi">hi: Hindi</div>
        <div class="language te">te: Telugu</div>
        <div class="language kn">kn: Kannada</div>
        <div class="language ml">ml: Malayalam</div>
        <div class="language bn">bn: Bengali</div>
        <div class="language mr">mr: Marathi</div>
        <div class="language gu">gu: Gujarati</div>
        <div class="language pa">pa: Punjabi</div>
        <div class="language or">or: Oriya</div>
        <div class="language as">as: Assamese</div>
    </div>
</body>
</html>
"""

# Render the HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)


# Language selection dropdown (default to Tamil 'ta', but can be changed to other languages like 'en', 'fr', etc.)
language = st.selectbox("Select Language", ["ta", "hi", "en", "te", "kn", "ml", "bn", "mr", "gu", "pa", "or", "as"] )





# Button to convert text to speech
if st.button("Convert to Speech"):
    if text_input:
        # Generate speech
        speech = gTTS(text=text_input, lang=language, slow=False,tld="com.au")
        # Save the speech to an mp3 file
        speech.save("output.mp3")

        # Provide the audio file as a download link and play it within the app
        st.audio("output.mp3", format="audio/mp3")
        st.success(f"Speech saved as 'output.mp3' in {language}!")
    else:
        st.warning("Please enter some text.")
