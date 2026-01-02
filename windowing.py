import pandas as pd

data = pd.read_csv("daily_data.csv")

def get_windows(df, short=7, mid=30, long=90):
    return {
        "short_term": df.tail(short),
        "mid_term": df.tail(mid),
        "long_term": df.tail(long)
    }

windows = get_windows(data)

print("Window sizes:")
for name, w in windows.items():
    print(f"{name}: {len(w)} days")
