class mutable_string:
	def __init__(self, string = ""):
		self.m_Characters = list(string)

	"""
		Make it easier to get and modify the string
	"""
	def get_string(self):
		return ''.join(self.m_Characters)

	def set_string(self, string):
		string = str(string)

		self.m_Characters = list(string)

		return self.get_string()

	"""
		Overload default operators to replicate
		default behavior
	"""
	def __getitem__(self, key):
		return self.m_Characters[key]

	def __setitem__(self, key, value):
		self.m_Characters[key] = str(value)[0]

	def __getslice__(self, start, end):
		return self.m_Characters[max(0, start):max(0, end)]

	def __str__(self):
		return self.get_string()

	def __repr__(self):
		return self.get_string()

	def __unicode__(self):
		return self.get_string()

	def __add__(self, other):
		return self.get_string() + str(other)

	def __iadd__(self, other):
		return self.set_string(self.__add__(other))

	def __mul__(self, other):
		return self.get_string() * other

	def __imul__(self, other):
		return self.set_string(self.__mul__(other))

	def __lt__(self, other):
		return self.get_string() < str(other)

	def __gt__(self, other):
		return self.get_string() > str(other)

	def __le__(self, other):
		return self.get_string() <= str(other)

	def __ge__(self, other):
		return self.get_string() >= str(other)

	def __eq__(self, other):
		return self.get_string() == str(other)

	def __ne__(self, other):
		return self.get_string() != str(other)

	"""
		Re-create default string functions
	"""
	def replace(self, old, new):
		self.set_string(self.get_string().replace(old, new))

	def strip(self):
		self.set_string(self.get_string().strip())

	def lstrip(self):
		self.set_string(self.get_string().lstrip())

	def rstrip(self):
		self.set_string(self.get_string().rstrip())