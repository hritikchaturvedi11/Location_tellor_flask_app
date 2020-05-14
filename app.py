from geocodio import GeocodioClient
client = GeocodioClient('e7da75f3ee9ab5dc5ec5eb557c91adffb5529e5')
geocoded_location = client.geocode("42370 Bob Hope Drive, Rancho Mirage CA")
print(f'{geocoded_location.coords}')

#get codinates
geocoded_addresses = client.geocode([
        '2 15th St NW, Washington, DC 20024',
        '3101 Patterson Ave, Richmond, VA, 23221'
    ])

print(f"{geocoded_addresses.coords}")
print(f"{geocoded_addresses[0].coords}")
print(f'{geocoded_addresses[1].coords}')

# get co-ordinates
cord = geocoded_addresses.get('2 15th St NW, Washington, DC 20024').coords
print(f'{cord}')

#parsing address
par = client.parse('1600 Pennsylvania Ave, Washington DC')
print(f'{par}')

#Find matching address

location = client.reverse((56.58, -15.40))
addre =  location.formatted_address
print(f'{addre}')

#Find multiple address
locations = client.reverse([
        (33.738987, -116.4083),
        (-33.738987, -1.511),
        (38.890083, -76.983822)
    ])
loca_multi = locations.formatted_addresses
print(f'{loca_multi}')

#Specific address from the tuple
speci_loc = locations.get("38.890083,-76.983822").formatted_address
print(f'{speci_loc}')


#by more natural key
natural_cord = locations.get((38.890083, -76.983822)).formatted_address
print(f'{natural_cord}')




from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def co_ordinates():
    title = "co_ordinates"
    cordi = geocoded_location.coords
    return render_template('index.html',title=title,cordi=cordi)

@app.route('/Cords_from_tupples')
def Cords_from_tupples():
    title = "Cords_from_tupples"
    cordi = geocoded_addresses[0].coords
    #co2 = "Cords from tupple"+geocoded_addresses[1].coords
    
    return render_template('about.html',title=title,cordi=cordi)

@app.route('/Address_from_cords')
def Address_from_cords():
    title = "Address_from_cords"
    cordi = locations.get("38.890083,-76.983822").formatted_address
    return render_template('contact.html',title=title,cordi=cordi)

''' cordi = location.formatted_address
    speci_loc = locations.get("38.890083,-76.983822").formatted_address
    natural_cord = locations.get((38.890083, -76.983822)).formatted_address
    '''

if __name__ == '__main__':
	app.run(debug = True, host = "0.0.0.0", port = 3000)

    
