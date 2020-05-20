import sqlite3
import pandas as pd


conn = sqlite3.connect('/Users/admin/purchase_ql/backend/db.sqlite3')
df = pd.read_csv('/Users/admin/purchase_ql/backend/sam.csv')
df['id'] = df.index
df = df[['id', 'Segement', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
df.to_sql('graphApp_productmodel', conn, if_exists='replace', index=False)
