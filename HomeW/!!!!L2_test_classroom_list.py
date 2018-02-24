quest = input('По какому классу вывести оценки? ')
school = [
			{'class':[
						{'1':[
								{'a':[1, 3, 4, 4, 3, 5, 3], 
                             	 'b':[1, 2, 4, 4, 3, 4, 4],
                             	 'c':[1, 2, 2, 5, 4, 5, 5]
                            	} 
                             ],
                    	 '2':[{'a':[2, 3, 3, 4, 3, 5, 3], 
                           	   'b':[1, 2, 4, 4, 4, 4, 4],
                           	   'c':[1, 3, 2, 5, 4, 4, 2]
                           	   }
                           	 ]
                        }
                     ]
            }
        ]
if quest == '2':
	a = school[0]['class'][0]['2'][0]['a']
	b = school[0]['class'][0]['2'][0]['b']
	c = school[0]['class'][0]['2'][0]['c']
		
	#for score in a, b ,c:
	for score in a:
# print(school[0]['class'][0]['2'][0]) #- как вывести значение по ключам списка в списке?
		print(score)
#	for score in b:
#		print(score)
#	for score in c:
#		print(score)
	sum(i for i in a)
	print(sum)

#if quest = '2':
#	for score in school[0]['class'][0]['2'][0]:
#		print(score)

#school_clsss = [{'school_class':'a'}]

# school = [{'class':[{'1':[{'a':[записать переменную с формулой подсчета оценок]','2','3','4','5'}]