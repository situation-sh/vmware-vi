# ArrayOfVirtualMachineContentLibraryItemInfo

A boxed array of *VirtualMachineContentLibraryItemInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineContentLibraryItemInfo]**](VirtualMachineContentLibraryItemInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_content_library_item_info import ArrayOfVirtualMachineContentLibraryItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineContentLibraryItemInfo from a JSON string
array_of_virtual_machine_content_library_item_info_instance = ArrayOfVirtualMachineContentLibraryItemInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineContentLibraryItemInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_content_library_item_info_dict = array_of_virtual_machine_content_library_item_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineContentLibraryItemInfo from a dict
array_of_virtual_machine_content_library_item_info_form_dict = array_of_virtual_machine_content_library_item_info.from_dict(array_of_virtual_machine_content_library_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


