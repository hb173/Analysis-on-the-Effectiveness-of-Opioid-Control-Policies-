#%%
# Mortality Analysis
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from analysis_functions import regression_mortality, regression_shipment

#%%
# Define regression_mortality function
policyyear = {"fl": 2010, "tx": 2007, "wa": 2012}

#%%
# Florida Analysis
fl_df, fl_model = regression_mortality("FL")
fl_model

with open("../20_outputs/regression_fl_mortality.csv", "w") as f:
    f.write(fl_model.as_csv())
#%%
# Washington Analysis
wa_df, wa_model = regression_mortality("WA")
wa_model

#%%
# Texas Analysis
tx_df, tx_model = regression_mortality("TX")
tx_model


# %%

fl_model_ship = regression_shipment("fl")
fl_model_ship

with open("../20_outputs/regression_fl_shipments.csv", "w") as f:
    f.write(fl_model_ship.as_csv())


# %%
wa_model_ship = regression_shipment("wa")
wa_model_ship