ydata=data['합격여부'].values # 결과값
xdata=[] # 결과를 도출해내기 위한 값들
for i, rows in data.iterrows(): # iterrows? 값을 가로로 출력하라
    xdata.append([rows['어학점수'], rows['학점평군'], rows['대학원라인']]) # 3개의 값이 있기 때문에 튜플과 리스트 사용


