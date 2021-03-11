#!/bin/bash

import requests
import json
import base64

#r = requests.get("http://127.0.0.1:8089/")
#print(r.text)

text = """
    The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price. The deal, first reported by The Real Deal, was for $150 million, according to a source familiar with the deal. Mubadala, an Abu Dhabi investment fund, purchased 90% of the building for $800 million in 2008. Real estate firm Tishman Speyer had owned the other 10%. The buyer is RFR Holding, a New York real estate company. Officials with Tishman and RFR did not immediately respond to a request for comments. It's unclear when the deal will close.
"""

data = {
        "ratio": 0.2,
        "data":text}

r = requests.post("http://127.0.0.1:8089/summarize_by_ratio", json = data)
print(r.text)


