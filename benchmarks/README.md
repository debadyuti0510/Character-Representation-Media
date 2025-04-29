# Benchmarks
Benchmarking and experimental scripts and notebooks exploring the performance of DeepFace and CLIP on AffectNet and FairFace datasets.

## Prerequisites
The AffectNet and FairFace datasets need to be downloaded first:

- [AffectNet Dataset](http://mohammadmahoor.com/affectnet/)
- [FairFace Dataset](https://huggingface.co/datasets/HuggingFaceM4/FairFace)

The benchmarking code is a little messy, but most of it is straightforward and should require minimal intervention to reproduce.

Please install torch(cpu/gpu) from the official [pytorch website](https://pytorch.org/get-started/locally/).

After activating a virtual environment, run the following command:

`pip install -r requirements.txt`

### Note
There may be issues with running deepface on GPU locally, try using Kaggle/Colab environments to run the notebooks/scripts.
The benchmarks for deepface _may_ require a separate environment and you may need to install the requirements in the [deepface repository](https://github.com/serengil/deepface).

## Descriptions

`Demography_experiments` contain most fundamental CLIP Zero Shot and CLIP + LR experiment notebooks that explore and create the gender, race and affect models.

`experiment_scripts` explores different models to fit on top of CLIP embeddings for age estimation.

`deepface_age.ipnb` and `deepface_gender.ipynb` run evaluation experiments on the FairFace dataset using deepface models. 

Other notebooks contain miscallaneous EDA or visualizations to aid in the project. 