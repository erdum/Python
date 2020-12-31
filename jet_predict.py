def predict_jet(cockpit, composite):
    import pandas as pd
    import numpy as np
    from sklearn import linear_model
    from sklearn.metrics import r2_score
    data = pd.read_csv("http://erdum.42web.io/jet.csv")
    train = data[:int((len(data)*0.8))]
    test = data[int((len(data)*0.8)):]
    train_x = np.array(train[["COMPOSITE", "COCKPIT"]])
    train_y = np.array(train[["GENERATION"]])
    test_x = np.array(test[["COMPOSITE", "COCKPIT"]])
    test_y = np.array(test[["GENERATION"]])
    regr = linear_model.LinearRegression()
    regr.fit(train_x, train_y)
    my_jet = np.array([[composite, cockpit]])
    return regr.predict(my_jet)


