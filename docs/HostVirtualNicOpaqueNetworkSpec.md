# HostVirtualNicOpaqueNetworkSpec

The *HostVirtualNicOpaqueNetworkSpec* data object describes the opaque network(*HostOpaqueNetworkInfo*) configuration used by virtual NIC.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque_network_id** | **str** | ID of the Opaque network to which the virtual NIC is connected.  ***Since:*** vSphere API 6.0  | 
**opaque_network_type** | **str** | Type of the Opaque network to which the virtual NIC is connected.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_virtual_nic_opaque_network_spec import HostVirtualNicOpaqueNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicOpaqueNetworkSpec from a JSON string
host_virtual_nic_opaque_network_spec_instance = HostVirtualNicOpaqueNetworkSpec.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicOpaqueNetworkSpec.to_json()

# convert the object into a dict
host_virtual_nic_opaque_network_spec_dict = host_virtual_nic_opaque_network_spec_instance.to_dict()
# create an instance of HostVirtualNicOpaqueNetworkSpec from a dict
host_virtual_nic_opaque_network_spec_form_dict = host_virtual_nic_opaque_network_spec.from_dict(host_virtual_nic_opaque_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


