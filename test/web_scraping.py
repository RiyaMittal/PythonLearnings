import requests
import bs4


def print_json_data(list_data,list_type):
	print("\n Here is the listing of {}".format(list_type))
	for items in list_data:
		print(items)
		
	#download the web page= get the response object from the site	
resp=requests.get('https://www.gutenberg.org/catalog/')
try:
     resp.raise_for_status()
except Exception as ex:
        print("Seems like there is a problem: %s" %(ex))
print("\nyou should see 200 as status code")
print(resp.status_code)

        # create a beautifulSoup object from text object of response object

gut_soup=bs4.BeautifulSoup(resp.text,"html.parser")

        #put all CSS elements named <input> that have  a name attribute  with any value
elems=gut_soup.select('input[name]')

print("\nthere are {} elements of type '<input>[name]'".format(len(elems)))

for items in elems:
        print(items)

print("\ncheck the class of one of the elements")
print(type(elems[2]))

print("\ncheck the attributes of one of the elements")
for items in elems:
        print(items.attrs)
