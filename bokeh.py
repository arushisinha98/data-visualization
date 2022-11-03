# annotation = titles, legends, labels, bands
# application = recipe for generating Bokeh documents; python code run by Bokeh server every session
# BokehJS = javascript client library that renders visuals and handles UI interactions for Bokeh plots and widgets in browder
# document = organizing data structure for Bokeh applications; contain all models and data needed to render interactive visualization
# embedding = methods to include Bokeh plots and widgets in web apps, web pages, or Jupyter notebooks
# glyph = API objects that draw vectorized graphics to represent data (building blocks of Bokeh plots)
# layout = collection of Bokeh objects
# model = lowest-level objects that Bokeh visualizations consist of
# plot = containers that hold various objects of a visualization
# renderer = method or function that draws elements of plot
# server = optional component to share and publish Bokeh plots and app, to handle data streaming, to enable complex UI
# widget = UI elements that are not directly part of Bokeh plot

from bokeh.plotting import figure, output_file, show
import pandas as pd

# set some figure dimensions:
width = 300
height = 300
size = 5

output_file(""" [OUTPUT_FILE_HERE].HTML """)
p = figure(width = width, height = height, tools = "pan, reset, save")
p.line = (x = [1,2,3], y = [4,6,2]) # add size, color, alpha, line width
show(p)
"""
alternative scatter plots (can be added after line plot as markers):
asterisk(), circle(), circle_cross(), circle_dot(), circle_x(), circle_y(), cross(), dash(), diamond(),
diamond_cross(), diamond_dot(), dot(), hex(), hex_dot(), inverted_triangle(), plus(), square(), square_cross(),
square_dot(), square_pin(), square_x(), star(), star_dot(), triangle(), triangle_dot(), triangle_pin(), x(), y()
"""
"""
alternative line plots:
step(), multi_line([[x1],[y1]],[[x2],[y2]]), vline_stack(), segment([x1],[y1],[x2],[y2]),
ray([x],[y],length,[angle]) # set length to 0 for infinite ray that extends to the edge of plot
arc([x],[y],radius,start_angle,end_angle) # add clock or anticlock
quadratic(), bezier()
"""
from bokeh.models import ColorBar, ColumnDataSource

data = {'x_values': [""" INSERT X DATA """],
        'y_values': [""" INSERT Y DATA """]}
source = ColumnDataSource(data = data)
p = figure()
p.circle(x = 'x_values', y = 'y_values', source = source)

new_sequence = [""" INSERT Z DATA """]
source.data['z_values'] = new_sequence

# stream() to take in new data 
# patch() updates slices of data source

"""
client-side color mapping:
linear_cmap()
log_cmap()
"""
from bokeh.transform import linear_cmap, factor_cmap, factor_mark

fill_color = linear_cmap('counts', 'Viridis256', min = 0, max = 10)


from numpy.random import standard normal
from bokeh.util.hex import hexbin

bins = hexbin(x, y, 0.1)
p = figure(tools = "", match_aspect = True, background_fill_color = '#FFFFFF')
p.grid.visible = False
p.hex_tile(q = 'q', r = 'r', size = 0.1, line_color = None, source = bins,
           fill_color = linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))
show(p)

x = list(range(1,11))
y = list(range(1,11))
source = ColumnDataSource(dict(x = x, y = y))
p = figure(width = width, height = height, title = """ INSERT TITLE """)
cmap = linear_cmap(field_name = 'y', palette = 'Spectral6', low = min(y), high = max(y))
p.scatter(x = 'x', y = 'y', color = cmap, size = size, source = source)
color_bar = ColorBar(color_mapper = cmap['transform'], width = width/30)
p.add_layout(color_bar, 'right')
show(p)


from bokeh.sampledata.penguins import data

SPECIES = sorted(data.species.unique())
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Penguin size", background_fill_color = "#fafafa")
p.xaxis.axis_label = 'Flipper Length (mm)'
p.yaxis.axis_label = 'Body Mass (g)'

p.scatter("flipper_length_mm", "body_mass_g", source = data,
          legend_group = "species", fill_alpha = 0.5, size = size,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))

p.legend.location = "top_left"
p.legend.title = "Species"

show(p)


v_func =
"""
    const first = xs[0]
    const norm = new Float64Array(xs.length)
    for (let i = 0; i < xs.length; i++) {
        norm[i] = xs[i] / first
    }
    return norm
"""
normalize = CustomJSTransform(v_func = v_func)

plot.line(x = 'aapl_date', y = transform('aapl_close', normalize), line_width = 2,
          color = '#cf3c4d', alpha = 0.5, legend = "Apple", source = aapl_source)

