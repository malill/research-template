import src.d01_data as d01
import pandas as pd
from datetime import datetime


def create_submission(model, X):
    res = model.predict(X)
    df = pd.DataFrame(res, index=X.index)
    date = str(datetime.today().strftime('%Y%m%d'))
    model_class = str(model.__class__.__name__)
    d01.write_data(df, '06_reporting', date + '_' + model_class)
