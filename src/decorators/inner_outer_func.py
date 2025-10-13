def outer_func():
	value = 1
	def inner_func():
		print(f"{value}")
	return inner_func

if __name__ == "__main__":
	inner_func = outer_func()
	inner_func()
