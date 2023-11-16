# ArrayOfInsufficientResourcesFault

A boxed array of *InsufficientResourcesFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientResourcesFault]**](InsufficientResourcesFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_resources_fault import ArrayOfInsufficientResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientResourcesFault from a JSON string
array_of_insufficient_resources_fault_instance = ArrayOfInsufficientResourcesFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientResourcesFault.to_json()

# convert the object into a dict
array_of_insufficient_resources_fault_dict = array_of_insufficient_resources_fault_instance.to_dict()
# create an instance of ArrayOfInsufficientResourcesFault from a dict
array_of_insufficient_resources_fault_form_dict = array_of_insufficient_resources_fault.from_dict(array_of_insufficient_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


