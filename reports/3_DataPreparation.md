
---

# Phase: Data Preparation

## Task: Select Data

### Output: Rationale for Inclusion/Exclusion

We include all five datasets because they contain information needed for the project. The main dataset, `vg_charts.csv`, contains game titles, platforms, genres, publishers, release dates and sales. The other datasets contain information about developers, publishers, cities and countries.

We keep the relevant columns for the analysis and remove duplicate rows. Rows with missing values are only excluded from specific analyses when the missing information is needed. We do not remove all rows with missing values because this would result in losing too much data.

## Task: Clean Data

### Output: Data Cleaning Report

We cleaned the datasets using Pandas. Duplicate rows were removed, extra spaces were stripped from text columns, and empty strings were converted to missing values.

Date columns were converted to datetime, and sales, critic scores and geographic coordinates were converted to numeric values. Invalid values were set to missing values instead of causing errors. We also created a `release_year` column from `release_date`.

The datasets contain many missing values, especially in the game sales and critic score columns. We kept these missing values rather than filling them with estimated values. Some rows are excluded from individual analyses when important information is missing. This means the results may vary in reliability depending on the available data.

## Task: Construct Data

### Output: Derived Attributes

We created several new attributes to support the analysis. The `release_year` column was extracted from `release_date`.

We also calculated total sales, regional sales percentages, average sales per record, and publisher sales statistics. For platform and genre comparisons, we calculated genre shares and a specialization index. For regional game comparisons, we calculated sales shares and relative sales indices.



## Task: Integrate Data

### Output: Merged Data

The five original datasets are cleaned separately, and no direct joins between them are performed. This means that information about developers, publishers, cities and countries is not combined with the main game dataset.

Instead, the main dataset (`vg_charts_prepared`) is used to create summary datasets for the 13 project questions. The data is grouped by different attributes, such as platform, genre, release year, publisher and game title. Sales values are summed, and additional statistics are calculated when needed.

For example, sales are grouped by platform to identify the most popular platforms, and by release year to study how sales change over time.

## Task: Format Data

### Output: Reformatted Data

The datasets were reformatted to make them easier to use in the analysis and visualizations. Text columns were cleaned, dates and numeric values were converted to the correct data types, and a new `release_year` column was created from the release date.

Some of the summary datasets were also sorted by release year or sales, depending on the question they are intended to answer. For example, the dataset for worldwide sales per title is sorted from highest to lowest sales.

All prepared datasets are saved as Pickle files (`.pkl`) in the `data/preparedData` folder. This allows the Dash application to load the prepared data directly instead of having to repeat the cleaning and aggregation steps every time.

## Main Output

### Output: Datasets

The data preparation phase produces 18 datasets, which are saved as Pickle files in the `data/preparedData` folder.

Five datasets contain the cleaned original data:

- `vg_charts_prepared`
- `vg_developers_prepared`
- `vg_publishers_prepared`
- `vg_geo_cities_prepared`
- `vg_geo_countries_prepared`

The other 13 datasets, named `df_q1` to `df_q13`, contain prepared data for the 13 project questions. Each dataset has been grouped, summarized or calculated according to the information needed for its question.

These datasets are used by the Dash application to create the graphs and interactive visualizations.

### Output: Dataset Descriptions

The main dataset, `vg_charts_prepared`, contains information about video games, including titles, platforms, genres, publishers, developers, release dates and sales in different regions. It is the main source for answering the project's questions.

The other four prepared datasets contain information about developers, publishers, cities and countries. They provide additional information about companies and geographical locations, although they are not directly merged with the main dataset in the current preparation code.

The 13 question-specific datasets contain summarized information for the visualizations. They cover topics such as regional sales by platform and genre, sales trends over time, publisher performance, the best-selling game titles and platform specialization in different genres. Some datasets also include calculated percentages, averages and statistical measures.

Together, these datasets provide the information needed to investigate the 13 project questions in the Dash application. However, many values are missing in the original data, which can affect the completeness and reliability of the results.