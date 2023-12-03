def add_time(start_time, duration, starting_day_of_week=None):
    # Parse the start time into hours and minutes
    start_time_parts = start_time.split(':')
    start_hours = int(start_time_parts[0])
    start_minutes = int(start_time_parts[1][:2])
    start_am_pm = start_time_parts[1][2:].strip()
    
    # Parse the duration into hours and minutes
    duration_parts = duration.split(':')
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    # Convert start time to 24hr format
    if start_am_pm == 'PM' and start_hours != 12:
        start_hours += 12
    elif start_am_pm == 'AM' and start_hours == 12:
        start_hours = 0

    # Add the duration to the start time
    end_hours = start_hours + duration_hours
    end_minutes = start_minutes + duration_minutes

    # If the end minutes are greater than 60, add the extra minutes to the end hours
    if end_minutes >= 60:
        end_hours += 1
        end_minutes -= 60

    # Convert hours to days if necessary
    if end_hours >= 24:
        end_days = end_hours // 24
        end_hours = end_hours % 24
    else:
        end_days = 0
    
    # Determine AM or PM
    if end_hours - 24 == 0:
        end_am_pm = 'AM'
        end_hours = 12
    elif end_hours == 12:
        end_hours = 12
        end_am_pm = 'PM'
    elif end_hours > 12:
        end_am_pm = 'PM'
        end_hours = end_hours - 12
    elif end_hours == 0:
        end_hours = 12
        end_am_pm = 'AM'
    else:
        end_am_pm = 'AM'
    
    # Set end time
    end_time = f'{end_hours}:{end_minutes:02d} {end_am_pm}'

    # Calculate day
    # If the starting day of the week is given, format it for the output
    if starting_day_of_week:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        index = days_of_week.index(starting_day_of_week.capitalize())
        index = (index + end_days) % 7
        starting_day_of_week = days_of_week[index].capitalize()
        output = f'{end_time}, {starting_day_of_week}'
    else:
        output = end_time
  
    # If the number of days difference is 1, add '(next day)' to the output
    if end_days == 1:
        output += ' (next day)'
    # If the number of days difference is greater than 1, add '(n days later)' to the output
    elif end_days > 1:
        output += f' ({end_days} days later)'

    return output