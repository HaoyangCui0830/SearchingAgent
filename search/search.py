# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import PriorityQueue
from util import manhattanDistance

maxDepth = 500
infinit = 10000000
Weight = 2

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    util.raiseNotDefined()
visited_list = []
def iterativeDeepeningSearch(problem):
    """Search the deepest node in an iterative manner."""
    "*** YOUR CODE HERE FOR TASK 1 ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    ##print("Start's successors:", problem.getSuccessors((22,16)))
    ActionList = []
    ##return ['East','West', 'East','West', 'East','West', 'East']
    for limit in range(maxDepth):
        stack = Stack()
        #visited_list = Stack()
        visited_list.clear()
        #print(limit)
        if deepthLimitSearch(stack,problem, problem.getStartState(), limit ) == True:
            while stack.isEmpty() == False:
                ActionList.append(stack.pop())
            ActionList.reverse()
            #print(ActionList)
            return ActionList
    ##util.raiseNotDefined()
""" should add visited list """
def deepthLimitSearch(stack, problem, state, limit):
    if state in visited_list and visited_list is not None:
        return False
    else:
        #visited_list.push(state)
        visited_list.append(state)
    if problem.isGoalState(state):
        return True
    if limit <= 0 :
        return False
    for i in problem.getSuccessors(state):
        stack.push(i[1])
        if deepthLimitSearch(stack, problem, i[0], limit-1 )==True:
            return True
        else:
            stack.pop()
    #visited_list.pop()
    visited_list.pop()
    return False

class NodeState:
    def __init__(self, node_state, parent_state, parent_g, cost, action):
        self.state = node_state
        self.father = parent_state
        self.g = parent_g + cost
        self.cost = cost
        self.action = action

def Get_g(NodeStateList, node_state):
    for i in range(len(NodeStateList)):
        if NodeStateList[i].state == node_state:
            return NodeStateList[i].g

def Get_Parent(NodeStateList, node_state):
    for i in range(len(NodeStateList)):
        if NodeStateList[i].state == node_state:
            return NodeStateList[i].father

def Get_Action(NodeStateList, node_state, node_father):
    for i in range(len(NodeStateList)):
        if NodeStateList[i].state == node_state and NodeStateList[i].father == node_father:
            return NodeStateList[i].action

def ReverseAction(action):
    if action == "West": return "East"
    if action == "East": return "West"
    if action == "North": return "South"
    if action == "South": return "North"

def getLocalSuccessors(NodeStateList, node_father):
    son_list = []
    for i in range(len(NodeStateList)):
        if NodeStateList[i].father == node_father:
            son_list.append((NodeStateList[i].state, NodeStateList[i].action, NodeStateList[i].cost))
    return son_list

def waStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has has the weighted (x 2) lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 2 ***"
    TotalActions = []
    solved = False
    asked_nodes = []
    recorded_nodes = []
    #while problem.goal is not None:
    while True:
        ActionList = []
        open = PriorityQueue()
        node = None
        nodes = []
        nodes.append( NodeState(problem.getStartState(), None, 0, 0, None) )
        open.push(problem.getStartState(), 0 + Weight * heuristic(problem.getStartState(), problem) )
        closed = []
        best_g = {problem.getStartState():0}
        while open.isEmpty() == False:
            node = open.pop()
            if node not in closed or Get_g(nodes, node) < best_g.get(node):
                closed.append(node)
                best_g[node] = Get_g(nodes, node)
                if problem.isGoalState(node):
                    #print("reached one goal")
                    break
                if node in asked_nodes:
                    for sub_node in getLocalSuccessors(recorded_nodes,node):
                        #print(sub_node)
                        nodes.append( NodeState(sub_node[0], node, Get_g(nodes, node), sub_node[2], sub_node[1]) )
                        if heuristic(sub_node[0],problem) < infinit:
                            open.push(sub_node[0], Get_g(nodes, sub_node[0]) + Weight * heuristic(sub_node[0],problem) )
                else:
                    for sub_node in problem.getSuccessors(node):
                        #print(sub_node)
                        asked_nodes.append(node)
                        recorded_nodes.append( NodeState(sub_node[0], node, Get_g(nodes, node), sub_node[2], sub_node[1]) )
                        nodes.append( NodeState(sub_node[0], node, Get_g(nodes, node), sub_node[2], sub_node[1]) )
                        if heuristic(sub_node[0],problem) < infinit:
                            open.push(sub_node[0], Get_g(nodes, sub_node[0]) + Weight * heuristic(sub_node[0],problem) )
        #if problem.goal == node:
        #print(problem.isGoalState(node))
        if hasattr(problem, 'goal'):
            if problem.goal == node:
                solved = True
        else:
            if problem.isGoalState(node):
                solved = True
        while Get_Parent(nodes, node) is not None:
            parent_node = Get_Parent(nodes, node)
            ActionList.append(Get_Action(nodes, node, parent_node))
            node = parent_node
        ActionList.reverse()
        TotalActions.extend(ActionList)
        if solved:
            break


    # if ( str(type(problem))=='<class \'searchAgents.CapsuleSearchProblem\'>'  ):
    #     problem.heuristicInfo['hasCapsule'] = True
    #     start_node = problem.goal
    #     while problem.allFoodEat() == False:
    #         goal = problem.getNextGoalPoint(start_node)
    #         #print(goal)
    #         ExtraActionList = []
    #         open = PriorityQueue()
    #         node = None
    #         nodes = []
    #         nodes.append( NodeState(start_node , None, 0, 0, None) )
    #         open.push(start_node, 0 + Weight * heuristic(problem.getStartState(), problem) )
    #         closed = []
    #         best_g = {start_node:0}
    #         while open.isEmpty() == False:
    #             node = open.pop()
    #             if node not in closed or Get_g(nodes, node) < best_g.get(node):
    #                 closed.append(node)
    #                 best_g[node] = Get_g(nodes, node)
    #                 if node == goal :
    #                     start_node = node
    #                     break
    #                 for sub_node in problem.getSuccessors(node):
    #                     if sub_node[0] in problem.food.asList() and sub_node[0]!=goal :
    #                         nodes.append( NodeState(sub_node[0], node, Get_g(nodes, node), -9, sub_node[1]) )
    #                     else:
    #                         nodes.append( NodeState(sub_node[0], node, Get_g(nodes, node), -1, sub_node[1]) )
    #                     if heuristic(sub_node[0],problem) < infinit:
    #                         open.push(sub_node[0], Get_g(nodes, sub_node[0]) + Weight * heuristic(sub_node[0],problem) )
    #         if node in problem.food.asList():
    #             problem.food[node[0]][node[1]] = False
    #         while Get_Parent(nodes, node) is not None:
    #             parent_node = Get_Parent(nodes, node)
    #             ExtraActionList.append(Get_Action(nodes, node, parent_node))
    #             node = parent_node
    #         ExtraActionList.reverse()
    #         ActionList.extend(ExtraActionList)
    # return ActionList
    #print(TotalActions)
    return TotalActions
    #return ActionList
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
wastar = waStarSearch
