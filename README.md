# Discrete Mathematics

### Social Network Analysis in Python

#### Social Network Analysis

The study of social structures using graph theory is called *social network analysis* (SNA). Thus, SNA is an area on the border of discrete maths and sociology. Vertices in social network graphs represent *actors*: people, social entities etc. Edges (also called *ties* or *links*) represent various *relations* between actors. The standard example is the friendship
relation in social networks.

#### Parameters of Social Network Graphs

Graph parameters of social network graphs are important for sociologists studying these networks. Some parameters of the graph behave specifically in the social network case (if compared to a random graph, for example). The clustering coefficients tend to be quite high. This reflects the fact that friends of one person are much more likely to be friends also. On the other hand, being highly clusterized, the social network happens to be tightly connected. The well-known theory of *six degrees of separation* (“six handshakes”) claims that any two people in the world are no more than six social connections from each other. In graph-theoretic terms, this means that the **diameter** of the social connections graph should be $\le$ 6.

#### Dataset

I'm going to use the SNAP (Stanford Network Analysis Project) dataset [ego-Facebook](https://snap.stanford.edu/data/ego-Facebook.html). This dataset consists of 'circles' (or 'friends lists') from Facebook. Facebook data was collected from survey participants using this Facebook app. The dataset includes node features (profiles), circles, and *ego networks*. Visualization makes clustering visible:

<p align="center">
<img src="https://github.com/Beorhthelm/discrete_mathematics/blob/85f787add57b64cc14a5df64d439f0f6de5d1b2c/Figure_1.png?raw=true" alt="Figure" width="70%">
</p>

#### Results

The experiment comparing graph from the Facebook dataset and an Erdős – Rényi graph shows that the average clustering coefficient (ACC) is much bigger on real data. Edge probability, however, is the same. The difference of the ACC comes from the fact that in the social network graph the edges are not independent. Indeed, the existence of edges A – B and A – C increases the probability of B – C. This is called the *small-world property*. Thus, we need better models for social network graphs, than Erdős – Rényi, for example, the Watts – Strogatz model. The Watts – Strogatz model was invented for better modelling of graphs with the
small-world property: good clustering, small average distance.
