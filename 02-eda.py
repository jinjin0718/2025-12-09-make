# python 02-eda.py --input_path=data/clean/titanic_clean.csv --output_path=output/titanic1.png
import pandas as pd
import click
from plotnine import ggplot, aes, geom_bar, ggtitle, ggsave


@click.command()
@click.option(
    "--input_path",
    default="data/clean/titanic_clean.csv",
    help="Path to input CSV file",
)
@click.option(
    "--output_path", default="output/titanic1.png", help="Path to output plot file"
)
def main(input_path, output_path):
    """This script performs EDA on titanic data"""

    # don't do this
    # from load_clean import main

    data = pd.read_csv(input_path)

    # eda

    bar = (
        ggplot(data, aes(x="pclass", fill="factor(survived)"))
        + geom_bar()
        + ggtitle("titanic")
    )

    bar.save(filename=output_path)

    ggplot(data, aes(x="survived")) + geom_bar()

    print("Finished EDA.")


if __name__ == "__main__":
    main()
