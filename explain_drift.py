import pandas as pd

data = pd.read_csv("daily_data.csv")

METRICS = {
    "sleep_hours": "sleep duration",
    "steps": "physical activity",
    "screen_time_hours": "screen time",
    "workout_minutes": "workout activity",
    "study_hours": "study time"
}

def get_windows(df, short=7, mid=30, long=90):
    return {
        "short": df.tail(short),
        "mid": df.tail(mid),
        "long": df.tail(long)
    }

def explain(metric, short_mean, mid_mean, long_mean):
    if short_mean > mid_mean and mid_mean > long_mean:
        return f"{METRICS[metric]} has steadily increased over time."
    if short_mean < mid_mean and mid_mean < long_mean:
        return f"{METRICS[metric]} has steadily decreased over time."
    if abs(short_mean - mid_mean) > abs(mid_mean - long_mean):
        return f"{METRICS[metric]} changed sharply in the recent period."
    return f"{METRICS[metric]} shows minor or temporary variation."

windows = get_windows(data)

print("Behavioral Drift Explanations:\n")
for metric in METRICS:
    short_mean = windows["short"][metric].mean()
    mid_mean = windows["mid"][metric].mean()
    long_mean = windows["long"][metric].mean()

    explanation = explain(metric, short_mean, mid_mean, long_mean)
    print(f"- {explanation}")
