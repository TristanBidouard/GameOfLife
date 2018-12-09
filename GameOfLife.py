import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

ON 	= 1
OFF = 0
GRIDX = 100
GRIDY = 100


def CreateGrid(x, y):
	grid = np.zeros((x+1, y+1), dtype=int)
	grid[4][2] = ON
	grid[3][3] = ON
	grid[4][3] = ON
	grid[5][3] = ON

	grid[40][20] = ON
	grid[40][21] = ON
	grid[40][22] = ON
	grid[41][20] = ON
	grid[39][21] = ON

	return grid


def PlotGrid(grid):
	plt.imshow(grid, interpolation='none')
	plt.gca().invert_yaxis()
	plt.gca().get_yaxis().set_visible(False)
	plt.gca().get_xaxis().set_visible(False)
	plt.gray()
	plt.pause(0.001)

def Update(grid):

	nextGrid = grid.copy()
	for i in range(1,GRIDX):
		for j in range(1, GRIDY):

			neighON = 	grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] + \
						grid[i-1][j]   +      0       + grid[i+1][j]   + \
						grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] 
			
			if grid[i, j]  == ON: 
				if (neighON < 2) or (neighON > 3): 
					nextGrid[i, j] = OFF
			else:
				if (neighON == 3):
					nextGrid[i, j] = ON

	return nextGrid

def main():
	grid = CreateGrid(GRIDX+1, GRIDY+1)
	plt.show()
	PlotGrid(grid)

	counter = 0
	end = False

	while(counter<500 and (Update(grid)==grid).all() == False):
		grid = Update(grid)
		PlotGrid(grid)
		counter = counter + 1

if __name__ == '__main__': 
    main()