import requests
import uuid
import json

baseurl = "https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/icdcstutorial.html"

# Cloudant: https://888536f4-064e-4bd7-b7a6-f710585ea5b6-bluemix.cloudant.com/dashboard.html
cred = {
  "username": "...",
  "password": "...",
  "host": "...",
  "port": 443,
  "url": "..."
}

def main(dict):
    url = "https://{}:{}@{}".format(cred["username"], cred["password"], cred["host"])

    if not "email" in dict:
        title = "Tutorial registration"
        body = """
        <form action='{}' method='post'>
        Your name:<br><input type='text' name='name'><br>
        Affiliation:<br><input type='text' name='affiliation'><br>
        E-mail address:<br><input type='text' name='email'><br>
        Interest:<br><textarea name='interests'></textarea><br>
        <input type='submit' value='Send info'></form>
        """.format(baseurl)
    else:
        data = {}
        data["name"] = dict["name"]
        data["affiliation"] = dict["affiliation"]
        data["email"] = dict["email"]
        data["interests"] = dict["interests"]
        requests.put(url + "/icdcsdb")
        docid = str(uuid.uuid4())
        requests.put(url + "/icdcsdb/" + docid, json.dumps(data))

        title = "Tutorial registration"
        body = "Thank you for your registration. GDPR regulations may apply."
    html = "<html><title>{}</title><body>{}</body></html>".format(title, body)
    return {"headers": {"Content-Type": "text/html"}, "statusCode": 200, "html": html}
