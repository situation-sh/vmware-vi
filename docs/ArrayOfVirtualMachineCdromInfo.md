# ArrayOfVirtualMachineCdromInfo

A boxed array of *VirtualMachineCdromInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineCdromInfo]**](VirtualMachineCdromInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_cdrom_info import ArrayOfVirtualMachineCdromInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineCdromInfo from a JSON string
array_of_virtual_machine_cdrom_info_instance = ArrayOfVirtualMachineCdromInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineCdromInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_cdrom_info_dict = array_of_virtual_machine_cdrom_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineCdromInfo from a dict
array_of_virtual_machine_cdrom_info_form_dict = array_of_virtual_machine_cdrom_info.from_dict(array_of_virtual_machine_cdrom_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


