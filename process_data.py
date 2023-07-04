import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# save a plotted chart to a file and show the result
def save_and_show(chart, name):
    fig = chart.get_figure()
    fig.savefig(f'charts/{name}.png')
    plt.show()

books = pd.read_csv('goodreads_library_export.csv', index_col=False)

# convert dates to datetime objects rather than strings
books['Date Read'] = pd.to_datetime(books['Date Read'])
books['Month Read'] = books['Date Read'].dt.month
books['Date Added'] = pd.to_datetime(books['Date Added'])

# reorganize to remove some columns we won't use
books.drop(columns=['Binding', 'My Review', 'Spoiler', 'Private Notes'], inplace=True)

# drop books if we don't know when they were read
books.dropna(subset=['Date Read'], inplace=True)

# build a scatter plot to show pages read over time
pages_over_time = books.plot.scatter(x='Date Read', y='Number of Pages')
save_and_show(pages_over_time, 'pages_over_time')

# chart overall busiest months for reading
books_by_month = books.groupby('Month Read')
total_books = books_by_month['Read Count'].aggregate(np.sum).plot()
save_and_show(total_books, 'books_by_month')

# build a bar chart to show personal most-read publishers
books_by_pub = books.groupby('Publisher')
top_publishers = books_by_pub['Read Count'].aggregate(np.sum).nlargest(8)
bar_graph = top_publishers.plot.bar()
save_and_show(bar_graph, 'top_read_publishers')
