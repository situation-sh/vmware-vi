# ReloadVirtualMachineFromPathRequestType

The parameters of *VirtualMachine.reloadVirtualMachineFromPath_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_path** | **str** |  | 

## Example

```python
from vmware_vi.models.reload_virtual_machine_from_path_request_type import ReloadVirtualMachineFromPathRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReloadVirtualMachineFromPathRequestType from a JSON string
reload_virtual_machine_from_path_request_type_instance = ReloadVirtualMachineFromPathRequestType.from_json(json)
# print the JSON string representation of the object
print ReloadVirtualMachineFromPathRequestType.to_json()

# convert the object into a dict
reload_virtual_machine_from_path_request_type_dict = reload_virtual_machine_from_path_request_type_instance.to_dict()
# create an instance of ReloadVirtualMachineFromPathRequestType from a dict
reload_virtual_machine_from_path_request_type_form_dict = reload_virtual_machine_from_path_request_type.from_dict(reload_virtual_machine_from_path_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


