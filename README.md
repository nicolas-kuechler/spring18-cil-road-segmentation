# CIL - Road Segmentation - 2018

Segmenting an image consists in partitioning an image into multiple segments (formally one has to assign a class label to each pixel). A simple baseline is to partition an image into a set of patches and classify every patch according to some simple features (average intensity). Although this can produce reasonable results for simple images, natural images typically require more complex procedures that reason abut the entire image or very large windows.

For this problem, we provide a set of satellite/aerial images acquired from GoogleMaps. We also provide ground-truth images where each pixel is labeled as {road, background}. Your goal is to train a classifier to segment roads in these images, i.e. assign a label {road=1, background=0} to each pixel.

## Useful Links
* [Trello Board](https://trello.com/b/D4NLabKT/cil)
* [Paper](https://v2.overleaf.com/7312313351mjgnqnjnsncf)
* [Kaggle](https://www.kaggle.com/c/cil-road-segmentation-2018)
* [Leonhard Wiki](https://scicomp.ethz.ch/wiki/Getting_started_with_clusters)
* [Tensorflow Doc](https://www.tensorflow.org/api_docs/python/)

## Getting Started

### Create a new Model

* Create Directory in Folder models/model_name (e.g. models/example)
* Create a config.py file with a class Config extending AbstractConfig
* adjust any configurations from the AbstractConfig file
* Create a model.py file with a class Model extending AbstractModel
* implement the build_model() method and set all necessary variables

### Run a Model

```
python main.py model_name mode
```

where model_name is the name of your model (defined by the folder it is in) and mode is either train or test

Example:
```
python main.py example train
```

### Prerequisites


### Installing



## Authors
