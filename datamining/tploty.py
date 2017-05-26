# coding: utf-8

import plotly.plotly as py
import plotly
import plotly.figure_factory as ff

import numpy as np

X = np.random.rand(15, 15)
plotly.offline.init_notebook_mode(connected=True)
dendro = ff.create_dendrogram(X)
dendro['layout'].update({'width': 800, 'height': 500})
plotly.offline.iplot(dendro, filename='simple_dendrogram')

import plotly
from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

plotly.offline.iplot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})
