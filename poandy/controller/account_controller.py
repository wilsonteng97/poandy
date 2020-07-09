from poandy.util.utils import Utils
from poandy.util.request import RequestSender, RequestType
from poandy.util.objectless import Objectless

class AccountController(Objectless):
    _config = Utils.get_config()
    _authorization = Utils.get_authorization()
    
    @classmethod
    def get_accounts(cls):
        url = f"{cls._config['base_url']}/v3/accounts"
        response = RequestSender.send(url, cls._authorization, RequestType.GET)
        return response.json()["accounts"] if response.status_code == 200 else response.raise_for_status()

    @classmethod
    def get_default_account(cls):
        return cls.get_accounts()[0]

    @classmethod
    def get_account_details(cls, account_id):
        url = f"{cls._config['base_url']}/v3/accounts/{account_id}"
        response = RequestSender.send(url, cls._authorization, RequestType.GET)
        return response.json() if response.status_code == 200 else response.raise_for_status()

    @classmethod
    def get_account_summary(cls, account_id):
        url = f"{cls._config['base_url']}/v3/accounts/{account_id}/summary"
        response = RequestSender.send(url, cls._authorization, RequestType.GET)
        return response.json() if response.status_code == 200 else response.raise_for_status()

    @classmethod
    def get_tradeable_instruments(cls, account_id, instruments=[]):
        url = f"{cls._config['base_url']}/v3/accounts/{account_id}/instruments"
        response = RequestSender.send(url, cls._authorization, RequestType.GET, {"instruments": instruments})
        return response.json() if response.status_code == 200 else response.raise_for_status()

    # TODO: Somehow "since_transaction_id" needs to be 3. Oanda bug?
    @classmethod
    def get_account_changes(cls, account_id, since_transaction_id=None):
        url = f"{cls._config['base_url']}/v3/accounts/{account_id}/changes"
        response = RequestSender.send(url, cls._authorization, RequestType.GET, {"sinceTransactionID": since_transaction_id})
        return response.json() if response.status_code == 200 else response.raise_for_status()