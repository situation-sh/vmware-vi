# ArrayOfVirtualIDEControllerOption

A boxed array of *VirtualIDEControllerOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualIDEControllerOption]**](VirtualIDEControllerOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_ide_controller_option import ArrayOfVirtualIDEControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualIDEControllerOption from a JSON string
array_of_virtual_ide_controller_option_instance = ArrayOfVirtualIDEControllerOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualIDEControllerOption.to_json()

# convert the object into a dict
array_of_virtual_ide_controller_option_dict = array_of_virtual_ide_controller_option_instance.to_dict()
# create an instance of ArrayOfVirtualIDEControllerOption from a dict
array_of_virtual_ide_controller_option_form_dict = array_of_virtual_ide_controller_option.from_dict(array_of_virtual_ide_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


