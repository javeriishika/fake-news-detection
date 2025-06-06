import pandas as pd

fake_df = pd.read_csv('data/Fake.csv')
real_df = pd.read_csv('data/True.csv')

fake_df['label'] = 'FAKE'
real_df['label'] = 'REAL'

combined = pd.concat([fake_df, real_df], ignore_index=True)
combined = combined[['title', 'text', 'label']]
combined.to_csv('data/news.csv', index=False)

