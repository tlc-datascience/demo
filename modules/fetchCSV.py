def downloadCSV(url):
    import pandas as pd 
    import requests
    x = requests.get(url, params=None)

    # Find Button
    btn = x.content.decode('utf-8')
    index = btn.find("btn datagovsg-btn btn-right btn-orange ga-dataset-download")
    sub = btn[index:index+1000]
    index_download_1 = sub.find('href="')
    index_download_2 = sub.find('/download')

    data = sub[index_download_1 + len('href="'): index_download_2 + len('/download')]

    # Get URL 
    data_url = 'https://data.gov.sg'+ data
    req = requests.get(data_url, params=None)

    # Download ZIP
    s = str(req.content)

    s1 = str(req.content).find('    Url: ')
    s2 = str(req.content).find('.csv')

    filename = url.split('/')[-1]
        
    # # Writing the file to the local file system
    # with open(filename,'wb') as output_file:
    #     output_file.write(req.content)

    try: 
        # GET CSV URL
        s_data = s[s1+len('    Url:  '):s2+len('.csv')]
        s_data = s_data[s_data.index('https'):]
        print("::", s_data)
        # SAVE TO CSV

        req1 = requests.get(s_data, params=None)

        # Writing the file to the local file system (buffer)
        with open('temp.csv','wb') as output_file:
            output_file.write(req1.content)

        out = pd.read_csv('temp.csv')
        return out

    except:
        return 0 

