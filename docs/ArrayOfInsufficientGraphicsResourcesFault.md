# ArrayOfInsufficientGraphicsResourcesFault

A boxed array of *InsufficientGraphicsResourcesFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientGraphicsResourcesFault]**](InsufficientGraphicsResourcesFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_graphics_resources_fault import ArrayOfInsufficientGraphicsResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientGraphicsResourcesFault from a JSON string
array_of_insufficient_graphics_resources_fault_instance = ArrayOfInsufficientGraphicsResourcesFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientGraphicsResourcesFault.to_json()

# convert the object into a dict
array_of_insufficient_graphics_resources_fault_dict = array_of_insufficient_graphics_resources_fault_instance.to_dict()
# create an instance of ArrayOfInsufficientGraphicsResourcesFault from a dict
array_of_insufficient_graphics_resources_fault_form_dict = array_of_insufficient_graphics_resources_fault.from_dict(array_of_insufficient_graphics_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


