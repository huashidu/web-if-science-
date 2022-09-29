import pandas as pd


way = ' '
df = pd.read_excel('way')
df.fillna(0)
data = df[['Article Title',
           'Authors',
           'Source Title',
           'Volume',
           'Issue',
           'Start Page',
           'End Page',
           'DOI',
           'Publication Date',
           'Publication Year',
           'Special Issue']]
# data = data.fillna(0)

for i in range(len(data)):
    title = data.iloc[i][0]
    author = data.iloc[i][1]
    source_title = data.iloc[i][2]
    volume = data.iloc[i][3]
    issue = data.iloc[i][4]
    start = data.iloc[i][5]
    end = data.iloc[i][6]
    doi = data.iloc[i][7]
    date = data.iloc[i][8]
    year = data.iloc[i][9]
    special = data.iloc[i][10]
    print("[{0}]标题:".format(i + 1), title)
    print("作者:", author)
    print("来源出版物:", source_title, end=' ')
    if pd.notnull(volume):
        if isinstance(volume, float):
            print("卷:", int(volume), end=' ')
        else:
            print("卷:", volume, end=' ')
    if pd.notnull(issue):
        if isinstance(issue, float):
            print("期:", int(issue), end=' ')
        else:
            print("期:", issue, end=' ')
    if pd.notnull(start):
        print("页:", "%d-%d" % (start, end), end=' ')
    if pd.notnull(special):
        print("特刊:", special, end=' ')
    if pd.notnull(doi):
        print("DOI:", doi, end=' ')
    if pd.isnull(date) and pd.isnull(year):
        print()
    elif pd.notnull(date) and pd.isnull(year):
        print("出版年:", date)
    elif pd.isnull(date) and pd.notnull(year):
        print("出版年:", int(year))
    else:
        if str(date)[-4:] == str(int(year)):
            print("出版年:", date)
        else:
            print("出版年:", date, int(year))
