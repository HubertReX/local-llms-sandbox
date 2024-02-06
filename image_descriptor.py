import ollama

# file_name = './old_soul.jpg'

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['./old_soul.jpg']
		}
	]
)

print(res['message']['content'])