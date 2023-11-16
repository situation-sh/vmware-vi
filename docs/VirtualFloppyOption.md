# VirtualFloppyOption

The VirtualFloppyOption data class contains the options for the virtual floppy data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_floppy_option import VirtualFloppyOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFloppyOption from a JSON string
virtual_floppy_option_instance = VirtualFloppyOption.from_json(json)
# print the JSON string representation of the object
print VirtualFloppyOption.to_json()

# convert the object into a dict
virtual_floppy_option_dict = virtual_floppy_option_instance.to_dict()
# create an instance of VirtualFloppyOption from a dict
virtual_floppy_option_form_dict = virtual_floppy_option.from_dict(virtual_floppy_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


