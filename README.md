This microservice provides functionality for findint the mode value in a list, as well as providing a list of all values and their frequency sorted by frequency.  

By default, the microservice runs on 127.0.0.1:6000, but this can be changed by modifying the URL and PORT constants in main.py  

Install required libraries by running "pip install -r requirements.txt" in a command prompt at the app's location.  

All requests are made as POST requests to the specified URL and path.
Include the list as JSON array with 'data' as the key as follows: {'data': list}  
No requests include query parameters.  
The response bodies are in JSON format as specified below each request.
<br>
<br>
<br>

Mode: Finds the mode value in a list.
POST to URL:PORT/mode/  
body: {'data': list}
response: {'value': [mode value(s)], 'frequency': # of appearances}  
notes: If a value is a list, every value in the list is considered.
If there are multiple modes, all are included in the 'value' list  
<br>

Frequency: Finds how often each unique value appears and sorts them in descending order by number of appearances.  
POST to URL:PORT/frequency/  
body: {'data': list}
response: [[value, # of appearences], [value, # of appearences], ...]
notes: If a value is a list, every value in that list is considered.
