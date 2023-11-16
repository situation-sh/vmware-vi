# ArrayOfVmNvramFileInfo

A boxed array of *VmNvramFileInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmNvramFileInfo]**](VmNvramFileInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_nvram_file_info import ArrayOfVmNvramFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmNvramFileInfo from a JSON string
array_of_vm_nvram_file_info_instance = ArrayOfVmNvramFileInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmNvramFileInfo.to_json()

# convert the object into a dict
array_of_vm_nvram_file_info_dict = array_of_vm_nvram_file_info_instance.to_dict()
# create an instance of ArrayOfVmNvramFileInfo from a dict
array_of_vm_nvram_file_info_form_dict = array_of_vm_nvram_file_info.from_dict(array_of_vm_nvram_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


