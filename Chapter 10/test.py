#AI for Snake using Deep Q-Learning and Convolutional Neural Networks: Testing AI

from environment import Environment
from brain import Brain
import numpy as np

nLastStates = 4
filepathToOpen = 'model.h5'
maxIterations = 40000
slowdown = 75

env = Environment(slowdown)
brain = Brain((env.nRows, env.nColumns, nLastStates))
model = brain.loadModel(filepathToOpen)

def resetStates():
    currentState = np.zeros((1, env.nRows, env.nColumns, 1))
    
    for i in range(nLastStates):
        state = np.reshape(env.screenMap, (1, env.nRows, env.nColumns, 1))
        currentState = np.append(currentState, state, axis = 3)
    
    currentState = np.delete(currentState, 0, axis = 3)
    
    return currentState, currentState

while True:
    env.reset()
    currentState, nextState = resetStates()
    gameOver = False
    iteration = 0
    while iteration < maxIterations and not gameOver: 
        iteration += 1
        
        qvalues = model.predict(currentState)[0]
        action = np.argmax(qvalues)
        
        state, _, gameOver = env.step(action)

        state = np.reshape(state, (1, env.nRows, env.nColumns, 1))
        nextState = np.append(nextState, state, axis = 3)
        nextState = np.delete(nextState, 0, axis = 3)
        
        currentState = nextState
