# VirtualMachineTargetInfo

The TargetInfo specified a value that can be used in the device backings to connect the virtual machine to a physical (or logical) host device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The identification of the endpoint on the host.  The format of this depends on the kind of virtual device this endpoints is used for. For example, for a VirtualEthernetCard this would be a networkname, and for a VirtualCDROM it would be a device name.  | 
**configuration_tag** | **List[str]** | List of configurations that this device is available for.  This is only filled out if more than one configuration is requested.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_target_info import VirtualMachineTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineTargetInfo from a JSON string
virtual_machine_target_info_instance = VirtualMachineTargetInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineTargetInfo.to_json()

# convert the object into a dict
virtual_machine_target_info_dict = virtual_machine_target_info_instance.to_dict()
# create an instance of VirtualMachineTargetInfo from a dict
virtual_machine_target_info_form_dict = virtual_machine_target_info.from_dict(virtual_machine_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


