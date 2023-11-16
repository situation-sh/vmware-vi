# RegisterKmipServerRequestType

The parameters of *CryptoManagerKmip.RegisterKmipServer*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**KmipServerSpec**](KmipServerSpec.md) |  | 

## Example

```python
from vmware_vi.models.register_kmip_server_request_type import RegisterKmipServerRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterKmipServerRequestType from a JSON string
register_kmip_server_request_type_instance = RegisterKmipServerRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterKmipServerRequestType.to_json()

# convert the object into a dict
register_kmip_server_request_type_dict = register_kmip_server_request_type_instance.to_dict()
# create an instance of RegisterKmipServerRequestType from a dict
register_kmip_server_request_type_form_dict = register_kmip_server_request_type.from_dict(register_kmip_server_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


