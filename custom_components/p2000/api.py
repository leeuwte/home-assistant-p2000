import requests
import json

class P2000Api:
    url = "https://beta.alarmeringdroid.nl/api2/find/"

    def __init__(self):
        self.session = requests.Session()

    def get_data(self, apiFilter):

        response = self.session.get(self.url + json.dumps(apiFilter),
                                    params={},
                                    allow_redirects=False)

        if response.status_code != 200:
            raise RuntimeError("Request failed: %s", response)

        data = json.loads(response.content.decode('utf-8'))
        
        if (len(data['meldingen']) == 0):
            return None;

        # Get the first melding, maybe extend it later for multiple messages.
        result = data['meldingen'][0]

        if (result == None):
            return None


        # Rename lat & lon
        result["latitude"] =  result.get("lat", None)
        result["longitude"] = result.get("lon", None)  

        if 'lat' in result:
            del result['lat']

        if 'lon' in result:
            del result['lon']

        # Return result
        return result