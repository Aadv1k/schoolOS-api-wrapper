import schoolos

# replace username and password with your credentials
so = schoolos.schoolOS("YOUR ECODE", "YOUR PWD", "SCHOOL GROUP")
print(type(so.get_timetable('2021-10-03', '2021-10-09')))

