
---

# Phase: Data Understanding

## Task: Collect Initial Data

### Output: Initial Data Collection Report

The initial data has already been collected, and is stored in the `data` folder together with the *data dictionary* (i.e. descriptions or each column/feature in each dataset) in the `data/data_dictionary` folder.

The datasets are:
- `vg_charts.csv`
- `vg_developers.csv`
- `vg_publishers.csv`
- `vg_geo_cities.csv`
- `vg_geo_countries.csv`

## Task: Describe Data

### Output: Data Description Report

- Here you need to describe the data that has been acquired, including the format of the data, the quantity of data (for example, the number of records (rows) and fields (columns) in each dataset/table), the identities of the fields, and any other surface features which have been discovered.
- You also have to evaluate whether the data acquired satisfies the relevant requirements (or if you need to collect more data).

#### 1. Overview of the Acquired Data

The project uses five CSV datasets provided in the `data` folder. The datasets contain information about video games, their platforms, genres, sales, developers, publishers, and geographical locations. The corresponding data dictionaries are stored in `data/data_dictionary` and describe the fields in each dataset.

The main dataset is `vg_charts.csv`, which contains information about individual video game releases. The remaining datasets provide information about developers, publishers, cities, and countries.

#### 2. Dataset Structure and Contents

The following table summarizes the size and purpose of each dataset.

| Dataset | Records (rows) | Fields (columns) | Purpose |
|---|---:|---:|---|
| `vg_charts.csv` | 64,016 | 14 | Main dataset containing video game releases, sales, genres, platforms, and dates |
| `vg_developers.csv` | 731 | 3 | Developer names and their headquarters cities and countries |
| `vg_publishers.csv` | 889 | 3 | Publisher names and their headquarters cities and countries |
| `vg_geo_cities.csv` | 23,412 | 3 | City names and geographical coordinates |
| `vg_geo_countries.csv` | 262 | 5 | Country names, ISO country codes, and geographical coordinates |

The main dataset contains 39,798 distinct game titles, 81 distinct platforms, 20 genres, and 3,383 distinct publisher names. The same title can appear in multiple records because a game may be released on several platforms. Therefore, the number of records should not be interpreted as the number of unique games.

#### 3. Description of the Main Dataset

The `vg_charts.csv` dataset is the primary source for answering the projects 13 questions. (The questions can be found in `Questions.md` in the root folder)

Its 14 fields are described below.

| Field | Description | Data type |
|---|---|---|
| `img` | URL path for the game's box art on VGChartz | Text, image reference |
| `title` | Title of the video game | Categorical text |
| `platform` | Platform on which the game was released | Categorical text |
| `genre` | Genre of the game, such as Action or Shooter | Categorical text |
| `publisher` | Company that published the game | Categorical text |
| `developer` | Company or organization that developed the game | Categorical text |
| `critic_score` | Metacritic critic score on a scale from 1 to 10 | Numeric |
| `total_sales` | Global sales of copies, expressed in millions | Numeric |
| `na_sales` | Sales in North America, expressed in millions | Numeric |
| `jp_sales` | Sales in Japan, expressed in millions | Numeric |
| `pal_sales` | Sales in Europe and Africa, expressed in millions | Numeric |
| `other_sales` | Sales in the rest of the world, expressed in millions | Numeric |
| `release_date` | Date the game was released | Date |
| `last_update` | Date the record was last updated | Date |

The fields support several types of analysis. Categorical fields such as `platform`, `genre`, `publisher`, and `title` can be grouped to compare popularity and sales. Numeric fields provide measurements for calculating totals and comparing regions. The release date allows the data to be grouped by year to examine historical trends.

The regional sales fields are particularly important. They allow sales to be compared across North America, Japan, Europe and Africa, and other regions. The `total_sales` field provides a measure of worldwide sales.

#### 4. Description of the Supplementary Datasets

**`vg_developers.csv`**

This dataset contains 731 records and three fields:

- `developer`: Name of the game developer.
- `city`: City in which the developer is headquartered.
- `country`: Country in which the developer is headquartered.

The dataset can provide geographical context for game developers. It contains 731 distinct developer names, with five missing city values.

**`vg_publishers.csv`**

This dataset contains 889 records and three fields:

- `publisher`: Name of the game publisher.
- `city`: City in which the publisher is headquartered.
- `country`: Country in which the publisher is headquartered.

The dataset can be used to investigate publisher locations and compare geographical differences with publisher performance. It contains 888 distinct publisher names. There are 147 missing city values and one missing country value.

