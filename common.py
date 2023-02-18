#!/usr/bin/python3
# random functions that are used in multiple scripts

step_list = [
	"0 - raw",
	"1 - cropped",
	"2 - sorted",
	"3 - tagged",
	"4 - fixed",
	"5 - out",
]

class Image:
	"""class to store image attributes"""
	category = None
	filename = None
	path = None # full path to file
	txt = None # full path to file
	tags = []
	def __int__(self):
		return len(self.tags)
	def __str__(self):
		return f"{self.filename}"
	def __repr__(self):
		return f"{self.filename}"

class Tag:
	"""class to store tag attributes"""
	name = None
	position = 10
	def __str__(self):
		return f"{self.name}"
	def __repr__(self):
		return f"{self.name}"
	def __lt__(self, other):
         return self.position < other.position

# api cacher, "borrowed" from unknown project.
def api_cacher(api_base, api_url):
	"""cache api requests in '.cache' folder"""
	global use_cache
	if not os.path.exists('.cache') and use_cache:
		os.makedirs('.cache')

	filename = api_url.replace(api_base,'')
	filename = filename.replace('/','_')
	filename = filename.replace('?','_')
	filename = filename.replace('&','_')
	path = os.path.join('.cache',filename+'.json')

	if os.path.isfile(path) and use_cache:
		print('   cached', api_url)
		with open(path, 'r') as f:
			data_json = json.load(f)
	else:
		print('   request', api_url)
		# data = requests.get(api_url)
		# pretend to be chrome
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
		data = requests.get(api_url, headers={'User-Agent': user_agent})

		data.raise_for_status()
		data_json = data.json()
		time.sleep(1)
		with open(path, 'wb') as f:
			f.write(data.content)
	return data_json

# bootleg input verification
def verify_input(text,true,false,default=None):
	while true:
		i = input(text).lower()
		if i == true.lower():
			return True
		elif i == false.lower():
			return False
		elif default != None:
			return default
		else:
			print(f"Invalid input '{i}'\n")
