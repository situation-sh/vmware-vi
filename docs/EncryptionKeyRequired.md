# EncryptionKeyRequired

An EncryptionKeyRequired fault occurs when an operation fails due to one or more required encryption keys.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_key** | [**List[CryptoKeyId]**](CryptoKeyId.md) | A list of required key identifiers.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.encryption_key_required import EncryptionKeyRequired

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyRequired from a JSON string
encryption_key_required_instance = EncryptionKeyRequired.from_json(json)
# print the JSON string representation of the object
print EncryptionKeyRequired.to_json()

# convert the object into a dict
encryption_key_required_dict = encryption_key_required_instance.to_dict()
# create an instance of EncryptionKeyRequired from a dict
encryption_key_required_form_dict = encryption_key_required.from_dict(encryption_key_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


