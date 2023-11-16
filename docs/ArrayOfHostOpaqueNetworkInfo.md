# ArrayOfHostOpaqueNetworkInfo

A boxed array of *HostOpaqueNetworkInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostOpaqueNetworkInfo]**](HostOpaqueNetworkInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_opaque_network_info import ArrayOfHostOpaqueNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostOpaqueNetworkInfo from a JSON string
array_of_host_opaque_network_info_instance = ArrayOfHostOpaqueNetworkInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostOpaqueNetworkInfo.to_json()

# convert the object into a dict
array_of_host_opaque_network_info_dict = array_of_host_opaque_network_info_instance.to_dict()
# create an instance of ArrayOfHostOpaqueNetworkInfo from a dict
array_of_host_opaque_network_info_form_dict = array_of_host_opaque_network_info.from_dict(array_of_host_opaque_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


