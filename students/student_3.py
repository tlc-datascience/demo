from __main__ import app
from show import display
from modules.fetchAPI import fetchData as getData


# Initialise the value
name=""
date="DD/MM/YY"

@app.route('/student3')
def student3_main(): # UNIQUE NAME 
    return f'Done by: {name}'

@app.route("/student3/basic")
def student3_basic():
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


@app.route("/student3/live")
def student3_live():
    df = getData()
    from matplotlib.figure import Figure
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
    return display(fig, name, date)