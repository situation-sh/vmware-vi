# VirtualMachineToolsStatus

A boxed *VirtualMachineToolsStatus_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineToolsStatusEnum**](VirtualMachineToolsStatusEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_tools_status import VirtualMachineToolsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineToolsStatus from a JSON string
virtual_machine_tools_status_instance = VirtualMachineToolsStatus.from_json(json)
# print the JSON string representation of the object
print VirtualMachineToolsStatus.to_json()

# convert the object into a dict
virtual_machine_tools_status_dict = virtual_machine_tools_status_instance.to_dict()
# create an instance of VirtualMachineToolsStatus from a dict
virtual_machine_tools_status_form_dict = virtual_machine_tools_status.from_dict(virtual_machine_tools_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


