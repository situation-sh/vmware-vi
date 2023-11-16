# ArrayOfHostNetOffloadCapabilities

A boxed array of *HostNetOffloadCapabilities*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetOffloadCapabilities]**](HostNetOffloadCapabilities.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_net_offload_capabilities import ArrayOfHostNetOffloadCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetOffloadCapabilities from a JSON string
array_of_host_net_offload_capabilities_instance = ArrayOfHostNetOffloadCapabilities.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetOffloadCapabilities.to_json()

# convert the object into a dict
array_of_host_net_offload_capabilities_dict = array_of_host_net_offload_capabilities_instance.to_dict()
# create an instance of ArrayOfHostNetOffloadCapabilities from a dict
array_of_host_net_offload_capabilities_form_dict = array_of_host_net_offload_capabilities.from_dict(array_of_host_net_offload_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


