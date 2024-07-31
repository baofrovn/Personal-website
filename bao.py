import base64
from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

current_dir = Path().parent if "_file_" in locals() else Path.cwd()
css_file = current_dir/ "styles" /"main.css"
resume = current_dir/"assets"/ "cv.pdf"
profile= current_dir/"assets"/ "profile-pic (10).png"

st.set_page_config(page_title="Personal Portfolio | Bao Pham", page_icon="16330881678370942 - Copy.png")
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume,"rb") as pdf_file:
  PDFbyte = pdf_file.read()
profile_pic = Image.open(profile)

col1, col2 = st.columns(2, gap="small")
with col1:
  st.image(profile_pic,width=230)
with col2:
  st.title("Pham Quoc Bao")
  st.write("Studying at VNU-HCM High School for the Gifted")
  st.write("Studied at Tam Binh secondary school")
  st.download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name=resume.name,
  )
  st.write("✉️"," ","baofromvn2007@gmail.com")

st.write('\n')
col1, col2, col3, col4= st.columns(4,gap="small")
with col1:
  st.markdown(
    """<a href="https://www.facebook.com/profile.php?id=100035521181531">
    <img src="data:image/png;base64,{}" width="70">
    </a>""".format(
        base64.b64encode(open("icons8-facebook-100.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with col2:
  st.markdown(
    """<a href="https://www.linkedin.com/in/bao-pham-065479318/">
    <img src="data:image/png;base64,{}" width="70">
    </a>""".format(
        base64.b64encode(open("icons8-linkedin-100.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with col3:
  st.markdown(
    """<a href="https://github.com/baofrovn">
    <img src="data:image/png;base64,{}" width="70">
    </a>""".format(
        base64.b64encode(open("icons8-github-100.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
with col4:
  st.markdown(
    """<a href="https://x.com/bao154688">
    <img src="data:image/png;base64,{}" width="70">
    </a>""".format(
        base64.b64encode(open("icons8-twitter-logo-100.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
st.write('\n')
st.header("My Goals & Objectives")
st.write("---")
st.write(
  """

  """
)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

python = load_lottieurl("https://lottie.host/493ce4ce-7e7f-495d-ad1d-1096b26be2a7/1nS91EtizC.json")
git = load_lottieurl("https://lottie.host/286708e0-8dc2-4dd9-ab2f-b900172154d9/yjsDNzdvdH.json")
tf = load_lottieurl("https://lottie.host/d453722a-c5ff-479f-abfb-5ea16c87ee48/MrdGuoYDzU.json")
html = load_lottieurl("https://lottie.host/ce0c8c60-4223-4093-8e50-b4a9cd10396d/xx2d5BvSGG.json")
css = load_lottieurl("https://lottie.host/755259ad-ac4d-4808-97f4-77521a6c81a3/5gEV6sSxEO.json")
st.write('\n')
with st.container():
    st.subheader('Programming Language')
    st.write("---")
    col1, col2, col3,col4, col5= st.columns([1, 1, 1, 1, 1])
    with col1:
        st_lottie(python, height=90,width=90, key="python", speed=2.5)
    with col2:
        st_lottie(git, height=90,width=90, key="git", speed=2.5)
    with col3:
        st_lottie(tf, height=90,width=90, key="tf", speed=2.5)
    with col4:
        st_lottie(html, height=90,width=90, key="ht", speed=2.5)
    with col5:
        st_lottie(css, height=90,width=90, key="cs", speed=2.5)
    
        
st.write('\n')
st.header("My Projects & Activities")
st.write("---")
st.write("📖", ":blue[PTNK Program in Interdisciplinary Sciences & Education - School Program]")
st.write(
    """


"""
)
st.image("received_1481589349449757.jpeg")

st.write("\n")
st.write("\n")
st.write("📖", ":blue[AIoT Lab VN at International university - National University HCMC]")
st.write(
    """


"""
)
st.image("449677624_453608770932861_6930925445494524292_n.jpg")

st.write("\n")
st.write("\n")
st.write("📖", ":blue[Volunteering at Summer campaign 2024]")
st.write(
    """


"""
)
st.image("summer.jpg")
