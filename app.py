
# import streamlit as st
# import joblib

# path = "models"  

# model_A = joblib.load(f"{path}/fine_tuned_logistic_imbalanced.pkl")  
# model_B = joblib.load(f"{path}/fine_tuned_svm_balanced.pkl")  
# vec_A = joblib.load(f"{path}/vectorizer_A.pkl")
# vec_B = joblib.load(f"{path}/vectorizer_B.pkl")

# st.markdown("""
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# body{
#     background:linear-gradient(135deg,#7b4397,#dc2430);
#     color: pink;
#     font-family:'Poppins', sans-serif;
# }
# .stApp{
#     background:#1c1c3c;
#     color:#f5f5f5;
#     padding:50px;
#     border-radius:20px;
#     box-shadow:0px 0px 30px rgba(0,0,0,0.5);
#     max-width:800px;
#     margin:50px auto;
# }
# h1{
#     color:gold !important;
#     text-align:center;
# }
# button[kind="primary"]{
#     background:gold !important;
#     color:black !important;
#     font-weight:bold !important;
#     border-radius:8px !important;
# }
# </style>
# """, unsafe_allow_html=True)


# st.set_page_config(page_title="Automated Review Rating System", page_icon="⭐", layout="centered")

# st.markdown("<h1 style='text-align:center; color:gold;'>⭐Automated Review Rating System⭐</h1>", unsafe_allow_html=True)
# # st.write("### Enter a review ")

# user_input = st.text_area("Enter Review Text:", height=150)

# if st.button("Predict Rating"):
#     review = user_input.strip()

#     if review == "":
#         st.warning("Please enter review to predict")
#     elif not any(char.isalpha() for char in review):  
#         st.error("Invalid review!!!")
#     else:
#         X_vec_A = vec_A.transform([review])
#         X_vec_B = vec_B.transform([review])

#         pred_A = model_A.predict(X_vec_A)[0]
#         pred_B = model_B.predict(X_vec_B)[0]

#         st.markdown("## Predictions")
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("### *Balanced Model*")
#             st.markdown(f"⭐ *{pred_B} Star*")
#         with col2:
#             st.markdown("### *Imbalanced Model*")
#             st.markdown(f"⭐ *{pred_A} Star*")


# chooosing the final model
import streamlit as st
import joblib


model = joblib.load("models/fine_tuned_svm_balanced.pkl")
vectorizer = joblib.load("models/vectorizer_B.pkl")

st.set_page_config(page_title="Automated Review Rating System", page_icon="⭐", layout="centered")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
body{
    background: linear-gradient(135deg, #1e3c72, #2a5298); /* blue background */
    color: #f5f5f5;
    font-family: 'Poppins', sans-serif;
}
.stApp{
    background: #004d1a;  /* dark green box */
    color: #f5f5f5;
    padding: 50px;
    border-radius: 20px;
    box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
    max-width: 800px;
    margin: 50px auto;
}
h1{
    color: gold !important;
    text-align: center;
}
button[kind="primary"]{
    background: gold !important;
    color: black !important;
    font-weight: bold !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>⭐ Automated Review Rating System ⭐</h1>", unsafe_allow_html=True)


user_input = st.text_area("Enter Review Text:", height=150)

if st.button("Predict Rating"):
    review = user_input.strip()
    if review == "":
        st.warning("Please enter a review to predict.")
    elif not any(char.isalpha() for char in review):
        st.error("Invalid review!")
    else:
        
        X_vec = vectorizer.transform([review])
        pred = model.predict(X_vec)[0]

        st.markdown("## Prediction")
        st.markdown(f"⭐ *{pred} Star*")
=======
# import streamlit as st
# import joblib

# path = "models"  

# model_A = joblib.load(f"{path}/fine_tuned_logistic_imbalanced.pkl")  
# model_B = joblib.load(f"{path}/fine_tuned_svm_balanced.pkl")  
# vec_A = joblib.load(f"{path}/vectorizer_A.pkl")
# vec_B = joblib.load(f"{path}/vectorizer_B.pkl")

# st.markdown("""
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# body{
#     background:linear-gradient(135deg,#7b4397,#dc2430);
#     color: pink;
#     font-family:'Poppins', sans-serif;
# }
# .stApp{
#     background:#1c1c3c;
#     color:#f5f5f5;
#     padding:50px;
#     border-radius:20px;
#     box-shadow:0px 0px 30px rgba(0,0,0,0.5);
#     max-width:800px;
#     margin:50px auto;
# }
# h1{
#     color:gold !important;
#     text-align:center;
# }
# button[kind="primary"]{
#     background:gold !important;
#     color:black !important;
#     font-weight:bold !important;
#     border-radius:8px !important;
# }
# </style>
# """, unsafe_allow_html=True)


# st.set_page_config(page_title="Automated Review Rating System", page_icon="⭐", layout="centered")

# st.markdown("<h1 style='text-align:center; color:gold;'>⭐Automated Review Rating System⭐</h1>", unsafe_allow_html=True)
# # st.write("### Enter a review ")

# user_input = st.text_area("Enter Review Text:", height=150)

# if st.button("Predict Rating"):
#     review = user_input.strip()

#     if review == "":
#         st.warning("Please enter review to predict")
#     elif not any(char.isalpha() for char in review):  
#         st.error("Invalid review!!!")
#     else:
#         X_vec_A = vec_A.transform([review])
#         X_vec_B = vec_B.transform([review])

#         pred_A = model_A.predict(X_vec_A)[0]
#         pred_B = model_B.predict(X_vec_B)[0]

#         st.markdown("## Predictions")
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("### *Balanced Model*")
#             st.markdown(f"⭐ *{pred_B} Star*")
#         with col2:
#             st.markdown("### *Imbalanced Model*")
#             st.markdown(f"⭐ *{pred_A} Star*")


# chooosing the final model
import streamlit as st
import joblib


model = joblib.load("models/fine_tuned_svm_balanced.pkl")
vectorizer = joblib.load("models/vectorizer_B.pkl")

st.set_page_config(page_title="Automated Review Rating System", page_icon="⭐", layout="centered")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
body{
    background: linear-gradient(135deg, #1e3c72, #2a5298); /* blue background */
    color: #f5f5f5;
    font-family: 'Poppins', sans-serif;
}
.stApp{
    background: #004d1a;  /* dark green box */
    color: #f5f5f5;
    padding: 50px;
    border-radius: 20px;
    box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
    max-width: 800px;
    margin: 50px auto;
}
h1{
    color: gold !important;
    text-align: center;
}
button[kind="primary"]{
    background: gold !important;
    color: black !important;
    font-weight: bold !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>⭐ Automated Review Rating System ⭐</h1>", unsafe_allow_html=True)


user_input = st.text_area("Enter Review Text:", height=150)

if st.button("Predict Rating"):
    review = user_input.strip()
    if review == "":
        st.warning("Please enter a review to predict.")
    elif not any(char.isalpha() for char in review):
        st.error("Invalid review!")
    else:
        
        X_vec = vectorizer.transform([review])
        pred = model.predict(X_vec)[0]

        st.markdown("## Prediction")
        st.markdown(f"⭐ *{pred} Star*")

