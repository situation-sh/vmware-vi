# ArrayOfOpaqueNetworkTargetInfo

A boxed array of *OpaqueNetworkTargetInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OpaqueNetworkTargetInfo]**](OpaqueNetworkTargetInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_opaque_network_target_info import ArrayOfOpaqueNetworkTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOpaqueNetworkTargetInfo from a JSON string
array_of_opaque_network_target_info_instance = ArrayOfOpaqueNetworkTargetInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfOpaqueNetworkTargetInfo.to_json()

# convert the object into a dict
array_of_opaque_network_target_info_dict = array_of_opaque_network_target_info_instance.to_dict()
# create an instance of ArrayOfOpaqueNetworkTargetInfo from a dict
array_of_opaque_network_target_info_form_dict = array_of_opaque_network_target_info.from_dict(array_of_opaque_network_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


