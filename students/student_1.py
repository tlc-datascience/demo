from __main__ import app
from show import display


# Initialise the value
name="John Doe"
date="DD/MM/YY"

@app.route('/student1')
def student1_main(): # UNIQUE NAME 
    return f'Done by: {name}'

@app.route("/student1/basic")
def student1_basic():
    import random
    from matplotlib.figure import Figure
    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(10,5))
    random.seed(1)
    x = list(range(10))
    y = [random.randint(1, 10) for i in range(10)]

    ax = fig.subplots()

    # Attributes
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Random sample")

    # Display plot
    ax.plot(x,y)
    return display(fig, name, date)

@app.route("/student1/scatter")
def student1_scatter():
    import random
    from matplotlib.figure import Figure
    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(10,5))
    random.seed(1)
    x = list(range(10))
    y = [random.randint(1, 10) for i in range(10)]

    ax = fig.subplots()

    # Attributes
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Random sample")

    # Display plot
    ax.scatter(x,y)
    return display(fig, name, date)

@app.route("/student1/bar")
def student1_bar():
    import pandas as pd
    from matplotlib.figure import Figure
    
    # Create Data
    players = [
            { "name": "player1", "hours": 15},
            { "name": "player2", "hours": 45},
            { "name": "player3", "hours": 32}
    ]

    # Create Dataframe
    df_players = pd.DataFrame(players)
    df_players

    # Create Figure Object
    fig = Figure()
    ax = fig.subplots()
    
    # Add Label, Title
    ax.set(xlabel='Players Profile', ylabel='Time Spent (hrs)', title="Gaming Addiction")

    # Plot bar graph
    ax.bar(df_players.name, df_players.hours)
    
    # RETURN
    return display(fig, name, date)
    