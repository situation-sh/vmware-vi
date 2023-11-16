# VirtualMachineVMCIDeviceFilterSpec

The *VirtualMachineVMCIDeviceFilterSpec* data object describes a filter based on protocol, direction and port or port-range.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** | Long value representing filter rank.  This is the rank of this filter. Filters are guaranteed to be processed in ascending rank order, that is, if rank1 &amp;lt; rank2, then rank1 is processed before rank2. The ranks within an array of filters should be unique.  ***Since:*** vSphere API 6.0  | 
**action** | **str** | String value from *VirtualMachineVMCIDeviceAction_enum* enum object.  ***Since:*** vSphere API 6.0  | 
**protocol** | **str** | String value from *VirtualMachineVMCIDeviceProtocol_enum* enum object  ***Since:*** vSphere API 6.0  | 
**direction** | **str** | String value from *VirtualMachineVMCIDeviceDirection_enum* enum object.  ***Since:*** vSphere API 6.0  | 
**lower_dst_port_boundary** | **int** | Long value representing the lower destination port boundary.  If unset, the lower destination port boundary is default to the lowest port number supported by the given protocol.  To specify a single port, both lowerDstPortBoundary and upperDstPortBoundary shall be set to the same value.  ***Since:*** vSphere API 6.0  | [optional] 
**upper_dst_port_boundary** | **int** | Long value representing the upper destination port range.  If unset, the upper destination port boundary is default to the highest port number supported by the given protocol.  To specify a single port, both lowerDstPortBoundary and upperDstPortBoundary shall be set to the same value.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_vmci_device_filter_spec import VirtualMachineVMCIDeviceFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVMCIDeviceFilterSpec from a JSON string
virtual_machine_vmci_device_filter_spec_instance = VirtualMachineVMCIDeviceFilterSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVMCIDeviceFilterSpec.to_json()

# convert the object into a dict
virtual_machine_vmci_device_filter_spec_dict = virtual_machine_vmci_device_filter_spec_instance.to_dict()
# create an instance of VirtualMachineVMCIDeviceFilterSpec from a dict
virtual_machine_vmci_device_filter_spec_form_dict = virtual_machine_vmci_device_filter_spec.from_dict(virtual_machine_vmci_device_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


