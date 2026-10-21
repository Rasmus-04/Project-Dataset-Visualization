import numpy as np
import pandas as pd

# ladda in alla dataframes
df_charts = pd.read_csv('data/vg_charts.csv')
df_developers = pd.read_csv('data/vg_developers.csv')
df_geo_cities = pd.read_csv('data/vg_geo_cities.csv')
df_geo_countries = pd.read_csv('data/vg_geo_countries.csv')
df_publishers = pd.read_csv('data/vg_publishers.csv')

# Ladda in alla data dictornarys
dd_charts = pd.read_csv('data/data_dictionary/vg_charts.csv')
dd_developers = pd.read_csv('data/data_dictionary/vg_developers.csv')
dd_geo_cities = pd.read_csv('data/data_dictionary/vg_geo_cities.csv')
dd_geo_countries = pd.read_csv('data/data_dictionary/vg_geo_countries.csv')
dd_publishers = pd.read_csv('data/data_dictionary/vg_publishers.csv')

prepaired_data_location = "data/preparedData"

REGIONAL_SALES = ["na_sales", "jp_sales", "pal_sales", "other_sales"]


# Sparar datframe i pickle format (.pkl)
def save_df(name, df, location=prepaired_data_location):
    output_path = f"{location}/{name}.pkl"
    df.to_pickle(output_path)
    print(f"Saved {output_path} ({len(df):,} rows)")



"""
Retunerar en Rengjorda dataframes
"""

# Rensar vg_charts dataset och skapar en relase_year kolumn
def clean_charts(df):
    df = df.copy()

    # Tar bort dupbletter
    df = df.drop_duplicates()

    # Tar bort alla withespaces på kolmerna som ska vara av datatypen string
    text_columns = ["img", "title", "platform", "genre", "publisher", "developer"]
    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip()
            df[column] = df[column].replace("", pd.NA)

    # Konventerar de värden som ska vara Datetime till rätt datatyp
    # Värden som inte kan omvandlas till ett datum blir NaT (Not a Time)
    for column in ["release_date", "last_update"]:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    # Omvandlar kolumnerna till numeriska värden och sätter ogiltiga värden till NaN
    numeric_columns = ["critic_score", "total_sales", "na_sales", "jp_sales", "pal_sales", "other_sales"]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # Skapar en ny kolumn med release_year från release_date kolumn
    # ex 2026-10-15 blir 2026 samt värden som inte går att konventeras blir Na
    df["release_year"] = df["release_date"].dt.year.astype("Int64")

    return df

# Rensar vg_developers dataset
def clean_developers(df):
    # Tar bort dubletter
    df = df.copy().drop_duplicates()

    # Tar bort alla withespaces på kolumerna och sätter datatypen till string samt sätter ogiltliga värden till Na
    for column in ["developer", "city", "country"]:
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip()
            df[column] = df[column].replace("", pd.NA)

    return df

# Rensar vg_publicher dataset
def clean_publishers(df):
    df = df.copy().drop_duplicates()

    # Tar bort alla withespaces på kolumerna och sätter datatypen till string samt sätter ogiltliga värden till Na
    for column in ["publisher", "city", "country"]:
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip()
            df[column] = df[column].replace("", pd.NA)

    return df

# Rensar vg_geo_cites dataset
def clean_geo_cities(df):
    df = df.copy().drop_duplicates()

    # Tar bort alla withespaces på kolumerna och sätter datatypen till string samt sätter ogiltliga värden till Na
    if "city" in df.columns:
        df["city"] = df["city"].astype("string").str.strip()
        df["city"] = df["city"].replace("", pd.NA)

    # konverterar "latitude" och "longitude" till int och de som inte kan konventeras sätts till NaN
    for column in ["latitude", "longitude"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    return df

# Rensar vg_geo_countries dataset
def clean_geo_countries(df):
    # Tar bort dubbleter
    df = df.copy().drop_duplicates()

    # Tar bort alla withespaces på kolumerna och sätter datatypen till string samt sätter ogiltliga värden till Na
    for column in ["Country", "Alpha-2 code", "Alpha-3 code"]:
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip().str.strip('"')
            df[column] = df[column].replace("", pd.NA)

    # konverterar "latitude" och "longitude" till int samt ogilitliga värden till Na
    for column in ["Latitude", "Longitude"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column].astype("string").str.strip().str.strip('"'), errors="coerce")

    return df


# Skapar dataframesen för alla frågor

# Används för fråga 1: regional sales by platform
def create_df_q1(prepared_charts):
    df = prepared_charts
    return (
        df.groupby("platform")[REGIONAL_SALES] # Grupperar raderna efter platform och väljer kolumnerna som ska summeras
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör platform till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
    )

# Används för fråga 2: most popular platform for playing video games
def create_df_q2(prepared_charts):
    df = prepared_charts
    return (
        df.groupby("platform")["total_sales"] # Grupperar raderna efter platform och väljer kolumnerna som ska summeras
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör platform till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
        .sort_values("total_sales", ascending=False) # Sorterar df på total_sales i fallande ordning (högst till lägst)
    )


