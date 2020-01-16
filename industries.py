import pandas as pd
if __name__ == '__main__':
  df = pd.read_html('https://developer.linkedin.com/docs/reference/industry-codes')[0]
  df.columns = df.iloc[0]
  df.drop(df.index[0])
  df.to_csv('industries.csv')