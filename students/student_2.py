from modules.show import display
from modules.fetchCSV import downloadCSV as getCSV

# Initialise the value
name="ACE"
date="DD/MM/YY"

def functions():

    d = {
        '/student2': student2_main,
        '/student2/basic': student2_basic,
        '/student2/fetchCSV': student2_fetchCSV
    }

    return d 

def student2_main(): # UNIQUE NAME 
    return f'Done by: {name}'

def student2_basic():
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

def student2_fetchCSV():
    import random
    from matplotlib.figure import Figure
    # Generate the figure **without using pyplot**.
    df = getCSV('https://data.gov.sg/dataset/online-shoppers')
    # df = getCSV('https://data.gov.sg/dataset/climate-change-and-energy-carbon-dioxide-emissions-from-combustion-of-fossil-fuels')

    fig = Figure(figsize=(10,5))
    ax = fig.subplots()

    # Attributes
    ax.set_xlabel("year")
    ax.set_ylabel("percentage")
    # ax.set_title("Global Temperature")

    l = list(df.columns)
    # Display plot
    ax.plot(df[l[0]], df[l[1]])
    return display(fig, name, date)