# TopprOSApiWrapper

A minimal (unofficial) wrapper for ```https://ryangroup.toppr.school```, might work with other SchoolOS sites too. 

## Installation 

```
git clone https://github.com/aadv1k/SchoolosWrapper`
cd SchoolosWrapper
```

You need python 3.9 for this to work

```
pip install -r requirements.txt
python test-script.py
```

### Usage

 ```get_token(cookie)```
Requires a cookie(```String```), which can be found by tapping the ```__cf_bm``` and ```admin_sessionId``` 
Also required as an input to all the other functions, fetches a token writes it to ```jwt_token.json```, 
reads it from there as long as the token is working, a new file will be generated if the file is corrupted 
or nor present in the directory.


```get_timetable(cookie, token, start, end)```
Gets the timetable view, takes a start and an end date, both of the dates need to be in the format of ```yyyy-mm-dd```  
and the date needs to be of Sunday-Saturday else it won't work. 


 ```get_assignments(token, complete=bool, quantity=int)```
Gets the assignments, by default gives out incomplete assignments, with a view set to 5, in order to change 
it you can set the ```complete=True```  to get the completed assignment and ```quantity=10```
to get more than five assignments, note that the input can only be a multiple of 5, anything else wont work.

### Instructions on how to get the cookie
<details>
 <summary></summary>
 
 Head on to <a href="https://ryangroup.toppr.school" target="_blank">SchoolOS</a>

press <kbd>ctrl+shift+i</kbd> to open the developer console, and head on over
to the network tab

Now, login, once you are on the timetable tab, search for ```get-jwt-token``` in the search bar

Click on the result, and find the header ```cookie```, copy the text, and paste
it in the ```test-script.py```

</details>

