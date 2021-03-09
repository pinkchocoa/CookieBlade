from GUIWidgets import *


day = [0,1,2,3,4,5,6,7,8,9,10]
views = [0,30,32,34,32,33,31,29,32,35,45]
App = StartApp()
GraphWindow = NewWindow("Graph", 800, 600)
Graph = NewGraph(GraphWindow.QWin, 0, 0, 800, 600)
Graph.plotGraph(day, views, "b", "o")
Graph.setBackGroundColor("w")
Graph.setGraphTitle("View Count Graph", "r", "30pt")
Graph.setAxisLabel("left", "Views", "red", "20pt")
Graph.setAxisLabel("bottom", "Day", "red", "20pt")
Graph.setAxisIntervalTo1("left", views)
exporter = exporters.ImageExporter(Graph.Graph.plotItem)
exporter.export("Graph.jpeg")
