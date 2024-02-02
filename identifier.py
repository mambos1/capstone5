import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def printRecord (ip):

     rec = gi.record_by_name(ip)

     city = rec['city']

     country = rec['country_name']

     longitude = rec['longitude']

     lat = rec['latitude']

     print('[+] Address: ' + ip + ' Geo-located ')

     print('[+] ' +str(city)+ ', ' + str(country))

     print('[+] Latitude: ' + str(lat) + ', Longitude: ' + str(longitude))

ip = input( 'Enter your IP: ' )

printRecord(ip)