# Används för fråga 3: Video game sales vary per release year in each region
def create_df_q3(prepared_charts):
    df = prepared_charts.dropna(subset=["release_year"])  # Tar bort rader där release_year saknas
    return (
        df.groupby("release_year")[REGIONAL_SALES] # Grupperar raderna efter release_year och väljer kolumnerna som ska summeras
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör release_year till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
        .sort_values("release_year") # Sorterar efter release_year i stigande ordning, från äldst till nyast
    )

# Används för fråga 4: worldwide sales per platform and release year
def create_df_q4(prepared_charts):
    df = prepared_charts.dropna(subset=["release_year", "platform"]) # Tar bort rader där release_year saknas
    return (
        df.groupby(["release_year", "platform"])["total_sales"] # Grupperar efter release_year och platform och väljer total_sales för summering
        .sum(min_count=1) # Summerar total_sales inom varje grupp om minst ett giltigt värde finns
        .reset_index() # Gör release_year och platform till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
        .sort_values(["release_year", "total_sales"], ascending=[True, False]) # Sorterar först efter release_year stigande och sedan efter total_sales fallande inom varje år
    )

# Används för fråga 5: sales by genre and region
def create_df_q5(prepared_charts):
    df = prepared_charts.dropna(subset=["genre"])
    return (
        df.groupby("genre")[REGIONAL_SALES] # Grupperar raderna efter genre samt väljer kolumnerna som ska summeras
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör genre till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
    )

# Används för fråga 6: sales by genre and region
def create_df_q6(prepared_charts):
    df = prepared_charts
    return (
        df.groupby("genre")[REGIONAL_SALES] # Grupperar raderna efter genre samt väljer kolumnerna som ska summeras
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör genre till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
    )

# Används för fråga 7: worldwide sales by genre and release year
def create_df_q7(prepared_charts):
    df = prepared_charts.dropna(subset=["release_year", "genre"]) # Tar bort rader där release_year eller genre saknas
    return (
        df.groupby(["release_year", "genre"])["total_sales"] # Grupperar efter release_year och genre och väljer total_sales för summering
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör release_year och genre till vanliga kolumner och återställer indexet
        .dropna(subset=["total_sales"])  # grupper där all försäljning saknas ska inte bli punkter
        .sort_values(["release_year", "total_sales"], ascending=[True, False]) # Sorterar först efter release_year stigande och sedan efter total_sales fallande inom varje år
    )

# Används för fråga 8: publisher sales statistics and consistency indicators
def create_df_q8(prepared_charts):
    df = prepared_charts.dropna(subset=["publisher"]) # Tar bort rader som saknar publisher
    summary = (
        df.groupby("publisher")["total_sales"] # Grupperar raderna efter publisher och väljer kolumnen total_sales för beräkningarna
        .agg( # Beräkna flera statistiska mått
            games_with_sales="count", # Räknar spel med registrerade värden i total_sales per publisher
            total_sales=lambda values: values.sum(min_count=1), # Summerar försäljningsvärdena per publisher
            mean_sales="mean", # Beräknar medelvärdet av försäljningen per spel
            median_sales="median", # Beräknar medianen av försäljningen per spel
            std_sales="std", # Beräknar standardavvikelsen, som beskriver variationen i försäljningen
            min_sales="min", # Hittar det lägsta registrerade försäljningsvärdet
            max_sales="max" # Hittar det högsta registrerade försäljningsvärdet
        )
        .reset_index() # Gör publisher till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
    )
    """
    Hur jag mäter “konsekvent” och “hit or miss”: Jag använder variationskoefficienten (CV = std_sales / mean_sales). 
    Den visar hur mycket ett publishers spel varierar i försäljning i förhållande till deras snittnivå.

    Låg CV betyder att spelen säljer ungefär lika bra, alltså konsekvent.
    Hög CV betyder att några få spel säljer mycket och resten lite, alltså hit or miss.
    """
    summary["cv"] = summary["std_sales"] / summary["mean_sales"]
    return summary.sort_values("total_sales", ascending=False) # Sorterar df på total_sales i fallande ordning (högst till lägst)

# Används för fråga 9: total recorded sales and data coverage per region
def create_df_q9(prepared_charts):
    df = prepared_charts
    region_names = {
        "na_sales": "North America",
        "jp_sales": "Japan",
        "pal_sales": "Europe and Africa",
        "other_sales": "Other"
    }

    # Sammanställer försäljning för varje region
    summary = pd.DataFrame([
        {
            "region": region_names[column], # Hämtar regionens namn från dictionaryn
            "sales_column": column, # Sparar namnet på den ursprungliga försäljningskolumnen
            "total_sales": df[column].sum(min_count=1), # Summerar försäljningsvärdena i regionen
            "records_with_sales": int(df[column].count()) # Räknar antalet rader med ett registrerat försäljningsvärde
        }
        for column in REGIONAL_SALES # Upprepar beräkningarna för varje regional försäljningskolumn i listan.
    ])

    # Beräknar varje regions andel av den totala försäljningen
    summary["share_of_total"] = summary["total_sales"] / summary["total_sales"].sum() * 100

    # Beräknar genomsnittlig försäljning per registrerat värde
    summary["avg_sales_per_record"] = summary["total_sales"] / summary["records_with_sales"]

    return summary


