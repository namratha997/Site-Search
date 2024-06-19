import pandas as pd
from flask import Flask, request, render_template
import sys

# Add the path to the module and import the WGDataApi
sys.path.append('\\modules')
from WgDataApi import WGDataApi # type: ignore

app = Flask(__name__)

# Initialize the API with the given key
api_key = 'API-Key'
wg_api = WGDataApi(api_key)

# Get all site data
wg_sites = wg_api.get_all_sites()

# Convert site data to DataFrame 
wg_sites_df = pd.DataFrame(wg_sites)

# Check if required columns are in DataFrame
print(wg_sites_df.columns)

# Convert date columns to desired format
wg_sites_df['GoLive'] = pd.to_datetime(wg_sites_df['goLiveDate']).dt.strftime('%m/%d/%Y')
wg_sites_df['validationDate'] = pd.to_datetime(wg_sites_df['validationDate']).dt.strftime('%m/%d/%Y')
wg_sites_df['closeOutPackageDate'] = pd.to_datetime(wg_sites_df['closeOutPackageDate']).dt.strftime('%m/%d/%Y')
wg_sites_df['cancellationDate'] = pd.to_datetime(wg_sites_df['cancellationDate']).dt.strftime('%m/%d/%Y')

# Function to search for a siteId and return relevant dates
def search_site(site_id):
    result = wg_sites_df[wg_sites_df['wgSiteId'] == site_id]
    if not result.empty:
        site_id = result['wgSiteId'].values[0]
        validation_date = result['validationDate'].values[0]
        go_live_date = result['GoLive'].values[0]
        close_out_package_date = result['closeOutPackageDate'].values[0]
        cancellation_date = result['cancellationDate'].values[0]
        return site_id, validation_date, go_live_date, close_out_package_date, cancellation_date
    else:
        return None, None, None, None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        site_id = request.form['site_id']
        site_id, validation_date, go_live_date, close_out_package_date, cancellation_date = search_site(site_id)
        if validation_date and go_live_date and close_out_package_date and cancellation_date:
            result = {
                'site_id': site_id,
                'validation_date': validation_date,
                'go_live_date': go_live_date,
                'close_out_package_date': close_out_package_date,
                'cancellation_date': cancellation_date
            }
        else:
            result = "Site Not Found"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
