<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

---

<h1 align="center">Parallel Fashion MNIST</h1>

_The lack of parallel processing in machine learning tasks inhibits economy of performance. With the horizons of Machine learning growing exponentially day by day, the complexity of the algorithms and the size of the data seems to be growing too. However, these models are notorious for their lengthy wait times while training. Thus, it is important to understand how we can effectively reduce the time taken by the model without compromising the efficiency. The aim of this project is to reduce the computational load and increase the speed of training a neural network that can predict fashion items based on the Fashion MNIST dataset, by using parallelization._

---

<br>

> The main objective of the project is to create a parallelized machine learning model that can be used to predict fashion items using an uploaded image.

<br>

1. Detailed **EDA (Exploratory Data Analysis)** to uncover different features of the dataset to give an elaborate understanding of the data.

2. Data is pre-processed and cleaned to reduce the overheads. The efficiency of the model is increased by standardisation using **StandardScaler** & dimensionality reduction using **PCA (Principal Component Analysis)**.

3. Different linear and tree-based **parallelised algorithms** are trained and their performance is evaluated using **accuracy**, **precision**, **recall** and **F1 score** metrics.

4. An individual module is created using the best performing model, namely **Extra Trees Classifier** which accepts an image and tests it using the trained model.

5. The classifier model is exported to a **Pickle file** to be stored as a binary file.

6. The fronetnd developed using **Streamlit** imports the Pickle file, provides an upload field to the user to upload an image, which is classified using the previously trained model.

---

<br>

- The project is developed in `Python` on Jupyter Notebook.

- The dataset has been collected from [Fashion MNIST](https://www.kaggle.com/datasets/zalando-research/fashionmnist "Kaggle") dataset on `Kaggle`.

---

<br>

## Developer 👨‍💻

<p align="center">
	<a href = 'https://github.com/theritwikkundu' target='_blank'> <img src=https://github.com/edent/SuperTinyIcons/blob/master/images/svg/github.svg height='40px' /></a>
    &nbsp;
<p>

---

Please ⭐️ this repository if this project helped you!


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/theritwikkundu/Parallel-Fashion-MNIST.svg?style=for-the-badge
[contributors-url]: https://github.com/theritwikkundu/Parallel-Fashion-MNIST/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/theritwikkundu/Parallel-Fashion-MNIST.svg?style=for-the-badge
[forks-url]: https://github.com/theritwikkundu/Parallel-Fashion-MNIST/network/members
[stars-shield]: https://img.shields.io/github/stars/theritwikkundu/Parallel-Fashion-MNIST.svg?style=for-the-badge
[stars-url]: https://github.com/theritwikkundu/Parallel-Fashion-MNIST/stargazers
[issues-shield]: https://img.shields.io/github/issues/theritwikkundu/Parallel-Fashion-MNIST.svg?style=for-the-badge
[issues-url]: https://github.com/theritwikkundu/Parallel-Fashion-MNIST/issues
[license-shield]: https://img.shields.io/github/license/theritwikkundu/Parallel-Fashion-MNIST.svg?style=for-the-badge
[license-url]: https://github.com/theritwikkundu/Parallel-Fashion-MNIST/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/theritwikkundu/