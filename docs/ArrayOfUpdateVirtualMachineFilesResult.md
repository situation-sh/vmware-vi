# ArrayOfUpdateVirtualMachineFilesResult

A boxed array of *UpdateVirtualMachineFilesResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UpdateVirtualMachineFilesResult]**](UpdateVirtualMachineFilesResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_update_virtual_machine_files_result import ArrayOfUpdateVirtualMachineFilesResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUpdateVirtualMachineFilesResult from a JSON string
array_of_update_virtual_machine_files_result_instance = ArrayOfUpdateVirtualMachineFilesResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfUpdateVirtualMachineFilesResult.to_json()

# convert the object into a dict
array_of_update_virtual_machine_files_result_dict = array_of_update_virtual_machine_files_result_instance.to_dict()
# create an instance of ArrayOfUpdateVirtualMachineFilesResult from a dict
array_of_update_virtual_machine_files_result_form_dict = array_of_update_virtual_machine_files_result.from_dict(array_of_update_virtual_machine_files_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


