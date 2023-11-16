# VirtualFloppy

The VirtualFloppy data object type contains information about a floppy drive in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_floppy import VirtualFloppy

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFloppy from a JSON string
virtual_floppy_instance = VirtualFloppy.from_json(json)
# print the JSON string representation of the object
print VirtualFloppy.to_json()

# convert the object into a dict
virtual_floppy_dict = virtual_floppy_instance.to_dict()
# create an instance of VirtualFloppy from a dict
virtual_floppy_form_dict = virtual_floppy.from_dict(virtual_floppy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


