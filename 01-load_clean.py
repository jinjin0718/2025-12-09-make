# python 01-load_clean.py --file_path=data/original/titanic.csv --output_path=data/clean/titanic_clean.csv
import pandas as pd
import click


@click.command()
@click.option("--file_path", required=True, help="Path to input CSV file")
@click.option("--output_path", required=True, help="Path to output CSV file")
def main(file_path, output_path):
    """This script loads, cleans, saves titanic data"""

    # load data
    data = pd.read_csv(file_path)

    # clean data (convert column names to snake_case)
    data.columns = (
        data.columns.str.lower()
        .str.replace(" ", "_")
        .str.replace("[^a-z0-9_]", "", regex=True)
    )

    # save data
    data.to_csv(output_path, index=False)

    print("Finished Loading and Cleaning.")


if __name__ == "__main__":
    main()
