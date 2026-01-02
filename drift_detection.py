import pandas as pd

data = pd.read_csv("daily_data.csv")

METRICS = [
    "sleep_hours",
    "steps",
    "screen_time_hours",
    "workout_minutes",
    "study_hours"
]

def mean_diff(a, b):
    return a.mean() - b.mean()

def detect_drift(short, mid, long):
    drift_results = {}

    for metric in METRICS:
        short_mean = short[metric].mean()
        mid_mean = mid[metric].mean()
        long_mean = long[metric].mean()

        drift_results[metric] = {
            "short_vs_mid": round(short_mean - mid_mean, 2),
            "mid_vs_long": round(mid_mean - long_mean, 2)
        }

    return drift_results

def get_windows(df, short=7, mid=30, long=90):
    return {
        "short": df.tail(short),
        "mid": df.tail(mid),
        "long": df.tail(long)
    }

windows = get_windows(data)
drift = detect_drift(
    windows["short"],
    windows["mid"],
    windows["long"]
)

print("Drift results:")
for metric, values in drift.items():
    print(metric, values)
