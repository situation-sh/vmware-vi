# HostVirtualNic

The *HostVirtualNic* data object describes a virtual network adapter that connects to a virtual switch.  A host virtual NIC differs from a physical NIC: - A host virtual NIC is a virtual device that is connected to a virtual switch. - A physical NIC (*HostNetworkInfo.pnic*) corresponds to a physical   device that is connected to the physical network.    A host virtual NIC provides access to the external network through a virtual switch that is bridged through a Physical NIC to a physical network. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Device name.  | 
**key** | **str** | Linkable identifier.  | 
**portgroup** | **str** | If the Virtual NIC is connecting to a vSwitch, this property is the name of portgroup connected.  If the Virtual NIC is connecting to a DistributedVirtualSwitch or opaque network, this property is an empty string.  | 
**spec** | [**HostVirtualNicSpec**](HostVirtualNicSpec.md) |  | 
**port** | [**HostPortGroupPort**](HostPortGroupPort.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic import HostVirtualNic

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNic from a JSON string
host_virtual_nic_instance = HostVirtualNic.from_json(json)
# print the JSON string representation of the object
print HostVirtualNic.to_json()

# convert the object into a dict
host_virtual_nic_dict = host_virtual_nic_instance.to_dict()
# create an instance of HostVirtualNic from a dict
host_virtual_nic_form_dict = host_virtual_nic.from_dict(host_virtual_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


