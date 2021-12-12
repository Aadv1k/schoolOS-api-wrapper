# SchoolOS-api-wrapper

An unofficial wrapper made for `https://ryangroup.toppr.school`, it might work with other sites based on schoolOS too

## Installation

```bash
git clone https://github.com/aadv1k/schoolos-wrapper.git
cd schoolos-wrapper
pip install -r requirements.txt
```

Then, you can either import `schoolOS` or put your credentials in `example.py` and run it directly from there.

**This app is tested with python 3.6 (and above)**

## Usage

## Initialization 
To use the functions provided below, you must initialize the app with your credentials, which can be done like so
```python
import schoolos
s = schoolos.schoolOS('YOUR USERNAME', 'YOUR PASSWORD')
```

`get_timetable(start, end)`
Gets the weekly classes, takes a start and an end date, both of which need to be in the format of `yyyy-mm-dd`
and the date needs to be of Sunday-Saturday else it won't work; Returns raw json data.

`get_assignments(complete=bool, quantity=int)`
Gets the assignments, by default gives out incomplete assignments, with a view set to 5, in order to change
it you can set the `complete=True` to get the completed assignment and `quantity=10`
to get more than five assignments, note that the input can only be a multiple of 5, anything else wont work.
