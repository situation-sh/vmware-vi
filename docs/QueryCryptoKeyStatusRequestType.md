# QueryCryptoKeyStatusRequestType

The parameters of *CryptoManagerKmip.QueryCryptoKeyStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_ids** | [**List[CryptoKeyId]**](CryptoKeyId.md) | \\[in\\] The Crypto Key Ids to query.  ***Since:*** vSphere API 6.5  | [optional] 
**check_key_bit_map** | **int** | \\[in\\] The key state to check. Supported value: 0x01. check if key data is available to VC. 0x02. check the VMs which use that key. 0x04. check the hosts using this key as host key. 0x08. Check 3rd party program which use that key. Other bits - reserved and will be igonred.  | 

## Example

```python
from vmware_vi.models.query_crypto_key_status_request_type import QueryCryptoKeyStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCryptoKeyStatusRequestType from a JSON string
query_crypto_key_status_request_type_instance = QueryCryptoKeyStatusRequestType.from_json(json)
# print the JSON string representation of the object
print QueryCryptoKeyStatusRequestType.to_json()

# convert the object into a dict
query_crypto_key_status_request_type_dict = query_crypto_key_status_request_type_instance.to_dict()
# create an instance of QueryCryptoKeyStatusRequestType from a dict
query_crypto_key_status_request_type_form_dict = query_crypto_key_status_request_type.from_dict(query_crypto_key_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


