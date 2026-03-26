from Weighted_Class_Tfidf_main.wcbtfidf import Wcbtfidf


def Modified_weighted_TFIDF(features, labels):
    wcbtfidf = Wcbtfidf(
        max_features=100,
        custom_weights={0: 10, 1: 15, 2: 20, 3: 25, 4: 30}
    )

    wcbtfidf.fit(features, labels)

    X_transformed = wcbtfidf.transform(features)

    return X_transformed, wcbtfidf
