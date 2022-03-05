from config_space import is_valid, map_img
import heapq as hq
import copy
import cv2
import numpy as np

def take_inputs():
    global start, goal
    start = input('Enter the start node as x-coordinate,y-coordinate. Eg: 0,0\n')
    goal = input('Enter the goal node as x-coordinate,y-coordinate. Eg: 394,244\n')
    start = [int(i) for i in start.split(',')]
    goal = [int(i) for i in goal.split(',')]
take_inputs()
while (not is_valid(start) or not is_valid(goal)):
    print('Entered start or goal coordinates are not in the navigable space. Please retry.')
    take_inputs()

debug = False

nodes = {} # maintains track of all generated nodes
#key:tuple having x&y coordinates of a node, value:dictionary containing info about a node
nodes[(start[0], start[1])] = {'parentX': -1, 'parentY': -1, 'cost': 0}
reached_goal = False

open_q = []#(cost, (x-coordinate, y-coordinate)) ##maintains track of all generated bu not expanded nodes
closed_q = []#maintains track of all expanded nodes
hq.heappush(open_q, (0, (start[0], start[1]))) 
hq.heapify(open_q)

def generate_children(parent):
    (parent_x, parent_y) = parent
    if debug:
        print('Expanding Node:', parent_x, parent_y, '\nChildren:')
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i==0 and j==0):
                continue
            child_x = parent_x+i
            child_y = parent_y+j
            if is_valid(child_x, child_y) == False:
                continue
            additional_cost = 1 if (i==0 or j==0) else 1.4
            child_cost = nodes[(parent_x, parent_y)]['cost'] + additional_cost
            if (child_x, child_y) in nodes:#if the child node already exists
                if child_cost < nodes[(child_x, child_y)]['cost']:# & a better path is found, update the parent & cost
                    nodes[(child_x, child_y)]['parentX'] = parent_x
                    nodes[(child_x, child_y)]['parentY'] = parent_y
                    nodes[(child_x, child_y)]['cost']    = child_cost
                    for idx in range(len(open_q)):
                        if open_q[idx][1] == (child_x, child_y):
                            open_q[idx] = (child_cost, (child_x, child_y))
                            hq.heapify(open_q)
                    if debug:
                        print(child_x, child_y, child_cost)
            else:#if the child node doesn't exist previously, insert it to `nodes`
                nodes[(child_x, child_y)] = {'parentX':parent_x, 'parentY':parent_y, 'cost':child_cost}
                hq.heappush(open_q, (child_cost, (child_x, child_y)))
                hq.heapify(open_q)
                if debug:
                    print(child_x, child_y, child_cost)


def backtrack(goal_node_x, goal_node_y):
    path = []
    curr_node = (goal_node_x, goal_node_y)
    while (nodes[curr_node]['parentX'] != -1 or nodes[curr_node]['parentY'] != -1):
        path.append(curr_node)
        curr_node = (nodes[curr_node]['parentX'], nodes[curr_node]['parentY'])
    path.append(curr_node)
    return path

def visualize():
    img = copy.copy(map_img)
    flipped_img = np.flip(img, 0)
    for node in closed_q:
        flipped_img[249-node[1], node[0]] = [255, 255, 0]
        cv2.imshow('frame', flipped_img)
        cv2.waitKey(1)
    for path_node in path[::-1]:
        flipped_img[249-path_node[1], path_node[0]] = [255, 0, 255]
        cv2.imshow('frame', flipped_img)
        if path_node == path[0]:
            cv2.imwrite('solution.jpg', flipped_img)
            cv2.waitKey(0)
        else:
            cv2.waitKey(10)

while (not reached_goal) and (len(open_q) != 0):
    _, curr_node = hq.heappop(open_q)
    closed_q.append(curr_node)
    if curr_node == (goal[0], goal[1]):
        path = backtrack(goal[0], goal[1])
        reached_goal = True
        print('\n\nGenerated Path:', path[::-1])
        break
    else:
        generate_children(curr_node)

    if debug:
        print('******* Processed', curr_node, '*******')
        print('nodes\n', nodes)
        print('open_q\n', open_q)
        print('closed_q\n', closed_q)
        print('*********************************************************************************************************')


if reached_goal:
    visualize()
else:
    print('************************************************ No solution found ************************************************')