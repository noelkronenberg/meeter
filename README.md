# Meeter

A platform for meeting other students with similar interests. 

## Methodology 

Users have to enter general information about themselves. The algorithm will then process those inputs with keyword-based matching. The degree and general interests (in relation to the overlap) each account for 50% of the score. Finally, the three highest scoring other users will be presented to each user.

## Set-up

> You may try a demo version [here](http://noelkronenberg.pythonanywhere.com) (last commit: ce1db6d)

1. requirements: 
    - Python (tested: 3.9.10)
    - ```pip install -r requirements.txt```
2. start application: ```python3 app.py```
3. open application: http://127.0.0.1:5000
