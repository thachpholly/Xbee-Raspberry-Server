
def sent_data(mechanize, WEBSERVICE_IP, WEBSERVICE_PORT, FORM_INPUT_PATH, data):
	br=mechanize.Browser()
	br.open('http://localhost:55555/demo_websocket/form.html')
	br.select_form(nr=0) #check yoursite forms to match the correct number
	print br['data']
	br['data']='Username' #use the proper input type=text name
	br.submit()
#br.retrieve('https://www.yourfavoritesite.com/pagetoretrieve.html','yourfavoritepage.html')
