# VirtualKeyboardOption

The VirtualKeyboardOption data object type contains the options for the virtual keyboard class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_keyboard_option import VirtualKeyboardOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualKeyboardOption from a JSON string
virtual_keyboard_option_instance = VirtualKeyboardOption.from_json(json)
# print the JSON string representation of the object
print VirtualKeyboardOption.to_json()

# convert the object into a dict
virtual_keyboard_option_dict = virtual_keyboard_option_instance.to_dict()
# create an instance of VirtualKeyboardOption from a dict
virtual_keyboard_option_form_dict = virtual_keyboard_option.from_dict(virtual_keyboard_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


