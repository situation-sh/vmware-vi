# ArrayOfInvalidController

A boxed array of *InvalidController*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidController]**](InvalidController.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_controller import ArrayOfInvalidController

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidController from a JSON string
array_of_invalid_controller_instance = ArrayOfInvalidController.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidController.to_json()

# convert the object into a dict
array_of_invalid_controller_dict = array_of_invalid_controller_instance.to_dict()
# create an instance of ArrayOfInvalidController from a dict
array_of_invalid_controller_form_dict = array_of_invalid_controller.from_dict(array_of_invalid_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


