from sys import int_info

info_string = 'Adam Ben Refael Hadera'
print('string length:', len(info_string))

print('in uppercase:', info_string.upper())
print('in lowercase:', info_string.lower())

print('string starts in first name:', info_string.startswith('Adam'))
print('string end in city name:', info_string.endswith('Hadera'))

print('break string to list:', info_string.split())

new_string = info_string.replace('', '*')
print('new string:', new_string)
print('break new string into list:', new_string.split('*'))

print(info_string.center(50, '$'))

print('4th char to end', info_string[3:])
print('start to 4th char', info_string[:4])

print('equal:', int_info[::2])

print('capital in every word:', info_string.title())


