import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Florida
florida, combfl = (
    pd.read_csv("../20_outputs/fl_mortality.csv"),
    pd.read_csv("../20_outputs/mortality_comparisons_for_fl.csv"),
)

# ../20_outputs/ combining all three states
# combined_data = pd.concat([florida, texas, washington], axis=0)


# calculating summary statistics
summary_stat = pd.DataFrame(columns=["Florida", "Comparison  State GA, IL, MS"])
summary_stat["Florida"] = florida["Mortality Rate"].describe().values
summary_stat["Comparison  State GA, IL, MS"] = (
    combfl["Mortality Rate"].describe().values
)
summary_stat["Comparison  State GA, IL, MS"] = (
    combfl["Mortality Rate"].describe().values
)

# getting the number of counties
county_unique = [
    len(florida["County"].unique()),
    len(combfl["County"].unique()),
]
summary_stat.loc[len(summary_stat)] = county_unique
# summary_stat= summary_stat.rename(index={'min': 'Minimum Mortality Rate','max': 'Maximum Mortality Rate','std': 'STD of mortality rate','count': 'Observations'})

# creating the index and renaming a few summary
index = list(florida["Mortality Rate"].describe().index)

index.append("Number of Counties")

index = np.char.replace(index, "min", "Minimum Mortality Rate")
index = np.char.replace(index, "max", "Maximum Mortality Rate")
index = np.char.replace(index, "mean", "Mean of Mortality Rate")
index = np.char.replace(index, "count", "Observations")
index = np.char.replace(index, "std", "STD of Mortality Rate")
summary_stat.index = index
summary_stat.iloc[0]
# remove 25,50,75
summary_stat = summary_stat.drop(["25%", "50%", "75%"])
# print(type(summary_stat))
summary_stat = summary_stat.T
summary_stat["Observations"] = summary_stat["Observations"].astype("int64")
summary_stat["Number of Counties"] = summary_stat["Number of Counties"].astype("int64")
# summary_stat.loc[["Observations", "Number of Counties"]]=summary_stat.[["Observations", "Number of Counties"]].round(0).astype('int64')
summary_stat[
    [
        "Minimum Mortality Rate",
        "Maximum Mortality Rate",
        "Mean of Mortality Rate",
        "STD of Mortality Rate",
    ]
] = (
    summary_stat[
        [
            "Minimum Mortality Rate",
            "Maximum Mortality Rate",
            "Mean of Mortality Rate",
            "STD of Mortality Rate",
        ]
    ]
    * 100
).round(
    5
)
print(summary_stat)

#### Texas
texas, combtx = (
    pd.read_csv("../20_outputs/tx_mortality.csv"),
    pd.read_csv("../20_outputs/mortality_comparisons_for_tx.csv"),
)

summary_stat1 = pd.DataFrame(columns=["Texas", "Comparison  State GA, IL, KS"])
summary_stat1["Texas"] = texas["Mortality Rate"].describe().values
summary_stat1["Comparison  State GA, IL, KS"] = (
    combtx["Mortality Rate"].describe().values
)

# getting the number of counties
county_unique1 = [
    len(texas["County"].unique()),
    len(combtx["County"].unique()),
]
summary_stat1.loc[len(summary_stat1)] = county_unique1
# summary_stat= summary_stat.rename(index={'min': 'Minimum Mortality Rate','max': 'Maximum Mortality Rate','std': 'STD of mortality rate','count': 'Observations'})

# creating the index and renaming a few summary
index1 = list(texas["Mortality Rate"].describe().index)

index1.append("Number of Counties")

index1 = np.char.replace(index1, "min", "Minimum Mortality Rate")
index1 = np.char.replace(index1, "max", "Maximum Mortality Rate")
index1 = np.char.replace(index1, "mean", "Mean of Mortality Rate")
index1 = np.char.replace(index1, "count", "Observations")
index1 = np.char.replace(index1, "std", "STD of Mortality Rate")

summary_stat1.index = index1

# remove 25,50,75
summary_stat1 = summary_stat1.drop(["25%", "50%", "75%"])

summary_stat1 = summary_stat1.T
summary_stat1["Observations"] = summary_stat1["Observations"].astype("int64")
summary_stat1["Number of Counties"] = summary_stat1["Number of Counties"].astype(
    "int64"
)
# summary_stat.loc[["Observations", "Number of Counties"]]=summary_stat.[["Observations", "Number of Counties"]].round(0).astype('int64')
summary_stat1[
    [
        "Minimum Mortality Rate",
        "Maximum Mortality Rate",
        "Mean of Mortality Rate",
        "STD of Mortality Rate",
    ]
] = (
    summary_stat1[
        [
            "Minimum Mortality Rate",
            "Maximum Mortality Rate",
            "Mean of Mortality Rate",
            "STD of Mortality Rate",
        ]
    ]
    * 100
).round(
    5
)
print(summary_stat1)


