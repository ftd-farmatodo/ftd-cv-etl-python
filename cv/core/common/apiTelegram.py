import requests

# from common import constants as cons
from cv.core.common import constants as cons


# cons = importlib.machinery.SourceFileLoader('cons', 'E:\gcloud_repository\CronsPython\common/constants.py').load_module()

def send_message(msg):
    params = {
        'chat_id': cons.ID_CHANNEL_TELEGRAM,
        'text': str(msg)
    }
    requests.post(cons.API_TELEGRAM_SEND_MSG, params=params)
