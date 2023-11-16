# ChangeKeyRequestType

The parameters of *CryptoManagerHost.ChangeKey_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_key** | [**CryptoKeyPlain**](CryptoKeyPlain.md) |  | 

## Example

```python
from vmware_vi.models.change_key_request_type import ChangeKeyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeKeyRequestType from a JSON string
change_key_request_type_instance = ChangeKeyRequestType.from_json(json)
# print the JSON string representation of the object
print ChangeKeyRequestType.to_json()

# convert the object into a dict
change_key_request_type_dict = change_key_request_type_instance.to_dict()
# create an instance of ChangeKeyRequestType from a dict
change_key_request_type_form_dict = change_key_request_type.from_dict(change_key_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