**`vg_geo_cities.csv`**

This dataset contains 23,412 records and three fields:

- `city`: Name of the city.
- `latitude`: Latitude of the city's geographical position.
- `longitude`: Longitude of the city's geographical position.

The geographical coordinates can be used to place cities on a map. City names alone may not always uniquely identify a location when several countries contain cities with the same name.

**`vg_geo_countries.csv`**

This dataset contains 262 records and five fields:

- `Country`: Country name.
- `Alpha-2 code`: Two-letter ISO country code.
- `Alpha-3 code`: Three-letter ISO country code.
- `Latitude`: Country's central latitude.
- `Longitude`: Country's central longitude.

The dataset can support geographical mapping and country identification. The country codes can also be useful when matching country information across datasets.

#### 5. Data for Answering the Project Questions

The acquired dataset contains the necessary types of information to investigate all 13 questions in `Questions.md`. However, the dataset is incomplete and contains many missing values. This means that the results may vary depending on which records and fields are available for each analysis. The findings may not fully represent the entire video game industry.

| Question(s) | Required fields | What the Data Can Tell Us |
|---|---|---|
| 1–2. Platform preferences by region and overall platform popularity | `platform`, `na_sales`, `jp_sales`, `pal_sales`, `other_sales` | Suitable for comparing platform sales across regions and identifying overall platform popularity. |
| 3. Sales per release year and region | `release_date` and regional sales fields | Suitable for examining sales trends over time in different regions by extracting the release year. |
| 4. Most popular platform per release year | `release_date`, `platform`, sales fields | Suitable for comparing platform popularity over time. |
| 5–6. Genre preferences and top three genres by region | `genre` and regional sales fields | Suitable for comparing regional genre preferences and identifying the three most popular genres in each region. |
| 7. Genre popularity over time | `genre`, `release_date`, sales fields | Suitable for examining how genre popularity changes over time. |
| 8. Consistently successful and inconsistent publishers | `publisher`, sales fields, and optionally `title` | Suitable for comparing publisher sales performance across their games and identifying differences in sales consistency. |
| 9. Region with the highest sales | Regional sales fields | Suitable for comparing total sales across regions. |
| 10. Best-selling worldwide titles | `title`, `total_sales` | Suitable for ranking titles by worldwide sales, while accounting for titles released on multiple platforms. |
| 11. Highest-selling release year and industry growth | `release_date`, `total_sales` | Suitable for comparing recorded sales across release years and examining changes in sales over time. |
| 12. Platform specialization in particular genres | `platform`, `genre`, sales fields | Suitable for comparing genre distributions and sales across platforms to identify genre preferences associated with different platforms. |
| 13. Titles that succeed in one region but perform poorly in another | `title` and regional sales fields | Suitable for identifying titles with strong sales in one region but weaker sales in another. |


## Task: Explore Data

### Output: Data Exploration Report

- Here you need to describe the results of this task, including first findings or initial hypothesis and their impact on the remainder of the project:
  - This task addresses the data mining questions (under `Phase: Business Uuderstanding -> Task: Determine Data Mining Goals`) using querying, visualization, and reporting techniques.
  - These include distribution of key attributes (e.g. sales, regions, genres, platforms, etc.) relationships between pairs of attributes, results of simple aggregations, properties of significant sub-populations (e.g. groupings of genres, platforms, etc.), and simple statistical analyses (counts, sums, means, standard deviations, etc.).
  - These analyses may directly address the data mining goals; they may also contribute to or refine the data description and quality  reports, and feed into the transformation (e.g. merging, feature engineering) and other data preparation steps (e.g. cleaning) needed for further analysis.
- If appropriate, include graphs and plots to indicate data characteristics that suggest further examination of interesting data subsets.

#### 1. Overview

The purpose of this task is to explore the data and find patterns that can help answer the 13 questions in `Questions.md`. The main focus is on sales, platforms, genres, regions, publishers and release years.

#### 2. Initial Findings

**Platforms**

The platform with the highest recorded worldwide sales is PS2, with approximately 1,028 million copies sold. It is followed by X360 and PS3.

This can help answer which platforms have been the most popular. However, some sales values are missing, so the results may not show the complete sales for each platform.

**Genres**

The genres with the highest recorded worldwide sales are Sports, Action and Shooter. This suggests that these genres are important when comparing game popularity.

Further analysis is needed to see if the same genres are popular in every region.

**Regional sales**

