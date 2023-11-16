# ArrayOfVirtualSIOControllerOption

A boxed array of *VirtualSIOControllerOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSIOControllerOption]**](VirtualSIOControllerOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_sio_controller_option import ArrayOfVirtualSIOControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSIOControllerOption from a JSON string
array_of_virtual_sio_controller_option_instance = ArrayOfVirtualSIOControllerOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSIOControllerOption.to_json()

# convert the object into a dict
array_of_virtual_sio_controller_option_dict = array_of_virtual_sio_controller_option_instance.to_dict()
# create an instance of ArrayOfVirtualSIOControllerOption from a dict
array_of_virtual_sio_controller_option_form_dict = array_of_virtual_sio_controller_option.from_dict(array_of_virtual_sio_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


