import base64
from io import BytesIO
import io 

from flask import Flask, render_template

import matplotlib.pyplot as plt

import requests
import pandas as pd
import random

from fetchAPI import fetchData # Custom Function



app = Flask(__name__)

# Initialise the value
name="John Doe"
date="DD/MM/YY"

@app.route("/")
def main():
    lst = ['/basic', '/multi', '/fetch', '/bar', '/live']
    text = "<br>".join(lst)
    return text

@app.route("/basic")
def basic():
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
    return display(fig)

@app.route("/multi")
def multi():
    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(10,5))
    random.seed(1)

    # Create Data
    x = list(range(10))
    y1 = [random.randint(1, 10) for i in range(10)]
    y2 = [random.randint(1, 10) for i in range(10)]

    ax = fig.subplots()

    # Set Labels, Title
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Random sample")

    # Display plot
    ax.plot(x,y1, label="y1")
    ax.plot(x,y2, label="y2")

    # Set Legend
    ax.legend(loc="upper right")

    return display(fig)

@app.route("/fetch")
def fetch():

    # Load Data
    df = pd.read_csv('datasets/local.csv').to_dict()

    # Create Figure Object
    fig = Figure()
    ax = fig.subplots()

    # Add Label
    ax.set(xlabel='Date', ylabel='Average Temperature', title="New York")

    # Plot
    ax.plot(list(df['DATE'].values()),list(df['TAVG'].values()))
    
    
    # RETURN
    return display(fig)

@app.route("/scatter")
def scatter():

    # Load Data
    df = pd.read_csv('datasets/local.csv').to_dict()

    # Create Figure Object
    fig = Figure()
    ax = fig.subplots()

    # Add Label, Title
    ax.set(xlabel='Date', ylabel='Average Temperature', title="New York")

    # Plot
    ax.scatter(list(df['DATE'].values()),list(df['TAVG'].values()))
    
    
    # RETURN
    return display(fig)

@app.route("/bar")
def bar():

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
    return display(fig)

@app.route("/live")
def live():

    # Load Live Data
    url = 'http://raw.githubusercontent.com/benchan911/public/main/local.csv'
    res = requests.get(url)
    df = pd.read_csv(io.BytesIO(res.content)).to_dict() # Required 

    # Create Figure Object
    fig = Figure()
    ax = fig.subplots()

    # PLOT
    ax.scatter(list(df['DATE'].values()),list(df['TAVG'].values()), s=2)

    # Add Label, Title
    ax.set(xlabel='Date', ylabel='Average Temperature', title="New York")

    # RETURN
    return display(fig)
    
@app.route("/demo")
def demo():

    df = fetchData()

    # Create Figure Object
    fig = Figure()
    ax = fig.subplots()

    # Set 
    ax.set_xlabel('DateTime') 
    ax.set_ylabel('$')
    ax.set_title('yh-finance.p.rapidapi.com/stock/v2/get-chart')

    # PLOT
    ax.plot(df.timestamp, df.close, label='close')
    ax.plot(df.timestamp, df.high, label='high')
    ax.plot(df.timestamp, df.low, label='low')

    # Show legend
    ax.legend()

    # RETURN
    return display(fig)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)