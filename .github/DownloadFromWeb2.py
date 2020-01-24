from urllib import request

sales_url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'

def download_csv(csv_url):
    response = request.urlopen(csv_url) # - Connects
    csv = response.read() # - Assigns to a variable
    csv_str = str(csv) # - Concatenates to string
    lines = csv_str.split("\\n") # - Splits a long line of text.
    dest_url= r'salesdata.csv' # - saves as salesdata.csv
    fx = open(dest_url, "w") # - Opening a file to write to it.
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_csv(sales_url)