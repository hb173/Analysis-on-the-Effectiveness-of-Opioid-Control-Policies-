#%%
import dask.dataframe as dd

cols_of_interest = {
    "DRUG_NAME": "category",
    "QUANTITY": "uint16",
    "STRENGTH": "float",
    "TRANSACTION_DATE": "datetime64",
    "REPORTER_COUNTY": "category",
    "NDC_NO": "category",
    "DOSAGE_UNIT": "uint32",
}

#%%
# To read prepared data choose: False; False

# Read file with all columns and unoptimized dtypes
READ_WHOLE_RAW_FILE = False
# Save reduced file (selected columns + dtypes optimized) to disk
RE_SAVE_AS_SMALLER_PARQUET = False

if READ_WHOLE_RAW_FILE:
    # Read the raw CSV file (not recommended for speed)
    # df = dd.read_csv(
    #     "../00_source_data/arcos-fl-statewide-itemized.csv",
    #     dtype=cols_of_interest,
    #     usecols=cols_of_interest.keys(),
    #     parse_dates=["TRANSACTION_DATE"],
    #     infer_datetime_format=True,
    # )

    # Read the raw file (parquet version)
    df = dd.read_parquet(
        "../00_source_data/arcos-fl-statewide-itemized.parquet",
        columns=cols_of_interest.keys(),
        parse_dates=["TRANSACTION_DATE"],
        infer_datetime_format=True,
    )

    # colnames to lowercase
    df.columns = [col.lower() for col in df.columns]
    df.head()

    # dtype conversions
    df["transaction_date"] = dd.to_datetime(df["transaction_date"], format="%m%d%Y")
    for col in list(x.lower() for x in cols_of_interest.keys()):
        df[col] = df[col].astype(cols_of_interest[col.upper()])

    if RE_SAVE_AS_SMALLER_PARQUET:
        print("[INFO] Re-saving as smaller parquet.")
        df.to_parquet("../20_outputs/shipments.parquet", engine="fastparquet")
    else:
        print("[INFO] Did NOT re-save smaller parquet.")

else:
    print("[INFO] Loading smaller parquet from disk.")
    df = dd.read_parquet("../20_outputs/shipments.parquet")
    df.head()


#%%
(df["dosage_unit"] == 0).sum().compute()  # 3 rows with zero dosage


#%%

na_pct = (df.isna().sum() / len(df)).compute().to_dict()

# Print data frame summary
print(f"{' SUMMARY ':=^80}")
print(
    f"- Date range: {df.transaction_date.min().compute()} - {df.transaction_date.max().compute()}"
)
print(f"- Unique drugs: {df.drug_name.unique().compute().tolist()}")
print(f"- Number of counties: {df.reporter_county.nunique().compute()}")
print("- NA Stats (% NA):")
for k, v in na_pct.items():
    print(f"    - {k:<20}: {v:.1%}")
print(f"=" * 80)

# strength has 69% missing values!

#%%
