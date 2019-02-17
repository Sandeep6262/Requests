def requests_fuction_api():
	import requests
	import json
	var = requests.get("http://saral.navgurukul.org/api/courses")
	# print(var)
	data = var.json()
	## print(data)

	with open("courses.json","w") as file_name:
		json.dump(data,file_name)

	with open("courses.json","r") as file_name:
		add=json.load(file_name)
	# print(add)
	new_list = []
	id_list = []
	number = 1
	for i in add:
		# prin(i)
		for j in add[i]:
			# print(j)
			print(number,j["name"])
			new_list.append(number)
			id_list.append(j["id"])
			number+=1
	print('')

	# # print(new_list)
	# # print(id_list)

	user=int(input("any number you want chek course "))
	print('')
	list_slug = []

	number_slug=[]
	number_ca_s =1
	for i in range(len(new_list)):
		if new_list[i] == user:
			y=id_list[i]
			# print(y)
			link_id = requests.get(" http://saral.navgurukul.org/api/courses/"+str(y)+"/exercises")
			# print(link_id)
			sec_data = link_id.json()
			# print(sec_data)

			for i in sec_data:
				# print(i)
				number=1
				for j in sec_data[i]:
					# print(j)
					# print(j["slug"])
					list_slug.append(j["slug"])
					number_slug.append(number_ca_s)
					number_ca_s+=1
					# print(number,j["name"])
					number+=1
					a=j["childExercises"]
					# print(a)
					for k in a:
						# print(k["slug"])
						list_slug.append(k["slug"])
						number_slug.append(number_ca_s)
						number_ca_s+=1
						print('	',number,k["name"])
						number+=1

	# print(list_slug)
	# print(number_slug)
	chuse=int(input("input any number you want open content "))
	for i in range(len(number_slug)):
		if number_slug[i] == chuse:
			b_slug = list_slug[i]
			print(b_slug)
			new_var= requests.get("http://saral.navgurukul.org/api/courses/"+str(y)+"/exercise/getBySlug?slug="+str(b_slug))
			third_data = new_var.json()
			print('')
			print('')
			# print(third_data)
			print(third_data["content"])
			
requests_fuction_api()