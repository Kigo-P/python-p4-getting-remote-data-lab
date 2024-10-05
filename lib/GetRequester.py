import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # # creating a variable that contains the url endpoint
        # url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        # using get method to create a response based on the url
        response = requests.get(self.url)
        #  returning the response.content
        print(response.content)
        return(response.content)
    

    def load_json(self):
        # creating a variable that uses json.loads() to convert json to python
        json_content = json.loads(self.get_response_body())
        # returning the data 
        return json_content
        
