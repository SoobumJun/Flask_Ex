import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
nextid = 0


def init(app):
    global entries, nextid
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())

        if int(entries[0]["postid"]) > nextid:
            nextid = int(entries[0]["postid"]) + 1
        f.close()

    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, nextid
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "postid": str(nextid)}
    entries.insert(0, entry) ## add to front of list
    nextid += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(postid):
    global entries, GUESTBOOK_ENTRIES_FILE, nextid
    pointer = {}
    for e in entries:
        if postid == e["postid"]:
            pointer = e
    entries.remove(pointer)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not re-write entries to file.")








