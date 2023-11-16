# HostVirtualNicConfig

The *HostVirtualNicConfig* data object describes the virtual NIC configuration.  It represents both the configured properties on a *HostVirtualNic* and identification information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | Change operation to apply on this configuration specification.  See also *HostConfigChangeOperation_enum*.  | [optional] 
**device** | **str** | Virtual NIC device (*HostVirtualNic.device*) to which configuration applies.  | [optional] 
**portgroup** | **str** | If the Virtual NIC is connecting to a vSwitch, this property is the name of portgroup connected.  If the Virtual NIC is connecting to a *DistributedVirtualSwitch* or *HostOpaqueNetworkInfo*, this property is ignored.  | 
**spec** | [**HostVirtualNicSpec**](HostVirtualNicSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic_config import HostVirtualNicConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicConfig from a JSON string
host_virtual_nic_config_instance = HostVirtualNicConfig.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicConfig.to_json()

# convert the object into a dict
host_virtual_nic_config_dict = host_virtual_nic_config_instance.to_dict()
# create an instance of HostVirtualNicConfig from a dict
host_virtual_nic_config_form_dict = host_virtual_nic_config.from_dict(host_virtual_nic_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


