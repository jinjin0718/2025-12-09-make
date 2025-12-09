# use PHONY to specify `all`, `clean`, `scratch` are just general commands name that you give
.PHONY: all clean scratch

# what is the main thing that you care about
all: 
	make index.html

# <this is an output file>: <dependencies: and it depends on these files>
# essentially telling make: if these files changes (the dependencies), that means the output file is outdated
# and therefore, the instructions is to run the next line's code
data/clean/titanic_clean.csv: 01-load_clean.py data/original/titanic.csv
	python 01-load_clean.py --file_path=data/original/titanic.csv --output_path=data/clean/titanic_clean.csv

index.html: report.qmd output/coefficients.csv output/coef_plot.png
	quarto render report.qmd --output index.html

output/coefficients.csv output/fig.png: 04-analyze.py output/model.joblib
	python 03-model.py --file_path=data/clean/titanic_clean.csv --output_path=output/model.joblib


# clean previous generated files
# to reset everythine
clean: 
	rm -f output/*
	rm -f data/clean/*
	rm -f report.html
	rm -f index.html
	rm -f *.pdf

# force run everything
# to make sure your whole pipeline works
scratch: 
	make clean
	python 01-load_clean.py --file_path=data/original/titanic.csv --output_path=data/clean/titanic_clean.csv
	python 02-eda.py --input_path=data/clean/titanic_clean.csv --output_path=output/titanic1.png
	python 03-model.py --file_path=data/clean/titanic_clean.csv --output_path=output/model.joblib
	python 04-analyze.py --model=output/model.joblib --output_coef=output/coefficients.csv --output_fig=output/coef_plot.png
	quarto render report.qmd --output index.html