import schoolOS

# replace username and password with your credentials
so = schoolOS.schoolOS('username', 'password')
print(so.get_timetable('2021-10-03', '2021-10-09'))
