# VirtualKeyboard

This data object type contains information about the keyboard on a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_keyboard import VirtualKeyboard

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualKeyboard from a JSON string
virtual_keyboard_instance = VirtualKeyboard.from_json(json)
# print the JSON string representation of the object
print VirtualKeyboard.to_json()

# convert the object into a dict
virtual_keyboard_dict = virtual_keyboard_instance.to_dict()
# create an instance of VirtualKeyboard from a dict
virtual_keyboard_form_dict = virtual_keyboard.from_dict(virtual_keyboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


