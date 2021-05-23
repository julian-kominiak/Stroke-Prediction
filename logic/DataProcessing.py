class DataProcessing:
    def __init__(self):
        return

    @staticmethod
    def shuffle(x):
        for i in range(len(x)-1,0,-1):
            j = rd.randint(0,i)
            x.iloc[i], x.iloc[j] = x.iloc[j], x.iloc[i]
        return x

    @staticmethod
    def normalize(df):
        normalized = df.drop("stroke", axis=1)
        normalized = (normalized - normalized.min())/(normalized.max() - normalized.min())
        normalized = normalized.join(df["stroke"])
        return normalized

    @staticmethod
    def split_set(x):
        k = int(len(x)*0.7)
        train = x[:k]
        val = x[k:]
        return train, val