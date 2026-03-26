from sklearn.feature_extraction.text import HashingVectorizer

def stats_feat_text(text):
    hv = HashingVectorizer(n_features=5000)
    X = hv.transform(text).toarray()
    return X