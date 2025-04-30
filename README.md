# Character Representation Analysis in Media

![Image](https://github.com/user-attachments/assets/edfa1e8b-c261-4504-9d24-a8c56c61951e)

## Pipeline
This project includes a complete pipeline to extract demographic attributes such as age, gender, race, and emotion from media content. The tool processes videos and outputs either interactive dashboards or structured CSV files for further analysis. It is designed for minimal setup and rapid deployment.

## Demography Model Benchmarks
We benchmarked demographic prediction models on the AffectNet and FairFace datasets. Both zero-shot and fine-tuned CLIP models were evaluated, alongside DeepFace models for baseline comparisons. The benchmarking scripts explore model performance across age, gender, race, and affect prediction tasks.

## Visualization
The visualization component consists of a Flask back-end and a React front-end. It enables users to explore demographic analytics from processed media in an interactive web application. The dashboard allows intuitive navigation through the demographic insights extracted from the pipeline.

## User Study - Data and Analysis
A user study with 30 participants was conducted to assess the understandability, trustworthiness, and usability of the demographic analytics tool. Collected data included both closed-form and open-ended responses, analyzed using Bayesian inference and qualitative coding techniques.
