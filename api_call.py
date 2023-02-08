# In this example, the function query_clinical_trials takes in the keywords and API key as inputs and 
# returns a list of trial records that match the keywords. The function starts with an initial offset of
# 0 and retrieves 1000 trials at a time. The function repeats the query and increments the offset until
# there are no more trials to retrieve. The returned results are concatenated to the results list.

import requests

def query_clinical_trials(keywords, api_key):
    results = []
    offset = 0
    count = 1000
    while True:
        params = {
            "expr": keywords,
            "min_rnk": 1,
            "max_rnk": count,
            "fmt": "JSON",
            "api_key": api_key,
            "of": offset
        }
        response = requests.get("https://api.clinicaltrials.gov/v1/trial", params=params)
        data = response.json()
        trials = data["trials"]
        if not trials:
            break
        results += trials
        offset += count
    return results

keywords = "cancer treatment"
api_key = "YOUR_API_KEY"
trials = query_clinical_trials(keywords, api_key)