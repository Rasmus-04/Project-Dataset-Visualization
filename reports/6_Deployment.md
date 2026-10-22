
---

# Phase: Deployment

This CRISP-DM phase has been modified somewhat to better align with the currect project.

## Task: Produce Final Report

### Output: Final Report

The purpose of this project was to develop an interactive Dash application for Mythic Realm Studios. The goal was to help the companys leadership understand video game sales and identify popular platforms, genres, publishers, titles and regions.

#### Business Understanding

The project started by identifying the business objectives and defining 13 questions about video game sales. These questions cover regional preferences, platform popularity, genre trends, publisher performance, best-selling titles and differences between regional markets.

The main objective was to create an application that allows users to explore the data and use the visualizations to answer these questions.

#### Data Understanding

The project uses five CSV datasets containing information about video games, developers, publishers, cities and countries. The main dataset, vg_charts.csv, contains 64,016 records and 14 columns.

The data includes game titles, platforms, genres, publishers, release dates and sales in different regions. Initial exploration showed differences in recorded sales between platforms, genres and regions. However, the data contains many missing values, especially in the sales columns, which limits the reliability and completeness of the results.

#### Data Preparation

The datasets were cleaned and prepared using Pandas. Text fields were cleaned, data types were converted, and a release_year column was created from the release dates. Additional calculations were made to support the project questions, including sales totals, percentages and publisher statistics.

The preparation process produced 18 datasets: five cleaned datasets and 13 question-specific datasets. These datasets were saved as Pickle files in data/preparedData so the Dash application could load the prepared data directly.

The supplementary datasets were cleaned separately and were not directly merged with the main game dataset.

#### Visualization and App Development

The application was developed using Python, Dash, Plotly Express and Dash Bootstrap Components. It contains a home page and 13 question pages, with each question page focusing on a specific business question.

Different visualization techniques were selected depending on the type of information being presented. Bar charts are used to compare sales, line charts show changes over time, heatmaps display differences between groups, and scatter plots compare publisher performance and sales consistency.

Interactive controls, such as dropdowns, sliders and radio buttons, allow users to change filters and select different measures. Dash callbacks update the visualizations when users change these controls.

#### Evaluation

The application provides visualizations for all 13 project questions and supports interactive exploration of the available data. The selected chart types are suitable for the comparisons and trends investigated in the project.

However, the missing values in the original datasets limit the reliability of some results. The application is considered suitable for the purposes of the project, but its results should be interpreted with caution. The pages, charts and interactive controls should also be tested before the application is used for business decisions.

#### Final Conclusion

Overall, the project has produced an interactive application that addresses the main business objectives. It allows users to investigate video game sales from different perspectives and explore patterns in platforms, genres, publishers, titles and regions.

The main limitation is the quality and completeness of the available data. Despite this limitation, the application provides a useful starting point for exploring video game sales. Further improvements to data quality and application testing could make the results more reliable.

## Task: Produce Final Presentation

### Output: Final Presentation

Here you need to create a final presentation for the seminar, where you will present your project. See the details in the notebook `presentation.ipynb` in the `presentation` folder.

### Output: App Demo

You also need to prepare a demonstration (demo) of your Dash application as part of your final presentation. See the details in the notebook `presentation.ipynb` in the `presentation` folder.

## Task: Review Project

### Output: Experience Documentation

Here you need to assess what went right and what went wrong, what was done well and what needs to be improved.
- Summarize important experience gained during the
project, e.g. pitfalls, misleading approaches, or hints for selecting the best suited datasets, pre-processing techniques, visualizations, and Dash application design.
- Also include a summary of things that have worked well in the CRISP-DM process, and things that haven't worked optimally (including suggestions of improvements if a future second iteration was conducted).



During this project, i gained experience in the main steps of the CRISP-DM process, from understanding the business objectives to preparing data, developing visualizations and evaluating the results.

One lesson was that data quality has a big impact on the analysis. The original datasets contained many missing sales values and release dates. This made it important to handle missing values carefully and avoid assuming that a missing sales value means zero sales. In a future project, i would spend more time investigating missing data and evaluating how it affects each question.

Another lesson was the importance of preparing the data before creating the visualizations. Creating separate summary datasets for the 13 questions made it easier for the application to load the relevant information and create the charts. Saving these datasets as Pickle files also meant that the cleaning and aggregation steps did not need to be repeated every time the application started.

The choice of visualization was also important. Different chart types were useful for different purposes. Bar charts made it easier to compare categories, line charts showed changes over time, heatmaps revealed differences between groups, and scatter plots helped compare publisher performance. Interactive controls made the application more useful because users could explore the data instead of only viewing fixed results.

Using separate pages for the 13 questions helped organize the application. The navigation bar made it possible to move between questions, while Dash callbacks allowed the charts to respond to user input.

#### What Worked Well

- Clear business objectives: The 13 questions gave the project a clear direction and helped determine which data and visualizations were needed.

- Separate preparation datasets: Creating question-specific datasets made it easier to organize the calculations and build the charts.

- Different visualization techniques: Using several chart types helped present different aspects of video game sales.

- Interactive application: Dropdowns, sliders and radio buttons allowed users to explore different parts of the data.

- CRISP-DM structure: Dividing the work into phases helped organize the project and document the decisions made during development.

#### What Could Be Improved

- Data quality: More time could have been spent investigating missing values and their effects on the results. In a future iteration, i would consider trying to restore some missing values.

- Data integration: The supplementary datasets were not directly merged with the main game dataset. Combining these datasets could allow additional analyses of developer and publisher locations.

- Documentation: The documentation could be improved by recording important data preparation decisions and explaining how each calculation supports its corresponding business question.

- Validation of results: I could compare selected calculations against the original data or independent calculations to increase confidence that the charts show the expected results.

#### Conclusion

The project provided practical experience in data preparation, visualization and interactive application development using Python and Dash. The CRISP-DM process helped us organize the work, while the 13 business questions guided the analysis and application design.

The main experience gained was that creating useful visualizations requires more than choosing the right chart type. The underlying data must also be prepared, the calculations must be appropriate for the question, and the application must be tested.

If i conducted a second iteration, i would focus on improving data quality, integrating the supplementary datasets where useful, validating the calculations and testing the application more systematically. These improvements would increase confidence in the results and make the application more useful for business decisions.