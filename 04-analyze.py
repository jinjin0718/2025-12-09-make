# python 04-analyze.py --model=output/model.joblib --output_coef=output/coefficients.csv --output_fig=output/coef_plot.png
import pandas as pd
import click
import joblib
from plotnine import ggplot, aes, geom_point, coord_flip, geom_hline, ggsave
import numpy as np


@click.command()
@click.option("--model", required=True, help="Path to input model file")
@click.option("--output_coef", required=True, help="Path to output coefficients CSV")
@click.option("--output_fig", required=True, help="Path to output figure")
def main(model, output_coef, output_fig):
    """This script analyzes logistic regression model results"""

    # load model
    fitted_model = joblib.load(model)

    # extract coefficients
    coef = pd.DataFrame(
        {
            "term": ["intercept"] + list(fitted_model.feature_names_in_),
            "estimate": np.concatenate(
                [[fitted_model.intercept_[0]], fitted_model.coef_[0]]
            ),
        }
    )

    # process results - calculate odds ratios
    coef["or"] = np.exp(coef["estimate"])

    # save coefficients
    coef.to_csv(output_coef, index=False)

    # plot results
    plot_data = coef[coef["term"] != "intercept"]

    g = (
        ggplot(plot_data, aes(x="term", y="or"))
        + geom_point()
        + coord_flip()
        + geom_hline(yintercept=1)
    )

    g.save(filename=output_fig)

    coef

    print(coef)

    print("Finished Analyzing.")


if __name__ == "__main__":
    main()
