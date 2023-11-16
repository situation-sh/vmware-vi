# ArrayOfOpaqueNetworkCapability

A boxed array of *OpaqueNetworkCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OpaqueNetworkCapability]**](OpaqueNetworkCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_opaque_network_capability import ArrayOfOpaqueNetworkCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOpaqueNetworkCapability from a JSON string
array_of_opaque_network_capability_instance = ArrayOfOpaqueNetworkCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfOpaqueNetworkCapability.to_json()

# convert the object into a dict
array_of_opaque_network_capability_dict = array_of_opaque_network_capability_instance.to_dict()
# create an instance of ArrayOfOpaqueNetworkCapability from a dict
array_of_opaque_network_capability_form_dict = array_of_opaque_network_capability.from_dict(array_of_opaque_network_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


