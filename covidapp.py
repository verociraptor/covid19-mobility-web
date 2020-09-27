from gs_quant.session import GsSession, Environment
from gs_quant.data import Dataset
from datetime import date, datetime
import constant as c 
import matplotlib.pyplot as plt 

# Example code to show graph of CDC data sets
GsSession.use(client_id=c.CLIENT_ID, client_secret=c.CLIENT_SECRET, scopes=('read_product_data',)) # authenticate GS Session with credentials

dataset = Dataset('COVID19_US_DAILY_CDC')                      # initialize the dataset
frame = dataset.get_data(countryId='US', start = date(2019,1,1))        # pull the US data into a Pandas dataframe

# time = frame['date']
cases = frame['totalConfirmed'] 
plt.plot(cases, label='Implied Volatility by Strike')
plt.xlabel('date')
plt.ylabel('confirmed cases')
plt.title('Implied Volatility by Strike')

plt.show()