North America has the highest recorded sales, with approximately 3,346 million copies. Europe and Africa have around 1,917 million, followed by Japan and other regions.

This can help answer which region purchases the most video games. Missing sales values could affect the results.

**Sales over time**

The year with the highest recorded worldwide sales is 2008, with approximately 538 million copies sold.

This gives us a starting point for investigating how sales have changed over time. However, missing sales values and release dates make it difficult to determine whether the entire industry has grown.

**Sales distribution**

The average worldwide sales per record is approximately 0.35 million copies, while the median is 0.12 million. This means that most games have relatively low sales, while a smaller number of games sell much more.

#### 3. Relationships Between Attributes

The data can be grouped in different ways to answer the project questions:

- **Platform and region:** Compare which platforms sell the most in each region.
- **Genre and region:** Find the most popular genres and the top three genres in each region.
- **Genre and release year:** Investigate how genre popularity changes over time.
- **Publisher and sales:** Compare publisher performance and identify publishers with more consistent sales.
- **Title and region:** Find games that sell well in one region but poorly in another.

These comparisons can be shown using bar charts, line charts and heatmaps in the Dash application.

#### 4. Conclusion

The initial exploration shows differences in sales between platforms, genres and regions. PS2 has the highest recorded platform sales, Sports has the highest recorded genre sales, North America has the highest regional sales, and 2008 has the highest recorded annual sales.

The results give us a good starting point for creating the visualizations. However, the missing data needs to be considered before drawing final conclusions.

## Task: Verify Data Quality

### Output: Data Quality Report

Here you need to list the results of the data quality verification, i.e. if quality problems exist, possible solutions to data quality issues, etc.

This includes examining the quality of the data, addressing questions
such as:
- Is the data complete (i.e. does it cover all the cases required, or will you need to collect more data)?
- Is it correct, or does it contain errors and, if there are errors, how common are they?
- Are there missing values in the data? If so, how are they represented, where do they occur, and how common are they?


#### 1. Missing Values

The main dataset, `vg_charts.csv`, contains 64,016 records. Several important fields have missing values.

| Field | Missing values | Percentage |
|---|---:|---:|
| `critic_score` | 57,338 | 89.57% |
| `total_sales` | 45,094 | 70.44% |
| `na_sales` | 51,379 | 80.26% |
| `jp_sales` | 57,290 | 89.49% |
| `pal_sales` | 51,192 | 79.97% |
| `other_sales` | 48,888 | 76.37% |
| `release_date` | 7,051 | 11.01% |
| `last_update` | 46,137 | 72.07% |

The biggest problem is the missing sales data. This affects most of the questions because many of them depend on comparing sales between platforms, genres, regions and years.

The supplementary datasets also contain missing values. `vg_developers.csv` has five missing city values, while `vg_publishers.csv` has 147 missing city values and one missing country value.

**Solution:** Missing values should not automatically be replaced with zero, since a missing sales value does not necessarily mean that no copies were sold. We should use the available data and mention its limitations.

#### 2. Duplicates and Data Types

No exact duplicate rows were found in the five datasets.

However, the same game title can appear several times because games can be released on different platforms. These records should not automatically be removed.

The date fields in `vg_charts.csv` are stored as text and should be converted to datetime values before analysing sales by year. The latitude and longitude fields in `vg_geo_countries.csv` are also stored as text and need to be converted to numeric values for geographical analysis.

**Solution:** Convert the fields to the correct data types and check for inconsistent names before combining the datasets.

#### 3. Sales Values

No negative sales values were found, and the available critic scores are within the expected range of 1 to 10.

Small differences were found when comparing worldwide sales with the sum of regional sales. These differences appear consistent with rounding.


**Solution:** Keep valid zero values, investigate unusual sales figures when necessary, and allow for rounding when comparing worldwide and regional sales.

#### 4. Data Coverage

The release dates range from 1971 to 2024, but some records have no release date or sales information. This means that yearly sales comparisons may not represent the complete video game industry.

The missing city and country values in the supplementary datasets may also limit geographical analysis of developers and publishers.

**Solution:** Consider the amount of available data when creating graphs.

#### 5. Conclusion

The datasets are useful for the project, but there are some quality problems that need to be considered.

The biggest issue is the large amount of missing sales data, followed by missing critic scores and release dates. No exact duplicate rows or negative sales values were found.

Wwe should handle missing values carefully, convert fields to the correct data types and check the data when combining datasets.

The data is sufficient for exploring the 13 questions, but the results should be interpreted with these limitations in mind.