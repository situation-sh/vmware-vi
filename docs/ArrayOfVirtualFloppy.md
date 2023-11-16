# ArrayOfVirtualFloppy

A boxed array of *VirtualFloppy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualFloppy]**](VirtualFloppy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_floppy import ArrayOfVirtualFloppy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualFloppy from a JSON string
array_of_virtual_floppy_instance = ArrayOfVirtualFloppy.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualFloppy.to_json()

# convert the object into a dict
array_of_virtual_floppy_dict = array_of_virtual_floppy_instance.to_dict()
# create an instance of ArrayOfVirtualFloppy from a dict
array_of_virtual_floppy_form_dict = array_of_virtual_floppy.from_dict(array_of_virtual_floppy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


