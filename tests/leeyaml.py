#%%
import yaml
from logparser import parser

# %%
with open('tests/toParse.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    # print(data)

    # sorted = yaml.dump(data, sort_keys=True)
    # print(sorted)

# %%
for item in data:
    item.get("name")

# %%
vector = data[0].get("vector")
vector[0]