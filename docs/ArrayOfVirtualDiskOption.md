# ArrayOfVirtualDiskOption

A boxed array of *VirtualDiskOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDiskOption]**](VirtualDiskOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_disk_option import ArrayOfVirtualDiskOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDiskOption from a JSON string
array_of_virtual_disk_option_instance = ArrayOfVirtualDiskOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDiskOption.to_json()

# convert the object into a dict
array_of_virtual_disk_option_dict = array_of_virtual_disk_option_instance.to_dict()
# create an instance of ArrayOfVirtualDiskOption from a dict
array_of_virtual_disk_option_form_dict = array_of_virtual_disk_option.from_dict(array_of_virtual_disk_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


