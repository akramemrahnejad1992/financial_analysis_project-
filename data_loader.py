import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path, sep='|', error_bad_lines=False)
    data['DateTime'] = pd.to_datetime(data['DateTime'])
    data = data.set_index('DateTime', drop=False)
    data['VAP_Prices'] = data['VAP_Prices'].apply(lambda x: list(eval(x)))
    data['VAP_Volumes'] = data['VAP_Volumes'].apply(lambda x: list(eval(x)))
    return data