# Används för fråga 10: worldwide sales summed across platform releases per title
def create_title_worldwide_sales(prepared_charts):
    df = prepared_charts.dropna(subset=["title"]) # Tar bort rader som saknar title
    return (
        df.groupby("title")["total_sales"] # Grupperar raderna efter title och väljer kolumnen total_sales för beräkningarna
        .sum(min_count=1)  # Summerar försäljningsvärdena för varje titel om minst ett giltigt värde finns
        .reset_index() # Gör title till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
        .rename(columns={"total_sales": "worldwide_sales"}) # Byter namn på kolumnen total_sales till worldwide_sales
        .sort_values("worldwide_sales", ascending=False) # Sorterar df på worldwide_sales i fallande ordning 
    )

# Används för fråga 11: sales per release year and region
def create_yearly_regional_sales(prepared_charts):
    df = prepared_charts.dropna(subset=["release_year"])  # Tar bort rader där release_year saknas
    return (
        df.groupby("release_year")[REGIONAL_SALES + ["total_sales"]] # Grupperar raderna efter release_year och väljer kolumnerna som ska summeras
        .sum(min_count=1) # Summerar värdena i varje grupp och kolumn om minst ett giltigt värde finns
        .reset_index() # Gör release_year till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
        .sort_values("release_year") # Sorterar efter release_year i stigande ordning, från äldst till nyast
    )

# används för fråga 12: sales grouped by platform and genre
def create_platform_genre_sales(prepared_charts):
    df = prepared_charts.dropna(subset=["platform", "genre"]) # Tar bort rader som saknar platform och ggenre

    summary = (
        df.groupby(["platform", "genre"])["total_sales"] # Grupperar raderna efter plattform och genre och väljer kolumnen total_sales
        .sum(min_count=1) # Summerar total_sales för varje kombination av plattform och genre
        .reset_index() # Gör platform och genre till vanliga kolumner och återställer indexet
    )

    # Beräknar plattformens totala försäljning över alla genrer
    summary["platform_total_sales"] = (summary.groupby("platform")["total_sales"].transform(lambda values: values.sum(min_count=1)))

    # Beräknar hur stor andel av plattformens försäljning i %
    # som kommer från respektive genre
    summary["genre_share"] = (summary["total_sales"] / summary["platform_total_sales"] * 100)

    return summary.sort_values( ["platform", "genre_share"], ascending=[True, False]) # Sorterar plattformarna alfabetiskt och försäljningen inom varje plattform från högst till lägst

# Används för fråga 13: regional sales summed across platform releases per title
def create_title_regional_sales(prepared_charts):
    df = prepared_charts.dropna(subset=["title"]) # Tar bort rader som saknar titel
    return (
        df.groupby("title")[REGIONAL_SALES] # Grupperar raderna efter titel och väljer kolumnerna för regional försäljning
        .sum(min_count=1) # Summerar försäljningsvärdena för varje region och titel om minst ett giltigt värde finns
        .reset_index() # Gör title till en vanlig kolumn och återställer indexet till 0, 1, 2, ...
    )


# Rensar och sparar alla dataframes samt skapar dataframes som behöves för frågorna och sparar dom också
def create_all_preprocessed_data_to_pkl():

    # rensar alla datasets
    vg_charts_prepared = clean_charts(df_charts)
    vg_developers_prepared = clean_developers(df_developers)
    vg_publishers_prepared = clean_publishers(df_publishers)
    vg_geo_cities_prepared = clean_geo_cities(df_geo_cities)
    vg_geo_countries_prepared = clean_geo_countries(df_geo_countries)

    dataframes = {
        "vg_charts_prepared": vg_charts_prepared,
        "vg_developers_prepared": vg_developers_prepared,
        "vg_publishers_prepared": vg_publishers_prepared,
        "vg_geo_cities_prepared": vg_geo_cities_prepared,
        "vg_geo_countries_prepared": vg_geo_countries_prepared,
        "df_q1": create_df_q1(vg_charts_prepared),
        "df_q2": create_df_q2(vg_charts_prepared),
        "df_q3": create_df_q3(vg_charts_prepared),
        "df_q4": create_df_q4(vg_charts_prepared),
        "df_q5": create_df_q5(vg_charts_prepared),
        "df_q6": create_df_q6(vg_charts_prepared),
        "df_q7": create_df_q7(vg_charts_prepared),
        "df_q8": create_df_q8(vg_charts_prepared),
        "df_q9": create_df_q9(vg_charts_prepared),
        "yearly_regional_sales": create_yearly_regional_sales(vg_charts_prepared),
        "title_worldwide_sales": create_title_worldwide_sales(vg_charts_prepared),
        "platform_genre_sales": create_platform_genre_sales(vg_charts_prepared),
        "title_regional_sales": create_title_regional_sales(vg_charts_prepared),
    }

    for name, df in dataframes.items():
        save_df(name, df)

    print(f"\nAll dataframes saved to: {prepaired_data_location}")


if __name__ == "__main__":
    create_all_preprocessed_data_to_pkl()