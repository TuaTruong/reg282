from gologin import GoLogin
from random import randint

gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzVhMDRmYmY5Y2FjZTE1NThlNWIxOGMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzVhMDUwZDhmNjdlN2I3NGZiOGNkOGYifQ.BHOEimvInQuW2NcIwNyqt6-Kip92JzgSU7X8Y4sD7jE",
	})

profile_id = gl.create({
    "name": f'{randint(100000000,999999999999999999999)}',
    "os": 'win',
    "navigator": {
        "language": 'en-US',
        "userAgent": 'random', # Your userAgent (if you don't want to change, leave it at 'random')
        "resolution": 'random', # Your resolution (if you want a random resolution - set it to 'random')
        "platform": 'win',
    },
    'proxyEnabled': False, # Specify 'false' if not using proxy
    'proxy': {
        'mode': 'none',
    },
    "webRTC": {
        "mode": "alerted",
        "enabled": True,
    },
});

print('profile id=', profile_id);

# gl.update({
#     "id": 'yU0Pr0f1leiD',
#     "name": 'profile_mac2',
# });

profile = gl.getProfile(profile_id);

print('new profile name=', profile.get("name"));

# gl.delete('yU0Pr0f1leiD')