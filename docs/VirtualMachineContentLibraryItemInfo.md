# VirtualMachineContentLibraryItemInfo

Describes the content library item information associated with the virtual machine.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_library_item_uuid** | **str** | The content library item UUID  ***Since:*** vSphere API 7.0  | 
**content_library_item_version** | **str** | The content library item version is determined and managed by content library and this field stamps the version provided by CL to the VM.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_content_library_item_info import VirtualMachineContentLibraryItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineContentLibraryItemInfo from a JSON string
virtual_machine_content_library_item_info_instance = VirtualMachineContentLibraryItemInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineContentLibraryItemInfo.to_json()

# convert the object into a dict
virtual_machine_content_library_item_info_dict = virtual_machine_content_library_item_info_instance.to_dict()
# create an instance of VirtualMachineContentLibraryItemInfo from a dict
virtual_machine_content_library_item_info_form_dict = virtual_machine_content_library_item_info.from_dict(virtual_machine_content_library_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


