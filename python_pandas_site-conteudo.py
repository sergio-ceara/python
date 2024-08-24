import pandas as pd
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
url = 'https://en.wikipedia.org/wiki/Minnesota'
dfs = pd.read_html(url)
print("type(dfs):",type(dfs))
print("len(dfs):",len(dfs))
for i, df in enumerate(dfs):
    print(f"DataFrame {i}:")
    print(df)
    print("\n" + "="*40 + "\n")