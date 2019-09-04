# Plant Network Visualization
POC for text network construction and Analysis

Steps : 

Install Dependencies of numpy and flask

pip install numpy flask

Install python-louvain and compatible networkx package using following 

pip install -U git+https://github.com/taynaud/python-louvain.git

Run - run plant_network.py file using "python plant_network.py"

If you face version mismatch of following issue with NetworkX and python-louvain (community) then install following version of python-louvain
developed by  [Thomas Aynaud ](https://github.com/taynaud)

pip install -U git+https://github.com/taynaud/python-louvain.git

Issue faced : AttributeError: 'Graph' object has no aplant_network.pyttribute 'edges_iter'
follow https://github.com/taynaud/python-louvain/issues/3 for more deatails.
