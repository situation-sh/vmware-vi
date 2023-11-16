# ArrayOfHostVirtualNicOpaqueNetworkSpec

A boxed array of *HostVirtualNicOpaqueNetworkSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualNicOpaqueNetworkSpec]**](HostVirtualNicOpaqueNetworkSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_nic_opaque_network_spec import ArrayOfHostVirtualNicOpaqueNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualNicOpaqueNetworkSpec from a JSON string
array_of_host_virtual_nic_opaque_network_spec_instance = ArrayOfHostVirtualNicOpaqueNetworkSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualNicOpaqueNetworkSpec.to_json()

# convert the object into a dict
array_of_host_virtual_nic_opaque_network_spec_dict = array_of_host_virtual_nic_opaque_network_spec_instance.to_dict()
# create an instance of ArrayOfHostVirtualNicOpaqueNetworkSpec from a dict
array_of_host_virtual_nic_opaque_network_spec_form_dict = array_of_host_virtual_nic_opaque_network_spec.from_dict(array_of_host_virtual_nic_opaque_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


