data=pd.read_csv('데이터.csv') # 파일을 읽어내는 명령어
print(data)
data=data.dropna() # 공란 제외