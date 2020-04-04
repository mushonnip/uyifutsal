from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'uyiblob'  # Must be replaced by your <storage_account_name>
    # Must be replaced by your <storage_account_key>
    account_key = 'WorRav4p6TjicCZ2qKUd8Ojhw+AHroLedt9PHgiEPv09FfgT8EVOE5ekSxerjy8LFEW4B5rv0RLb0A6IJG6hew=='
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'uyiblob'  # Must be replaced by your storage_account_name
    # Must be replaced by your <storage_account_key>
    account_key = 'WorRav4p6TjicCZ2qKUd8Ojhw+AHroLedt9PHgiEPv09FfgT8EVOE5ekSxerjy8LFEW4B5rv0RLb0A6IJG6hew=='
    azure_container = 'static'
    expiration_secs = None
