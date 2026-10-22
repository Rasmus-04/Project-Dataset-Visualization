
---

# Phase: Evaluation

## Task: Evaluate Results

### Output: Assessment of Data Mining Results

The goal of the project was to create an interactive Dash application that helps Mythic Realm Studios understand video game sales and identify popular platforms, genres, publishers, titles and regions.

The application contains 13 question pages, with visualizations designed to answer the 13 business questions. The charts allow users to compare sales between regions, explore changes over time, identify popular genres and platforms, and analyse publisher performance. Interactive controls also allow users to select different regions, genres, years and sales measures.

The application therefore covers the main business objectives of the project. However, the results have some limitations because the original datasets contain many missing values, especially in the sales fields. This means that some comparisons may be incomplete and the results may not represent the entire video game industry. 

Overall, we consider that the project meets its main objectives because the application provides visualizations for all 13 business questions. However, the results should be interpreted with caution because of the limitations in the available data.

### Output: Approved Visualizations and App Functionality

After assessing the Dash application and its visualizations with respect to the business success criteria, either approve or disapprove the Dash application and its visualizations, given your (the project group's) own judgement.

I approve the overall design and choice of visualizations in the Dash application. The application uses different chart types depending on the question, including bar charts, line charts, heatmaps and scatter plots. These visualizations are suitable for comparing sales, identifying patterns and exploring changes over time.

The interactive controls make it possible to explore the data in more detail instead of only viewing fixed charts. The application is also divided into separate pages, which makes it easier to navigate between the 13 project questions.

I approve the application and its visualizations for the purposes of this project, with the limitation that the results depend on the quality and completeness of the available data.

## Task: Review Process

### Output: Review of Process

Here you need to perform a more thorough review of
the *data mining* engagement in order to determine if there is any important factor or task that has somehow been overlooked, e.g.:
- Did we select and pre-process the datasets appropriately?
- Did we select appropriate visualizations given the underlying data?
- Did we correctly build the Dash application?
- etc.

Summarize the process review and highlight activities that have been missed and those that should really be repeated.

During the project, i followed the main steps of the CRISP-DM process, adapted to the requirements of the assignment. i defined the business objectives, explored the available datasets, prepared the data, and developed visualizations in a Dash application.

The data preparation process included cleaning text fields, converting data types, extracting release years and creating summary datasets for the 13 project questions. In total, 18 prepared datasets were created and saved as Pickle files for use in the application.

The selected visualization techniques are appropriate for most of the questions. Bar charts support comparisons between categories, line charts show changes over time, heatmaps show differences between groups, and scatter plots help compare publisher performance. Interactive controls also make the application more useful for exploring the data.

However, the review identified some limitations that should be considered:

Missing data: The original dataset contains many missing sales values and release dates. These missing values can affect the completeness and reliability of the results. The handling of missing values should be reviewed for each question to ensure that the calculations are appropriate.

Additional datasets: The supplementary datasets contain information about developers, publishers and geographical locations, but they are not directly combined with the main dataset in the current data preparation process.

Interpretation of results: Chart titles, axes, units and labels should be clear. The limitations caused by missing data should also be considered when interpreting the results.


Overall, the process produced an application that addresses the project's main questions. Further improvements to data quality handling would increase accuracy in the results before the application is used for business decisions.

## Task: Determine Next Steps

### Output: List of Possible Actions

Depending on the results of the assessment and the process review, the project team decides how to proceed.

Here we would normally list potential further actions, and rationale (reasons for and against each option), but we will skip this step in this project.

### Output: Decisions

Here we would normally describe the decision as to how to proceed, along with the rationale (e.g. if we need to perform an additional iteration, or proceed to deployment), but we will skip this step in this project, and decide to go ahead with the deployment phase.