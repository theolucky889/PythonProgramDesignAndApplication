import pandas as pd

def find_and_display(csv_file):
    df = pd.read_csv(csv_file, encoding='utf-8')
    
    filtered_df = df[df['學校名稱'].str.contains('國立臺北科技大學')]
    
    result_df = filtered_df[['學年度', '學校名稱', '科系名稱', '日間∕進修別', '等級別', '總計', '男生計', '女生計']]

    return result_df

csv_path = '112_students.csv' 

data_frame = find_and_display(csv_path)
if data_frame.empty:
    print('No data found.')
else:
    display(data_frame) # open in jupyter notebook 
