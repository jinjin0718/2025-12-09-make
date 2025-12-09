# python 03-model.py --file_path=data/clean/titanic_clean.csv --output_path=output/model.joblib
import pandas as pd
import click
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib


@click.command()
@click.option("--file_path", required=True, help="Path to input CSV file")
@click.option("--output_path", required=True, help="Path to output model file")
def main(file_path, output_path):
    """This script trains a logistic regression model on titanic data"""

    data = pd.read_csv(file_path)

    # prepare features
    model_data = data[["pclass", "sex", "age", "fare", "survived"]].dropna()

    # encode categorical variables
    le = LabelEncoder()
    model_data["sex_encoded"] = le.fit_transform(model_data["sex"])
    model_data["pclass"] = model_data["pclass"].astype("category")

    # create dummy variables for pclass
    X = pd.get_dummies(
        model_data[["pclass", "sex_encoded", "age", "fare"]],
        columns=["pclass"],
        drop_first=False,
    )
    y = model_data["survived"]

    # fit logistic regression
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    # save model
    joblib.dump(model, output_path)

    # return model for inspection (similar to summary in R)
    model

    print("Finsihed Model.")


if __name__ == "__main__":
    main()
