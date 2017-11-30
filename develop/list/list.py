# This program is written in Python3

length = 6
value_list = [0, 1, 2, 3, 4, 5]
print(value_list)

def test(value_list, length):
	new_value = 299

	for i in range(length - 1):
		value_list[i] = value_list[i+1]

	value_list[length - 1] = new_value

	return value_list

print(test(value_list, length))
print(sum(value_list)/length)
