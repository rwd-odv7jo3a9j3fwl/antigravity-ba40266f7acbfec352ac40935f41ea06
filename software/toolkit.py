import datetime, json
print(json.dumps({'toolkit': 'ok', 'utc': datetime.datetime.utcnow().isoformat()}))
