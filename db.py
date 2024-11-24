# Random api keys as dummy data in the format of key:value pairs (API key:user ID) 
api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
    "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t"
}

# Mapping api key to users 
users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "name": "Eryka"
    },
    "mUP7PpTHmFAkxcQLWKMY8t": {
        "name": "Ika"
    },
}

# Check apakah api key user yang ingin masuk ada di daftar api key 
def check_api_key(api_key: str):
    return api_key in api_keys

# Retrieve user ID yang berkaitan dengan api key  
def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]
