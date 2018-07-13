import requests
import uuid
import json

baseurl = "https://openwhisk.eu-de.bluemix.net/api/v1/web/SPLab_ESSCA18/default/esscacfp.html"

# Cloudant: ...
cred = {
  "username": "...",
  "password": "...",
  "host": "...",
  "port": 443,
  "url": "...",
}

tmpl_header = """
    <img src='http://essca2018.servicelaboratory.ch/essca2018-logo.png'>

    <p>
    <b>ESSCA 2018 CfP: Industry/community talk proposals</b> [via esscacfp cloud function - <a href='https://github.com/serviceprototypinglab/functions-collection/blob/master/esscacfp.py'>fork on Github</a>]
    </p>
"""

tmpl_call = tmpl_header + """
    <p>
    Hello! We'd like to have you as speaker in <a href='http://essca2018.servicelaboratory.ch/'>ESSCA 2018</a> on December 21st in Zurich.
    Please provide us information about the talk or demo you want to give. We will review all proposals and come back to you within a few days.
    </p>

    <form action='{}' method='post'>
    Your name:<br><input type='text' name='name' size='40'><br>
    Affiliation:<br><input type='text' name='affiliation' size='40'><br>
    E-mail address:<br><input type='text' name='email' size='40'><br>
    Talk title:<br><input type='text' name='title' size='40'><br>
    Talk description:<br><textarea name='description' cols='45' rows='10'></textarea><br>
    Preferred duration in minutes (e.g. 15, 30, 45):<br><input type='text' name='duration' size='40'><br>
    Any comments, references to previous talks, questions:<br><textarea name='comments' cols='45' rows='10'></textarea><br>
    <input type='submit' value='Send talk proposal'></form>
"""

tmpl_resp = tmpl_header + """
    <p>
    Thank you for submitting the proposal. You'll hear from us soon.
    </p>
"""

def main(dict):
    url = "https://{}:{}@{}".format(cred["username"], cred["password"], cred["host"])

    if not "email" in dict:
        title = "ESSCA 2018 CfP: Industry/community talk proposals"
        body = tmpl_call.format(baseurl)
    else:
        data = {}
        for kw in ("name", "affiliation", "email", "title", "description", "duration", "comments"):
          data[kw] = dict[kw]
        requests.put(url + "/esscadb")
        docid = str(uuid.uuid4())
        requests.put(url + "/esscadb/" + docid, json.dumps(data))

        title = "ESSCA 2018 talk proposal"
        body = tmpl_resp
    html = "<html><title>{}</title><body>{}</body></html>".format(title, body)
    return {"headers": {"Content-Type": "text/html"}, "statusCode": 200, "html": html}
