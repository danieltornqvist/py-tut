import pandas as pd
from functions import add_twelve 

df = pd.DataFrame(data={
    'col1' : [1, 2, 3],
    'col2' : ['dog', 'cat', 'fish']
})
df['col1'] = df['col1'].apply(add_twelve)

print(df)

test = "Git push is working"
print(test)
# This will comment may be seen in Git if properly committed, and pushed.