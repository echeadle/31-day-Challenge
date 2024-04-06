import json

data = { 
	"name": "Satyam kumar", 
	"place": "patna", 
	"skills": [ 
		"Raspberry pi", 
		"Machine Learning", 
		"Web Development"
	], 
	"email": "xyz@gmail.com", 
	"projects": [ 
		"Python Data Mining", 
		"Python Data Science"
	] 
} 
with open( "data_file.json" , "w" ) as write: 
	json.dump( data , write ) 

# JSON string: 
# Multi-line string 
data = """{ 
	"Name": "Jennifer Smith", 
	"Contact Number": 7867567898, 
	"Email": "jen123@gmail.com", 
	"Hobbies":["Reading", "Sketching", "Horse Riding"] 
	}"""
	
# parse data: 
res = json.loads( data ) 
	
# the result is a Python dictionary: 
print( res )


# Read JSON data from the file
with open("/home/echeadle/Autogen/31-day-Challenge/day_20_quiz_creator/question-1712115024.json", 'r') as json_file:
    json_data = json.loads(json_file)

print(json_data)


