# ArrayOfVirtualController

A boxed array of *VirtualController*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualController]**](VirtualController.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_controller import ArrayOfVirtualController

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualController from a JSON string
array_of_virtual_controller_instance = ArrayOfVirtualController.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualController.to_json()

# convert the object into a dict
array_of_virtual_controller_dict = array_of_virtual_controller_instance.to_dict()
# create an instance of ArrayOfVirtualController from a dict
array_of_virtual_controller_form_dict = array_of_virtual_controller.from_dict(array_of_virtual_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


