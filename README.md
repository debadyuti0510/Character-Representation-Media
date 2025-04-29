# Character Representation Analysis in Media

An end-to-end tool that allows the extraction and visualization of demography data like Age, Gender, Race and Emotion/Affect in an interactive dashboard with minimal intervention. 

## Prerequisites
Please install torch(cpu/gpu) from the official [pytorch website](https://pytorch.org/get-started/locally/).

After activating a virtual environment, run the following command:

`pip install -r requirements.txt`

### Note
There may be issues with running deepface on GPU locally, try using Kaggle/Colab environments to run the notebooks/scripts.
The benchmarks for deepface _may_ require a separate environment and you may need to install the requirements in the [deepface repository](https://github.com/serengil/deepface).

## Running the pipeline

Execute the following command to run the pipeline on a video file of your choice from the pipeline directory:

To generate visualizations - 
`python pipeline.py -v "path/to/video"`

To generate a CSV dump - 
`python pipeline.py -d "path/to/video"` 

The dashboard of interactive visualizations should show up on : `http://127.0.0.1:8050`

## Demography Model Benchmarks

The AffectNet and FairFace datasets need to be downloaded first:

- [AffectNet Dataset](http://mohammadmahoor.com/affectnet/)
- [FairFace Dataset](https://huggingface.co/datasets/HuggingFaceM4/FairFace)

The benchmarking code is a little messy, but most of it is straightforward and should require minimal intervention to reproduce.

## Visualization

## User Study - Data and Analysis

