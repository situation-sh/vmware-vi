# ArrayOfVirtualMachineToolsStatus

A boxed array of *VirtualMachineToolsStatus_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineToolsStatusEnum]**](VirtualMachineToolsStatusEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_tools_status import ArrayOfVirtualMachineToolsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineToolsStatus from a JSON string
array_of_virtual_machine_tools_status_instance = ArrayOfVirtualMachineToolsStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineToolsStatus.to_json()

# convert the object into a dict
array_of_virtual_machine_tools_status_dict = array_of_virtual_machine_tools_status_instance.to_dict()
# create an instance of ArrayOfVirtualMachineToolsStatus from a dict
array_of_virtual_machine_tools_status_form_dict = array_of_virtual_machine_tools_status.from_dict(array_of_virtual_machine_tools_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


