import streamlit as st
import tensorflow as tf
from tensorflow import keras
from urllib.request import urlopen
import matplotlib.pyplot as plt
from PIL import Image
from numpy import asarray
import base64

generator = keras.models.load_model('C:/Users/Neel/PycharmProjects/VanGoghExperience',compile=False)

def generate_images(model, test_input):
    prediction = model(test_input)
    plt.figure(figsize=(4, 4))
    display_list = [prediction[0]]
    i=0
    plt.imshow(display_list[i]* 0.5 + 0.5)
    plt.axis('off')
    plt.show()
    plt.savefig('van.jpg', dpi=300, bbox_inches='tight')

def input_image(url):
    img = Image.open(urlopen(url))
    img.save('original.jpg')
    basewidth = 256
    hsize = 256
    img = img.resize((basewidth, hsize))
    img=asarray(img)
    img.astype('float32')
    img = (img / 127.5) - 1
    image_tensor = tf.convert_to_tensor(img, dtype=tf.float32)
    image_tensor = tf.expand_dims(image_tensor, 0)
    return image_tensor


st.markdown("<h1 style='text-align: center; color:#111111;font-size:44px;'>The Van Gogh Experience</h1>",
            unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color:#000000;font-size:30px;'><b>Get your own Van Gogh style Image</b></h2>",
            unsafe_allow_html=True)

main_bg = "starrynight.jpg"#,"forest.jpg","road.jpg","field.jpg","Corner-of-Voyer-dArgenson-Park-at-Asnieres.jpg"]
main_bg_ext = "jpg"
st.markdown(
    f"""
    <style>
    .reportview-container{{

    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
    max-width:100%
    height: 100%;

     /* Center and scale the image nicely */
     background-position: center;
      background-repeat: no-repeat;
    background-size: cover;
    }}

    </style>
    """,
    unsafe_allow_html=True
    )
user_input = st.text_input("Input your Image url here")

if user_input != "":
    def load_image():
        input_img =input_image(user_input)
        return input_img


    inp = load_image()

col1, col2, col3 , col4, col5 = st.beta_columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Generate')


if center_button:
    with st.spinner('Generating Van Gogh Image...'):  # loader widget
        generate_images(generator,inp)
        st.image('van.jpg')
    st.success('Van Gogh Image Generated Successfully!')  # success widget

footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
}

a:hover,  a:active {
color: black;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>
<div class="footer">
<h3><b>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/BlueBlaze6335" target="_blank">BlueBlaze</a></b>
</h3></div>
"""
st.markdown(footer,unsafe_allow_html=True)