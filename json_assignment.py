import json
with open(r"C:\Users\salvamol.km\Downloads\sample_data.json", "r") as file:
    content = json.load(file)

outer_list=[]
parameter_content=content["parametersList"]
for one in parameter_content:
    inner_dict={}
    inner_dict["parameterName"] = one["parameterName"]
    inner_dict["min"] = one["min"]
    inner_dict["max"] = one["max"]
    inner_dict["avg"] = one["avg"]
    outer_list.append(inner_dict)

print(outer_list)
with open(r"C:\Users\salvamol.km\Downloads\sample_data_out.json", "w") as file:
    json.dump(outer_list,file)