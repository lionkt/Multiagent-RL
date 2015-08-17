from simulator import pacman as pacman_simulator
from simulator import layout as simulator_layout
from simulator import textDisplay
from simulator import graphicsDisplay
from simulator import myAgents

def create_layout(layout_file):
    layout = simulator_layout.getLayout(layout_file)

    if layout == None:
        raise Exception("The layout " + layout_file + " cannot be found")

    return layout

def create_pacman():
    return myAgents.RandomPacmanAgent()

def create_ghosts(num_ghosts):
    return [myAgents.RandomGhostAgent(i+1) for i in range(num_ghosts)]

def create_display(text_only=False, zoom=1.0, frameTime=0.1):
    if text_only:
        display = textDisplay.PacmanGraphics()
    else:
        display = graphicsDisplay.PacmanGraphics(zoom, frameTime=frameTime)

    return display

if __name__ == '__main__':
    layout_file = 'mediumClassic'
    num_ghosts = 4
    num_games = 1
    record = False

    layout = create_layout(layout_file)
    pacman = create_pacman()
    ghosts = create_ghosts(num_ghosts)
    display = create_display(text_only=False)

    pacman_simulator.runGames(layout, pacman, ghosts, display, num_games, record)