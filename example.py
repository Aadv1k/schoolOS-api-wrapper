import schoolos

# replace username and password with your credentials
so = schoolos.schoolOS("YOUR ECODE", "YOUR PASSWORD")
print(so.get_timetable('2021-10-03', '2021-10-09'))
