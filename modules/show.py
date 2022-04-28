def display(fig, name, date):
    import base64
    from io import BytesIO
    import io 
    from flask import render_template
    
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('index.html', plot_url = data, name=name, date=date)