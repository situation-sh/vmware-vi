# ArrayOfKmipServerInfo

A boxed array of *KmipServerInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KmipServerInfo]**](KmipServerInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_kmip_server_info import ArrayOfKmipServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKmipServerInfo from a JSON string
array_of_kmip_server_info_instance = ArrayOfKmipServerInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfKmipServerInfo.to_json()

# convert the object into a dict
array_of_kmip_server_info_dict = array_of_kmip_server_info_instance.to_dict()
# create an instance of ArrayOfKmipServerInfo from a dict
array_of_kmip_server_info_form_dict = array_of_kmip_server_info.from_dict(array_of_kmip_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


