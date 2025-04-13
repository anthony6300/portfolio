import streamlit as st
from base64 import b64encode


def web_portfolio():
    # page Config
    st.set_page_config(page_title="Anthony Ojei's Portfolio",page_icon="⭐")
    # set the page title
    st.write(f"""
    <div class ="title" style = "text-align: center; " >
            <span style = "font-size : 32px;" >hello! My Name is Anthony Ojei </span>👏 
    </div>
    """ , unsafe_allow_html=True)

    st.markdown("<style>div.block-container{padding-top:3rem;}</style", unsafe_allow_html=True)

    # Get profile Image
    with open("db.png","rb") as img_file:
        img =" data: image/png;base64," + b64encode(img_file.read()).decode()

    #Reading Profile
    with open("profile.pdf","rb") as pdf_file:
        pdf_bytes =pdf_file.read()

    # st.write(f"""
    # <div style = "display: flex; justify-content: center;" >
    #     <div class ="box" >
    #         <img src = "{img}" alt="Athony Ojei" style =" width:300px; height:200px;"> 
    #     </div>
    # </div>    
    # """ ,
    # unsafe_allow_html=True)

    # Animation
    st.write(f"""
    <style>
    @keyframes slowTilt {{
    0%, 100% {{
    transform: rotate(0deg);         
    }}
    50%{{
    transform: rotate(5deg);
    }}         
    }}
    .box img{{
    width:300px;
    height:200px;
    border-radius: 50%;
    animation: slowTilt 3s ease-in-out infinite;
    }}
    </style>
    <div style = "display: flex; justify-content: center;" >
    <div class ="box" >
    <img src = "{img}" alt="Athony Ojei" style =" width:300px; height:200px;"> 
    </div>
    </div> 
    """,
    unsafe_allow_html=True)

    # set  the titile
    st.write(f"""
    <div class= "subtitle" style= "text-align: center; font-size:30px; "> Junior Python Developer
    </div>
    """, unsafe_allow_html=True)

    social_icon_data = {
        "Linkedin": [ "www.linkedin.com/in/anthony-ojei-1831862b6", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "Github": ["https://github.com/anthony6300/Anthonyojei-API.git" , "https://cdn-icons-png.flaticon.com/128/270/270798.png"],
        "another": ["https://github.com/anthony6300/ojeiblog.git" , "https://cdn-icons-png.flaticon.com/128/25/25657.png"],
        
    }
    
    social_icon_html = [
    f"<a  href= '{social_icon_data[platform][0]}' target='_blank' style='magin-right: 10px;'>"
    f"<img class='social_icon' src= '{social_icon_data[platform][1]}' alt= '{platform}'"
    f" style=' width: 25px; height: 25px;'></a> "
    for platform in social_icon_data
    ]
    
    st.write(f"""
    <div style= "display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icon_html)}
    </div>
    """, unsafe_allow_html=True)

    
    
    

    # About Me Set
    st.subheader("About Me")
    st.markdown("""
    BLUELINE URBAN PROJECT 
    - ๋࣭ ⭑✮💻₊ ⊹ i work as a FREELANCER in [Blueline urban Project](https://www.businesslist.com.ng/company/260746/blueline-urban-projects#google_vignette)            
    - 🌐 i Creating dynamic and interactive web pages which improved customer interaction by 40%.
    - ⚛️ i Worked on HTML,CSS,JAVASCRIPT and PYTHON in development of projects, with focus on data fetching and cleansing.
    - ✨ i Assisted in building API’S on top of cleaned data set which helped to automate flow from multiple sources.
    - 🛢️ i worked on storing extracted data into SQLAlchemy database.
    - 🚀i Develop GUI(Graphic User interface) for secondary school as a teaching aid.
    -🎬 i Help in Version Control by storing future projects in GITHUB for public views. 
    """)
    st.write("##")
    #Download Cv bottom
    st.download_button(label="📩Download My CV", data=pdf_bytes,file_name="Anthony_Linkedin_CV.pdf",mime="application/pdf",)
    st.write("##")
    st.write(f"""
    <div class="subtitle" style= "text-align: center;">⭐ Have A Wonderful Day!!!⭐</div
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    web_portfolio()
