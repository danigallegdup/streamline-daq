def add_features(data):
    data["moving_avg"] = data["value"].rolling(window=3).mean()
    return data
