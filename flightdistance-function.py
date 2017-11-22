import csv
import math
import os
import urllib.request
import zipfile
import tempfile
import time
import hashlib
import http.cookiejar
import sys
import getpass

def printdebug(*s):
	print(*s)

def login(opener, user, password):
	f = opener.open("https://openflights.org/php/map.php")
	s = f.read(100).decode("utf-8").split(";")
	challenge = s[7].split("\n")[0]
	pwuser = hashlib.md5(bytes(password + user.lower(), "utf-8")).hexdigest()
	lpwuser = hashlib.md5(bytes(password + user, "utf-8")).hexdigest()
	pw = hashlib.md5(bytes(challenge + pwuser, "utf-8")).hexdigest()
	lpw = hashlib.md5(bytes(challenge + lpwuser, "utf-8")).hexdigest()
	logurl = "https://openflights.org/php/login.php"
	logdata = "name={}&pw={}&lpw={}&challenge={}".format(user, pw, lpw, challenge)
	f = opener.open(logurl, data=bytes(logdata, "utf-8"))

def download():
	airportdb = "http://www.partow.net/downloads/GlobalAirportDatabase.zip"
	cachepath = "/tmp/GlobalAirportDatabase.txt"
	if os.path.isfile(cachepath):
		if time.time() - os.path.getmtime(cachepath) > 300:
			printdebug("Invalidate cache")
			os.unlink(cachepath)
	if not os.path.isfile(cachepath):
		printdebug("File cache from source")
		ziplink = urllib.request.urlopen(airportdb)
		f = tempfile.NamedTemporaryFile()
		f.write(ziplink.read())
		f.flush()
		zipf = zipfile.ZipFile(f.name)
		gad = zipf.open("GlobalAirportDatabase.txt")
		txt = gad.read()
		f = open(cachepath, "wb")
		f.write(txt)
		f.close()
	return cachepath

def loadairports(cachepath):
	airdb = {}
	r = csv.reader(open(cachepath), delimiter=":")
	for airport in r:
		airdb[airport[1]] = float(airport[14]), float(airport[15])
	return airdb

def loadbackup(opener):
	backupcsv = "https://openflights.org/php/flights.php?export=backup"
	backuplink = opener.open(backupcsv)
	backupdata = backuplink.read().decode("utf-8")
	if backupdata.startswith("You must be logged in"):
		raise Exception("Unauthorised. Log into openflights.org first.")
	return backupdata

def calculatedistance(airdb, backupdata):
	count = 0
	skip = 0
	alldistance = 0.0
	r = csv.reader(backupdata.split("\n"))
	r.__next__()
	for flight in r:
		origin, destination = flight[1], flight[2]
		origpos = None
		destpos = None
		if origin in airdb:
			origpos = airdb[origin]
		if destination in airdb:
			destpos = airdb[destination]
		if origpos and destpos and abs(origpos[0]) > 0.01 and abs(destpos[0]) > 0.01:
			x1 = math.radians(origpos[0])
			y1 = math.radians(origpos[1])
			x2 = math.radians(destpos[0])
			y2 = math.radians(destpos[1])
			distance = math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y2-y1))*6378.137
			count += 1
			alldistance += distance
		else:
			skip += 1
	return count, skip, alldistance

def flightdistance(user, password):
	"""
	Calculcates the overall flight distance between all identified airports in an OpenFlights account.
	Requires the account credentials (user, password) as parameters.
	Returns a tuple with the distance in km and the percentage of covered flights.
	"""
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	printdebug("Logging in...")
	login(opener, user, password)
	printdebug("Loading airports...")
	cachepath = download()
	airdb = loadairports(cachepath)
	printdebug("{} airports loaded.".format(len(airdb)))
	printdebug("Loading backup...")
	backupdata = loadbackup(opener)
	printdebug("{} flights loaded.".format(len(backupdata.split("\n"))))
	count, skip, alldistance = calculatedistance(airdb, backupdata)
	coverage = 100 * count / (count + skip)
	printdebug("{} distances determined ({}%). Overall distance {} km.".format(count, coverage, alldistance))
	return alldistance, coverage

def getcredentials():
	"""
	Takes user, password pair from command line or alternatively asks for it.
	"""
	if len(sys.argv) > 1:
		user = sys.argv[1]
	else:
		user = input("Openflights username? ")
	if len(sys.argv) > 2:
		password = sys.argv[2]
	else:
		password = getpass.getpass("Openflights password (*** not shown)? ")
	return user, password

def lambda_handler(event, context):
	"""
	AWS Lambda entry point.
	"""
	return flightdistance(event["user"], event["password"])

def main(dict):
	"""
	OpenWhisk entry point.
	"""
	return {"distance": flightdistance(dict["user"], dict["password"])}

if __name__ == "__main__":
	# Command line entry point.
	user, password = getcredentials()
	flightdistance(user, password)
