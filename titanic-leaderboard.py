# Format: id;survived
baseurl = "https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html"

groundtruthpacked = """
aWQ7c3Vydml2ZWQNCjU7MA0KMTA7MA0KMTU7MQ0KMjA7MA0KMjU7MQ0KMzA7MQ0KMzU7MA0KNDA7
MA0KNDU7MQ0KNTA7MQ0KNTU7MQ0KNjA7MQ0KNjU7MQ0KNzA7MQ0KNzU7MA0KODA7MQ0KODU7MA0K
OTA7MA0KOTU7MQ0KMTAwOzENCjEwNTsxDQoxMTA7MQ0KMTE1OzANCjEyMDsxDQoxMjU7MQ0KMTMw
OzENCjEzNTsxDQoxNDA7MQ0KMTQ1OzENCjE1MDsxDQoxNTU7MA0KMTYwOzENCjE2NTsxDQoxNzA7
MA0KMTc1OzANCjE4MDswDQoxODU7MA0KMTkwOzANCjE5NTswDQoyMDA7MQ0KMjA1OzENCjIxMDsx
DQoyMTU7MQ0KMjIwOzENCjIyNTswDQoyMzA7MQ0KMjM1OzANCjI0MDswDQoyNDU7MA0KMjUwOzEN
CjI1NTsxDQoyNjA7MQ0KMjY1OzENCjI3MDswDQoyNzU7MQ0KMjgwOzANCjI4NTsxDQoyOTA7MQ0K
Mjk1OzANCjMwMDswDQozMDU7MQ0KMzEwOzENCjMxNTsxDQozMjA7MQ0KMzI1OzENCjMzMDsxDQoz
MzU7MA0KMzQwOzENCjM0NTsxDQozNTA7MQ0KMzU1OzANCjM2MDsxDQozNjU7MA0KMzcwOzANCjM3
NTswDQozODA7MQ0KMzg1OzANCjM5MDswDQozOTU7MA0KNDAwOzANCjQwNTswDQo0MTA7MA0KNDE1
OzANCjQyMDswDQo0MjU7MA0KNDMwOzANCjQzNTsxDQo0NDA7MA0KNDQ1OzANCjQ1MDsxDQo0NTU7
MQ0KNDYwOzANCjQ2NTswDQo0NzA7MQ0KNDc1OzANCjQ4MDsxDQo0ODU7MQ0KNDkwOzENCjQ5NTsx
DQo1MDA7MA0KNTA1OzANCjUxMDswDQo1MTU7MQ0KNTIwOzANCjUyNTsxDQo1MzA7MQ0KNTM1OzEN
CjU0MDswDQo1NDU7MA0KNTUwOzENCjU1NTswDQo1NjA7MQ0KNTY1OzENCjU3MDswDQo1NzU7MA0K
NTgwOzANCjU4NTsxDQo1OTA7MQ0KNTk1OzANCjYwMDswDQo2MDU7MQ0KNjEwOzANCjYxNTswDQo2
MjA7MA0KNjI1OzANCjYzMDswDQo2MzU7MA0KNjQwOzANCjY0NTswDQo2NTA7MA0KNjU1OzANCjY2
MDsxDQo2NjU7MQ0KNjcwOzANCjY3NTsxDQo2ODA7MA0KNjg1OzANCjY5MDswDQo2OTU7MA0KNzAw
OzANCjcwNTswDQo3MTA7MQ0KNzE1OzENCjcyMDsxDQo3MjU7MA0KNzMwOzANCjczNTsxDQo3NDA7
MA0KNzQ1OzANCjc1MDswDQo3NTU7MA0KNzYwOzENCjc2NTswDQo3NzA7MA0KNzc1OzANCjc4MDsw
DQo3ODU7MA0KNzkwOzANCjc5NTsxDQo4MDA7MA0KODA1OzANCjgxMDswDQo4MTU7MA0KODIwOzEN
CjgyNTswDQo4MzA7MA0KODM1OzANCjg0MDswDQo4NDU7MA0KODUwOzANCjg1NTswDQo4NjA7MA0K
ODY1OzANCjg3MDswDQo4NzU7MQ0KODgwOzANCjg4NTswDQo4OTA7MQ0KODk1OzENCjkwMDsxDQo5
MDU7MA0KOTEwOzENCjkxNTswDQo5MjA7MA0KOTI1OzANCjkzMDswDQo5MzU7MQ0KOTQwOzANCjk0
NTswDQo5NTA7MQ0KOTU1OzANCjk2MDswDQo5NjU7MA0KOTcwOzANCjk3NTswDQo5ODA7MA0KOTg1
OzENCjk5MDswDQo5OTU7MA0KMTAwMDsxDQoxMDA1OzENCjEwMTA7MA0KMTAxNTswDQoxMDIwOzAN
CjEwMjU7MA0KMTAzMDswDQoxMDM1OzENCjEwNDA7MQ0KMTA0NTsxDQoxMDUwOzENCjEwNTU7MA0K
MTA2MDswDQoxMDY1OzENCjEwNzA7MA0KMTA3NTswDQoxMDgwOzENCjEwODU7MA0KMTA5MDswDQox
MDk1OzENCjExMDA7MA0KMTEwNTswDQoxMTEwOzANCjExMTU7MA0KMTEyMDswDQoxMTI1OzANCjEx
MzA7MA0KMTEzNTswDQoxMTQwOzANCjExNDU7MA0KMTE1MDsxDQoxMTU1OzANCjExNjA7MQ0KMTE2
NTswDQoxMTcwOzANCjExNzU7MA0KMTE4MDswDQoxMTg1OzANCjExOTA7MQ0KMTE5NTswDQoxMjAw
OzANCjEyMDU7MA0KMTIxMDswDQoxMjE1OzANCjEyMjA7MA0KMTIyNTswDQoxMjMwOzANCjEyMzU7
MA0KMTI0MDswDQoxMjQ1OzENCjEyNTA7MA0KMTI1NTsxDQoxMjYwOzANCjEyNjU7MA0KMTI3MDsw
DQoxMjc1OzANCjEyODA7MA0KMTI4NTswDQoxMjkwOzANCjEyOTU7MA0KMTMwMDswDQoxMzA1OzAN
Cg==
"""

