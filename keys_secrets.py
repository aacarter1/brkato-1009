# write a method that will take in secrets and keys and store them in a dict
# in a secure manner
import json
import hashlib

def store_secrets_and_keys(secrets, keys):
    """
    Takes two lists: secrets and keys, and hashes the secrets, and returns a dictionary mapping keys to hashed secrets.
    Also, returns  a SHA-256 of the resulting dictionary.
    """
    hashed_secrets = [hashlib.sha256(s.encode()).hexdigest() for s in secrets]
    secrets_dict = dict(zip(keys, hashed_secrets))
    dict_json = json.dumps(secrets_dict, sort_keys=True)
    dict_hash = hashlib.sha256(dict_json.encode()).hexdigest()
    return secrets_dict, dict_hash
    