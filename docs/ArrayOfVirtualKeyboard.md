# ArrayOfVirtualKeyboard

A boxed array of *VirtualKeyboard*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualKeyboard]**](VirtualKeyboard.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_keyboard import ArrayOfVirtualKeyboard

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualKeyboard from a JSON string
array_of_virtual_keyboard_instance = ArrayOfVirtualKeyboard.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualKeyboard.to_json()

# convert the object into a dict
array_of_virtual_keyboard_dict = array_of_virtual_keyboard_instance.to_dict()
# create an instance of ArrayOfVirtualKeyboard from a dict
array_of_virtual_keyboard_form_dict = array_of_virtual_keyboard.from_dict(array_of_virtual_keyboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


