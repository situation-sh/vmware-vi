# RemoveKmipServerRequestType

The parameters of *CryptoManagerKmip.RemoveKmipServer*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 
**server_name** | **str** | \\[in\\] KMIP server name.  | 

## Example

```python
from vmware_vi.models.remove_kmip_server_request_type import RemoveKmipServerRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveKmipServerRequestType from a JSON string
remove_kmip_server_request_type_instance = RemoveKmipServerRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveKmipServerRequestType.to_json()

# convert the object into a dict
remove_kmip_server_request_type_dict = remove_kmip_server_request_type_instance.to_dict()
# create an instance of RemoveKmipServerRequestType from a dict
remove_kmip_server_request_type_form_dict = remove_kmip_server_request_type.from_dict(remove_kmip_server_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


