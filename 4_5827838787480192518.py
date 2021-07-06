#seyed ali hossieni
#mohammad hossieni givKashi
#mohammad hossieni farzanegan

sub_code = []
f = open("input.txt","r")
table = []

lines = f.readlines();
i = 0
while i < len(lines) :
	l = lines[i]
	index = l.find(":")
	if index > 0 :
		div = l.split(":")
		sub_code.append([div[0],div[1]])
	elif index < 0 :
		sub_code.append(["",l])
	i = i + 1

f.close()
counter = 0;

while counter < len(sub_code):
	line = sub_code[counter]
	one_line= line[1]
	
	if one_line.find("MOV") >= 0 :
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		v = div[2].replace('\n','')
		flag = False
		for col in table:
			if col[0] == v:
				col[1] = int(div[0])
				flag = True
		if flag == False:
			table.append([v,int(div[0])])
	
	if one_line.find("JMPF") >= 0:
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		lable = div[2].replace('\n','')
		check = div[0]
		count = 0
		for col in table:
			if col[0] == check and col[1] == 0:
				for l in sub_code:
					if l[0] == lable:
						counter = count - 1
					count = count + 1
	
	if one_line.find("JMP") >= 0:
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		lable = div[2].replace('\n','')
		check = div[0]
		count = 0
		for col in table:
			if col[0] == check and col[1] == 1:
				for l in sub_code:
					if l[0] == lable:
						counter = count - 1
					count = count + 1
	
	
					
	if one_line.find("ADD") >= 0 :
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		t1=div[0]
		t2=div[1]
		v = div[2].replace('\n','')
		flag = False
		f1=False
		f2=False
		if len(table)==0:
			a = int(t1)
			b = int(t2)
		for col in table:
			if col[0]==t1:
				a = col[1]
				f1=True
		if f1==False:
			a = int(t1)
		for col in table:
			if col[0]==t2:
				b = col[1]
				f2=True
		if f2==False:
			b = int(t2)
		for col in table:
			if col[0] == v:
				col[1] = a+b
				flag = True
		if flag == False:
			table.append([v,a+b])

	if one_line.find("SUB") >= 0 :
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		t1=div[0]
		t2=div[1]
		v = div[2].replace('\n','')
		flag = False
		f1=False
		f2=False
		if len(table)==0:
			a = int(t1)
			b = int(t2)
		for col in table:
			if col[0]==t1:
				a=col[1]
				f1=True
		if f1==False:
			a=int(t1)
		for col in table:
			if col[0]==t2:
				b=col[1]
				f2=True
		if f2==False:
			b=int(t2)
		for col in table:
			if col[0] == v:
				col[1] = a-b
				flag = True
		if flag == False:
			table.append([v,a-b])

	if one_line.find("MUL") >= 0 :
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		t1=div[0]
		t2=div[1]
		v = div[2].replace('\n','')
		flag = False
		f1=False
		f2=False
		if len(table)==0:
			a = int(t1)
			b=int(t2)
		for col in table:
			if col[0]==t1:
				a=col[1]
				f1=True
		if f1==False:
			a=int(t1)
		for col in table:
			if col[0]==t2:
				b=col[1]
				f2=True
		if f2==False:
			b=int(t2)
		for col in table:
			if col[0] == v:
				col[1] = a*b
				flag = True
		if flag == False:
			table.append([v,a*b])


	if one_line.find("POW") >= 0 :
		div_temp = one_line.split(" ")
		div = div_temp[1].split(",")
		t1=div[0]
		t2=div[1]
		v = div[2].replace('\n','')
		flag = False
		f1=False
		f2=False
		if len(table)==0:
			a = int(t1)
			b=int(t2)
		for col in table:
			if col[0]==t1:
				a=col[1]
				f1=True
		if f1==False:
			a=int(t1)
		for col in table:
			if col[0]==t2:
				b=col[1]
				f2=True
		if f2==False:
			b=int(t2)
		
		for i in range(b):
			a=a*b
		res=a
			
		for col in table:
			if col[0] == v:
				col[1] = res
				flag = True
		if flag == False:
			table.append([v,res])
	
			
	if one_line.find("PRINT")>=0:
		t1=one_line.split(" ")
		t1[1]=t1[1].replace('\n','')
		for ta in table:
			if ta[0]==t1[1]:
				print(ta[1])
				break
		
	if one_line.find("EQ")>=0:
		t1=one_line.split(" ")
		t2=t1[1].split(",")
		t2[2]=t2[2].replace('\n','')
		key=0
		bol=0
		for ta1 in table:
			if ta1[0]==t2[0]:
				for ta2 in table:
					if ta2[0]==t2[1]:
						if ta1[1]==ta2[1]:
							bol=1
						else:
							bol=0
		for ta in table:
			if ta[0]==t2[2]:
				ta[1]=bol
				key=1
				break
		if key==0:
			table.append([t2[2],bol])
		
	if one_line.find("LT")>=0:
		t1=one_line.split(" ")
		t2=t1[1].split(",")
		t2[2]=t2[2].replace('\n','')
		key=0
		bol=0
		for ta1 in table:
			if ta1[0]==t2[0]:
				for ta2 in table:
					if ta2[0]==t2[1]:
						if ta1[1]<ta2[1]:
							bol=1
						else:
							bol=0
		for ta in table:
			if ta[0]==t2[2]:
				ta[1]=bol
				key=1
				break
		if key==0:
			table.append([t2[2],bol])

	if one_line.find("NEQ")>=0:
		t1=one_line.split(" ")
		t2=t1[1].split(",")
		t2[2]=t2[2].replace('\n','')
		key=0
		bol=0
		for ta1 in table:
			if ta1[0]==t2[0]:
				for ta2 in table:
					if ta2[0]==t2[1]:
						if ta1[1]==ta2[1]:
							bol=0
						else:
							bol=1
		for ta in table:
			if ta[0]==t2[2]:
				ta[1]=bol
				key=1
				break
		if key==0:
			table.append([t2[2],bol])
		
	if one_line.find("GT")>=0:
		t1=one_line.split(" ")
		t2=t1[1].split(",")
		t2[2]=t2[2].replace('\n','')
		key=0
		bol=0
		for ta1 in table:
			if ta1[0]==t2[0]:
				for ta2 in table:
					if ta2[0]==t2[1]:
						if ta1[1]>ta2[1]:
							bol=1
						else:
							bol=0
		for ta in table:
			if ta[0]==t2[2]:
				ta[1]=bol
				key=1
				break
		if key==0:
			table.append([t2[2],bol])
	if one_line.find("DIV")>=0:
		t1=one_line.split(" ")
		t2=t1[1].split(",")
		t2[2]=t2[2].replace('\n','')
		key=0
		bol=0
		div=0
		flag1=0
		flag2=0
		a=0
		b=0
		for ta1 in table:
			if ta1[0]==t2[0]:
				flag1=1
				a=ta1[1]
				for ta2 in table:
					if ta2[0]==t2[1]:
						flag2=1
						b=ta2[1]
		if flag1==0:
			a=int(t2[0])
		if flag2==0:
			b=int(t2[1])
		div=a/b
		for ta in table:
			if ta[0]==t2[2]:
				ta[1]=div
				key=1
				break
		if key==0:
			table.append([t2[2],div])
		
	counter = counter + 1
	
print('\n'+"table:"+'\n')	
print(table)		