import csv

def readleaderboard():
    try:
        f = open("/tmp/leaderboard.csv")
    except:
        return {}
    csv_file_object = csv.reader(f)
    data = {}
    for row in csv_file_object:
        data[row[0]] = row[1]
    return data

def readscores(filename_or_string, asstring=True):
    if asstring:
        f = filename_or_string.split("\n")
    else:
        f = open(filename_or_string, "r")
    csv_file_object = csv.reader(f, delimiter=';')
    header = csv_file_object.__next__()
    data = {}
    for row in csv_file_object:
        if row:
            data[row[0]] = row[1]
    return data

def calculatescore(data_gt, data_sub):
    if len(data_gt) > len(data_sub):
        rights = 0
        for k in data_sub:
            if k in data_gt and data_sub[k] == data_gt[k]:
                rights += 1
    else:
        rights = sum([1 if x[1] == y[1] else 0 for x, y in zip(data_gt.items(), data_sub.items())])

    return rights / len(data_sub)

def calculatescorewrapper(data_sub):
    import base64
    groundtruthunpacked = base64.decodebytes(bytes(groundtruthpacked, "utf-8")).decode("utf-8")
    data_gt = readscores(groundtruthunpacked, True)
    return calculatescore(data_gt, data_sub)

def main(dict):
    if not "csv" in dict:
        title = "Titanic submission"
        body = "<form action='{}' method='post'>Your submission name+id:<br><input type='text' name='submission'><br>Paste your CSV:<br><textarea name='csv'>key;value</textarea><br><input type='submit' value='Send'></form>".format(baseurl)
    else:
        data_sub = readscores(dict["csv"], True)
        score = calculatescore(data_sub)

        if "submission" in dict and dict["submission"]:
            submission = dict["submission"]
        else:
            submission = "anonymous"
        f = open("/tmp/leaderboard.csv", "a")
        print("{},{}".format(submission.replace(",", ";"), score), file=f)
        f.close()

        leaderboard = readleaderboard()
        leaderboard = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)
        leaderboardstr = ""
        for pos, (name, score) in enumerate(leaderboard, 1):
            leaderboardstr += "{}: {} → {}<br>".format(pos, name, score)

        title = "Titanic leaderboard"
        body = "Leaderboard!<br>" + leaderboardstr
    html = "<html><title>{}</title><body>{}</body></html>".format(title, body)
    return {"headers": {"Content-Type": "text/html"}, "statusCode": 200, "html": html}

if __name__ == "__main__":
    import sys
    data_sub = readscores(sys.argv[1], asstring=False)
    score = calculatescorewrapper(data_sub)
    print(score)
