def my_decorator(f):
	def wrapper():
		print("Before function")
		f()
		print("After function")
	return wrapper


@my_decorator
def execute_task():
	print("Executing task…")


if __name__ == "__main__":
	execute_task().