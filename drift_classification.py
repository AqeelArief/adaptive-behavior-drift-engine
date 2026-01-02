import pandas as pd

data = pd.read_csv("daily_data.csv")

METRICS = [
    "sleep_hours",
    "steps",
    "screen_time_hours",
    "workout_minutes",
    "study_hours"
]

def get_windows(df, short=7, mid=30, long=90):
    return {
        "short": df.tail(short),
        "mid": df.tail(mid),
        "long": df.tail(long)
    }

def classify_drift(short_mean, mid_mean, long_mean, confidence):
    diff_short_mid = short_mean - mid_mean
    diff_mid_long = mid_mean - long_mean

    if confidence < 0.5:
        return "temporary fluctuation"

    if abs(diff_short_mid) > abs(diff_mid_long) * 1.5:
        return "sudden shift"

    return "gradual drift"

windows = get_windows(data)

print("Drift classification results:")
for metric in METRICS:
    short_mean = windows["short"][metric].mean()
    mid_mean = windows["mid"][metric].mean()
    long_mean = windows["long"][metric].mean()

    confidence = abs(short_mean - mid_mean) + abs(mid_mean - long_mean)

    drift_type = classify_drift(
        short_mean,
        mid_mean,
        long_mean,
        confidence
    )

    print(f"{metric}: {drift_type}")
