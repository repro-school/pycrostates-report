# Pycrostates Report

## Introduction

The goal of this brainhack project is to develop a basic BIDS App that computes EEG microstate clustering solutions and helps researchers choose the best among them.

### What is a BIDS App?

A BIDS App is a container image capturing a neuroimaging pipeline that takes a BIDS formatted dataset as input. BIDS (Brain Imaging Data Structure) is an emerging standard for organizing and describing neuroimaging datasets. Each BIDS App has the same core set of command line arguments, making them easy to run and integrate into automated platforms. BIDS Apps are constructed in a way that does not depend on any software outside of the image other than the container engine.

## Report

The report is an HTML file that provides interactive visualizations of the BIDS App outputs. This report aims to address the following statement:

*As a researcher, I want to choose the optimal number of microstate topographies to use for my analysis.*

Here is a list of graphical elements that can address this problem (this list can be modified as ideas evolve and Brainhack progresses):

### A global view with:

- Microstate topographies for each value of K.
  - The spatial correlation between those topographies ([example image](https://onlinelibrary.wiley.com/cms/asset/f2d1a02e-89c6-4dc2-8590-ed793748f677/hbm25834-fig-0002-m.jpg)).
  - These topographies can be further matched using [Pycrostates optimize_order](https://pycrostates.readthedocs.io/en/latest/api/generated/pycrostates.cluster.utils.optimize_order.html#pycrostates.cluster.utils.optimize_order).

- The global explained variance as a function of K: Global Explained Variance (GEV) is a metric used to quantify the amount of variance in the EEG data that is accounted for by the identified microstates. It provides an estimate of how well the microstates capture the temporal dynamics of the EEG signal.

- 2D embeddings of clustering solutions: By embedding the high-dimensional data into a 2D space, it becomes easier to visualize the clusters and their relationships. Each data point can be represented as a dot on a scatter plot, where points belonging to the same cluster tend to be closer together. This visualization allows for a qualitative assessment of the clustering results using techniques such as [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html), [UMAP](https://umap-learn.readthedocs.io/en/latest/), and [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html).

- Clustering Metrics: These metrics provide quantitative measures of the quality and effectiveness of clustering results. Some metrics are already implemented in the [Pycrostates metrics module](https://pycrostates.readthedocs.io/en/latest/api/metrics.html), while others, such as Within-cluster sum of squares (WCSS) and Gap statistic, are not yet implemented.

### A solution-specific view

The Pycrostates Report may also include a solution-specific view for each K value, focusing on individual subjects or recordings within the dataset. This view provides the following information:

- GEV distribution for each subject/recording.
- The correlation between the group and subject solutions for each microstate map.

By incorporating these graphical elements and insights, the Pycrostates Report aims to facilitate the selection of the optimal number of microstate topographies for EEG analysis. Researchers can make informed decisions based on both visual assessments and quantitative metrics, ultimately enhancing the quality and interpretability of their microstate analysis.

### Interactivity and Visualization

To enhance the interactivity and visualization capabilities of the Pycrostates Report, we can utilize interactive plotting libraries such as Bokeh and Plotly. These libraries provide powerful tools to create interactive and dynamic visualizations, allowing researchers to explore and analyze the data more effectively.