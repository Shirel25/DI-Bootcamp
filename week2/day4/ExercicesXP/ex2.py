import json 

sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}

json_file = "ex2.json"

with open(json_file, 'w', encoding="utf-8") as jf:
    json.dump(sampleJson, jf, indent = 2) # write sampleJson into the ex2.json file
    
with open(json_file, 'r', encoding="utf-8") as jf:
    data = json.load(jf) # load the ex2.json data into a variable

print(f"salary : {data['company']['employee']['payable']['salary']}")

data['company']['employee']['birth_date'] = "2003-03-25"

with open(json_file, 'w', encoding="utf-8") as jf:
    json.dump(data, jf, indent = 2) # add the birth_date to the ex2.json file
    print("Birth date added successfully !") 

print(f"Dictionary saved successfully in {json_file} !")