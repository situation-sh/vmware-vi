# ArrayOfHostNetCapabilities

A boxed array of *HostNetCapabilities*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetCapabilities]**](HostNetCapabilities.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_net_capabilities import ArrayOfHostNetCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetCapabilities from a JSON string
array_of_host_net_capabilities_instance = ArrayOfHostNetCapabilities.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetCapabilities.to_json()

# convert the object into a dict
array_of_host_net_capabilities_dict = array_of_host_net_capabilities_instance.to_dict()
# create an instance of ArrayOfHostNetCapabilities from a dict
array_of_host_net_capabilities_form_dict = array_of_host_net_capabilities.from_dict(array_of_host_net_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


