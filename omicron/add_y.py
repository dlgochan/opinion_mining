import pandas as pd

# 정제 끝난 words 파일에서 y_label 추가하는 코드
df_words = pd.read_csv("./nlp/words.csv", index_col=0)
df_y = pd.read_csv("./opm/y_label.csv", index_col=0)

df_words['y'] = df_y['y']

df_words.to_csv('./opm/words.csv')