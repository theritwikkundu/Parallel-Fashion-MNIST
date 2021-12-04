import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from PIL import Image
import pickle

#headings
st.title("Prediction of Fashion Items using Parallel Classifier")
st.subheader("This application uses parallel Extra Trees Classifier trained on the Fashion MNIST dataset")

pca= pickle.load(open("pca.pkl",'rb'))

dictionary = {
    0 : 'T-shirt/top',
    1 : 'Trouser',
    2 : 'Pullover',
    3 : 'Dress',
    4 : 'Coat',
    5 : 'Sandal',
    6 : 'Shirt',
    7 : 'Sneaker',
    8 : 'Bag',
    9 : 'Ankle boot'
}


image_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
if image_file is not None:
    st.image(Image.open(image_file),width=250)
    img=Image.open(image_file)
    arr2 = [[0] * 28 for i in range(28)]
    for i in range(0, 28):
        for j in range(0, 28):
            coordinate =(i, j)
            arr2[j][i] = img.getpixel(coordinate)
    arr1 = list(np.concatenate(arr2).flat)
    column_name=['pixel'+str(i) for i in range(1,785)]
    X_test1 = pd.DataFrame(np.array(arr1).reshape(-1,len(arr1)),columns = column_name)   
    X_test1 = pca.transform(X_test1)
    X_test1 = pd.DataFrame(X_test1,columns = column_name[0:84])
    print(X_test1)
    loaded_model = pickle.load(open("parallelmodel.sav", 'rb'))
    print("hi")
    prediction = loaded_model.predict(X_test1)
    value1=""
    for key, value in dictionary.items():
        if key == prediction:
            print(value)
            value1=value
    if value!="":
        st.markdown('<p style="font-size: 20px;">The predicted clothing is: </p>', unsafe_allow_html=True)
        st.title(value1)