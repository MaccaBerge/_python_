import requests


# https://discord.com/api/v9/channels/536607785862037524/messages

payload = {
    'content': 'BØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\nBØ\n',
    }

header = {
    'authorization': 'NTQxNTc4NjIyNTExNzQyOTc3.Yi98lg.rVIT_OmSqahC4zyI4Eo26diGytw'
    }


while True:
    r = requests.post('https://discord.com/api/v9/channels/953362943062446131/messages', data=payload, headers=header)