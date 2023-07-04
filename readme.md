# Goodreads Data Charts

A simple Python script that creates several data charts based on a personal Goodreads library export.

To run:
* Install listed requirements
* Replace the csv.template file with a csv export from Goodreads (the template includes the current expected columns from the export). To generate this export:
  * In Goodreads, go to "My Books"
  * Under Tools, select "Import and export"
  * Click the "Export library" button
  * Follow the generated link to your export
* Run the `process_data.py` file

Several charts are created to supplement Goodreads' reading stats. Note that library data is expected to include at least some books with a read date.

**Pages over time**

A scatter plot displaying number of pages read over time so that those achievements of 1,000-page fantasy epics don't get averaged out with potato chip novellas.

**Total books read by month**

A line chart showing which months you've done the most vs. least reading. Combines data across years.

**Top-read publishers**

Collects the top publishers or imprints you've read most in a bar chart.
