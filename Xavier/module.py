from Params import params as pm
import pandas as pd

df = pd.DataFrame(pm)
df.to_csv("xavier.csv")
