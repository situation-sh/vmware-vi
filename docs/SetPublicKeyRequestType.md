# SetPublicKeyRequestType

The parameters of *ExtensionManager.SetPublicKey*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key of extension to update.  | 
**public_key** | **str** | Public key of extension, encoded in PEM (privacy-enhanced mail) format.  | 

## Example

```python
from vmware_vi.models.set_public_key_request_type import SetPublicKeyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetPublicKeyRequestType from a JSON string
set_public_key_request_type_instance = SetPublicKeyRequestType.from_json(json)
# print the JSON string representation of the object
print SetPublicKeyRequestType.to_json()

# convert the object into a dict
set_public_key_request_type_dict = set_public_key_request_type_instance.to_dict()
# create an instance of SetPublicKeyRequestType from a dict
set_public_key_request_type_form_dict = set_public_key_request_type.from_dict(set_public_key_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


