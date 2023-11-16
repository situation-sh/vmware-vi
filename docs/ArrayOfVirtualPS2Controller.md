# ArrayOfVirtualPS2Controller

A boxed array of *VirtualPS2Controller*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPS2Controller]**](VirtualPS2Controller.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_ps2_controller import ArrayOfVirtualPS2Controller

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPS2Controller from a JSON string
array_of_virtual_ps2_controller_instance = ArrayOfVirtualPS2Controller.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPS2Controller.to_json()

# convert the object into a dict
array_of_virtual_ps2_controller_dict = array_of_virtual_ps2_controller_instance.to_dict()
# create an instance of ArrayOfVirtualPS2Controller from a dict
array_of_virtual_ps2_controller_form_dict = array_of_virtual_ps2_controller.from_dict(array_of_virtual_ps2_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


