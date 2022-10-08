rp = GithubData('https://github.com/imahdimir/d-USD-IRR-monthly')
df = rp.read_data()

##
df['USD-Rial'] = df['USD-Rial'].astype(int)
##
rp = GithubData('https://github.com/imahdimir/d-TSE-Overall-Index-TEDPIX')
df1 = rp.read_data()

##
df1.reset_index(inplace = True)

##
df1['JMonth'] = df1['JDate'].str[:7]
##
msk = df1.groupby('JMonth').tail(1).index

df2 = df1.loc[msk]

##
df = df.merge(df2[['JMonth' , 'TEDPIXClose']] , on = 'JMonth' , how = 'outer')

##
fp = '/Users/mahdi/Desktop/coin.xlsx'
df1 = pd.read_excel(fp)

##
df1 = df1[['JDate' , 'Close']]

##
df1.rename(columns = {
        'Close' : 'Sekke'
        } , inplace = True)

##
df1['JMonth'] = df1['JDate'].str[:7]
##
msk = df1.groupby('JMonth').tail(1).index

df2 = df1.loc[msk]

##
df = df.merge(df2[['JMonth' , 'Sekke']] , on = 'JMonth' , how = 'outer')

##
fp = '/Users/mahdi/Desktop/rf.xlsx'
df1 = pd.read_excel(fp)

##
df = df.merge(df1[['JMonth' , 'RiskFreeRateAPR']] ,
              on = 'JMonth' ,
              how = 'outer')

##
fp = '/Users/mahdi/Desktop/Home-Monthly.xlsx'

df1 = pd.read_excel(fp)
##
df = df.merge(df1[['JMonth' , 'Home']] , on = 'JMonth' , how = 'outer')

##
fp = '/Users/mahdi/Desktop/CPI-Monthly.xlsx'
df1 = pd.read_excel(fp)

##
df1 = df1[['JMonth' , 'CPI']]

##
df1['Inflation'] = df1['CPI'].pct_change()

##
df1['Inflation'] = df1['Inflation'] * 100
##
df1 = df1[['JMonth' , 'Inflation']]

##
df = df.merge(df1 , on = 'JMonth' , how = 'outer')

##
snxl(df , 'mkts.xlsx')

##