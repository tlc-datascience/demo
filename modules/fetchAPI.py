def fetchData():
  import requests
  import pandas as pd

  url = "https://yh-finance.p.rapidapi.com/stock/v2/get-chart"

  querystring = {"interval":"5m","symbol":"AMRN","range":"1d","region":"US"}

  headers = {
    "X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
    "X-RapidAPI-Key": "b7b51adbcdmsh186729b53126ee3p1ba27cjsndd9ab3a4fe7d"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  t = response.json()['chart']['result'][0]['timestamp']
  r = response.json()['chart']['result'][0]['indicators']['quote'][0]

  close = r['close']
  high = r['high']
  open = r['open']
  low = r['low']
  volume = r['volume']

  import pandas as pd

  df = pd.DataFrame({
      'timestamp': t,
      'close': close,
      'high': high,
      'low': low,
      'volume': volume
  })


  df['timestamp'] = pd.to_datetime(df['timestamp'],unit='s') # Convert to DateTime obj

  return df