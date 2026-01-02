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

def compute_confidence(short_mean, mid_mean, long_mean):
    diff_short_mid = short_mean - mid_mean
    diff_mid_long = mid_mean - long_mean

    magnitude = abs(diff_short_mid) + abs(diff_mid_long)

    consistent = (diff_short_mid * diff_mid_long) > 0
    consistency_bonus = 1.5 if consistent else 1.0

    confidence = magnitude * consistency_bonus
    return round(confidence, 2), consistent

windows = get_windows(data)

print("Drift confidence scores:")
for metric in METRICS:
    short_mean = windows["short"][metric].mean()
    mid_mean = windows["mid"][metric].mean()
    long_mean = windows["long"][metric].mean()

    confidence, consistent = compute_confidence(
        short_mean, mid_mean, long_mean
    )

    print(
        f"{metric}: confidence={confidence}, "
        f"consistent={'yes' if consistent else 'no'}"
    )
