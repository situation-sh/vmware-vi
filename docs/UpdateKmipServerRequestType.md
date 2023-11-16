# UpdateKmipServerRequestType

The parameters of *CryptoManagerKmip.UpdateKmipServer*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**KmipServerSpec**](KmipServerSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_kmip_server_request_type import UpdateKmipServerRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKmipServerRequestType from a JSON string
update_kmip_server_request_type_instance = UpdateKmipServerRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateKmipServerRequestType.to_json()

# convert the object into a dict
update_kmip_server_request_type_dict = update_kmip_server_request_type_instance.to_dict()
# create an instance of UpdateKmipServerRequestType from a dict
update_kmip_server_request_type_form_dict = update_kmip_server_request_type.from_dict(update_kmip_server_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


