# The Van Gogh Experience !!!

## This is a streamlit web-app that converts any image to a Van Gogh painting's styled image. 

### Details :

**AI and Machine Learning technique like GAN is used to generate a stylized image from the input image. The CycleGAN model has been trained on Van Gogh's paintings and normal images so that it can learn the style of the great artist and forge it on your picture !!  **

The streamlit app takes your input as in an URL of the picture or a picture from your destop , converts it to a tensor , and then passes the tensor through the model (saved keras model ) and ***voila*** !! You get your picture personally made by the one eared Artist !!

<p align="center">
    <img src="https://github.com/BlueBlaze6335/Van-Gogh-Experience/blob/master/Static/sc1.jpg" alt="Logo" width="480" height="360">
    <img src="https://github.com/BlueBlaze6335/Van-Gogh-Experience/blob/master/Static/sc2.jpg" alt="Logo" width="480" height="360">
</p>

### Results :


<div align="center">
    <img src="https://github.com/BlueBlaze6335/Van-Gogh-Experience/blob/master/Static/original.jpg" alt="Original" width="300" height="200">
</div>
<h3 align="center"> Original Image</h3>
<div align="center">
    <img src="https://github.com/BlueBlaze6335/Van-Gogh-Experience/blob/master/Static/van.jpg" alt="Output" width="300" height="200">
</div>
<h3 align="center"> Output Image</h3>

### How to Run :

* First step :

  ```
  $ git clone https://github.com/BlueBlaze6335/Van-Gogh-Experience
  $ cd Van-Gogh-Experience
  $ pip install -r requirements.txt
  ```
* Second step :
  
  Download the [variables folder](https://drive.google.com/drive/folders/1EVV-MULab_H2ZhTpStK8qSb1WfsrWLpp?usp=sharing) and save this inside the project folder !!
  The app wont run without this , because this has the support variables for the saved model !!
  
* Third step :
  
  ```
  $ streamlit run app.py
  ```
 ### Link to demo Video :
 
 * Demo 1 - [link](https://drive.google.com/file/d/1iuLLBz9MbwWIcWhS7xMcW_hAnQBi4qZD/view?usp=sharing)
 * Demo 2 - [link](https://drive.google.com/file/d/1B4Q8w3DI3uokcEEmpsyt0E7RrjVNsSVl/view?usp=sharing)


***If you like the project , show some love by starring the repo !!***

***Saved model taken from this [project](https://github.com/BlueBlaze6335/Artistic-Style-Transfer-with-CycleGAN) !!***
