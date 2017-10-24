from bokeh.plotting import figure, show, output_notebook

def probability(n):
    # initial probabilities
    p = [0, 0, 0, 0, 0, 1]

    # next field is conditioned on previous six fields
    for _ in range(n):
        p.append(sum(p[-6:]) / 6)

    return p[6:]

fields = probability(24)
output_notebook()

plot = figure(y_range=(0, .5))
plot.scatter(x=range(1, 25), y=fields)
show(plot)