###Washington
washington, combwa = (
    pd.read_csv("../20_outputs/wa_mortality.csv"),
    pd.read_csv("../20_outputs/mortality_comparisons_for_wa.csv"),
)

summary_stat2 = pd.DataFrame(columns=["Washington", "Comparison  State CA, IL, KS"])
summary_stat2["Washington"] = washington["Mortality Rate"].describe().values.round(5)
summary_stat2["Comparison  State CA, IL, KS"] = (
    combwa["Mortality Rate"].describe().values.round(5)
)

# getting the number of counties
county_unique2 = [
    len(washington["County"].unique()),
    len(combwa["County"].unique()),
]
summary_stat2.loc[len(summary_stat2)] = county_unique2
# summary_stat= summary_stat.rename(index={'min': 'Minimum Mortality Rate','max': 'Maximum Mortality Rate','std': 'STD of mortality rate','count': 'Observations'})

# creating the index and renaming a few summary
index2 = list(washington["Mortality Rate"].describe().index)

index2.append("Number of Counties")

index2 = np.char.replace(index2, "min", "Minimum Mortality Rate")
index2 = np.char.replace(index2, "max", "Maximum Mortality Rate")
index2 = np.char.replace(index2, "mean", "Mean of Mortality Rate")
index2 = np.char.replace(index2, "count", "Observations")
index2 = np.char.replace(index2, "std", "STD of Mortality Rate")

summary_stat2.index = index2

# remove 25,50,75
summary_stat2 = summary_stat2.drop(["25%", "50%", "75%"])
summary_stat2 = summary_stat2.T
summary_stat2["Observations"] = summary_stat2["Observations"].astype("int64")
summary_stat2["Number of Counties"] = summary_stat2["Number of Counties"].astype(
    "int64"
)
# summary_stat.loc[["Observations", "Number of Counties"]]=summary_stat.[["Observations", "Number of Counties"]].round(0).astype('int64')
summary_stat2[
    [
        "Minimum Mortality Rate",
        "Maximum Mortality Rate",
        "Mean of Mortality Rate",
        "STD of Mortality Rate",
    ]
] = (
    summary_stat2[
        [
            "Minimum Mortality Rate",
            "Maximum Mortality Rate",
            "Mean of Mortality Rate",
            "STD of Mortality Rate",
        ]
    ]
    * 100
).round(
    5
)
print(summary_stat2)

"""
combined_data = pd.concat([florida, texas, washington], axis=0)
print("Mortality Rate for each State over Years")
combined_data.groupby(["Year", "State"]).mean()["Mortality Rate"]
print("Average Mortality Rate each year in TX,FL, WA Combined")
combined_data.groupby("Year").mean()["Mortality Rate"]
year = []
ac = florida.groupby(["Year", "State"]).mean()
ac=ac.reset_index()

#for i in range(len(ac)):
#    year.append(ac.index[i][0])
ac = ac.reset_index(drop=True)

plt.plot(ac['Year'], ac["Mortality Rate"])
plt.title("Florida Average Mortality Rates")
plt.ylabel("Average Mortality Rate")
plt.xlabel("Year")
plt.show()

year1 = []
bc = texas.groupby(["Year", "State"]).mean()
for i in range(len(bc)):
    year1.append(bc.index[i][0])
bc["year"] = year1
bc = bc.reset_index(drop=True)
plt.plot(year1, bc["Mortality Rate"])
plt.title("Texas Average Mortality Rates")
plt.ylabel("Average Mortality Rate")
plt.xlabel("Year")
plt.show()

year2 = []
cc = washington.groupby(["Year", "State"]).mean()
for i in range(len(cc)):
    year2.append(cc.index[i][0])
cc["year"] = year2
cc = cc.reset_index(drop=True)
plt.plot(year2, cc["Mortality Rate"])
plt.title("Washington Average Mortality Rates")
plt.ylabel("Average Mortality Rate")
plt.xlabel("Year")
plt.show()

year3 = []
dc = combined_data.groupby(["Year"]).mean()
for i in range(len(dc)):
    year3.append(dc.index[i])
dc["year"] = year3
dc = dc.reset_index(drop=True)
plt.plot(year3, dc["Mortality Rate"])
plt.title("All States Average Mortality Rates")
plt.ylabel("Average Mortality Rate")
plt.xlabel("Year")
plt.show()


"""
