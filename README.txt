Description:
A 400x250 sized map is used. Bottom left pixel is (1,1). A clearance of 5 is used around the boundary & obstacles. The clearance is added to the original obstacle & the original_obstacle+clearance is represented as the obstacle in the map. Black region represents un-navigable space & the white region represents navigable space.

After running the find_path.py file, the nodes being explored are represented with cyan & the final path generated is marked with magenta color.

Libraries used:
opencv==4.2.0
numpy==1.17.4
python==3.8.10 

Instructions to run:
1) clone the repo using: `git clone https://github.com/sparsh-b/Dijkstra_Algorithm.git`
2) change directory using `cd Dijkstra_Algorithm/`
3) Run the repo using `python3 find_path.py`
   - Upon receiving the prompt to enter the start & goal nodes, enter the pixel coordinates of the desired nodes.
   - For a node, enter its x-coordinate followed by the y-coordinate (comma-separated & no spaces). Eg: '6,6'
   - The most-extreme bottom-left node that can be selected is 6,6 because a clearance of 5 is used.
   - The most-extreme top-right node that can be selected is 394,244 because a clearance of 5 is used.
