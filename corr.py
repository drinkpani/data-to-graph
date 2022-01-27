#!/usr/bin/python3
import sys
import pandas as pd

df = pd.read_csv(f"data/{sys.argv[1]}.tsv", sep="\t")

# fig.subplots_adjust(bottom=0.15)
print(
    df[
        [
            "TEMP",
            "PH VALUE",
            "EC VALUE",
            "TURBIDITY (NTU)",
        ]
    ].corr(method="pearson")
)
