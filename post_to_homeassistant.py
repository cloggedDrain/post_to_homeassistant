import requests
import sys
ha_url="http://<ha ip here>:8123"  # https is also supported
token="Long lived token goes here"


def main(argv):
    entity = sys.argv[1]
    state = sys.argv[2]
    service = entity.split('.')[0]
    print("Will set {0} to {1}".format(entity, state))
    url = '{0}/api/services/{1}/turn_{2}'.format(ha_url, service, state)
    payload = { "entity_id": entity }
    headers = {
        'Authorization': 'Bearer {0}'.format(token),
        'content-type': 'application/json',
    }
    r = requests.post(url, headers=headers, json=payload, verify=False)
    print("Return code: {0}".format(r.status_code))


if __name__ == "__main__":
    main(sys.argv[1:])
