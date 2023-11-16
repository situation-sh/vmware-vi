# ArrayOfKmipServerStatus

A boxed array of *KmipServerStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KmipServerStatus]**](KmipServerStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_kmip_server_status import ArrayOfKmipServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKmipServerStatus from a JSON string
array_of_kmip_server_status_instance = ArrayOfKmipServerStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfKmipServerStatus.to_json()

# convert the object into a dict
array_of_kmip_server_status_dict = array_of_kmip_server_status_instance.to_dict()
# create an instance of ArrayOfKmipServerStatus from a dict
array_of_kmip_server_status_form_dict = array_of_kmip_server_status.from_dict(array_of_kmip_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


