# ListKmipServersRequestType

The parameters of *CryptoManagerKmip.ListKmipServers*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | \\[in\\] maximum clusters to return.  | [optional] 

## Example

```python
from vmware_vi.models.list_kmip_servers_request_type import ListKmipServersRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListKmipServersRequestType from a JSON string
list_kmip_servers_request_type_instance = ListKmipServersRequestType.from_json(json)
# print the JSON string representation of the object
print ListKmipServersRequestType.to_json()

# convert the object into a dict
list_kmip_servers_request_type_dict = list_kmip_servers_request_type_instance.to_dict()
# create an instance of ListKmipServersRequestType from a dict
list_kmip_servers_request_type_form_dict = list_kmip_servers_request_type.from_dict(list_kmip_servers_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


