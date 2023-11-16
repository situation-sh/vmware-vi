# ArrayOfPerformanceDescription

A boxed array of *PerformanceDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerformanceDescription]**](PerformanceDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_performance_description import ArrayOfPerformanceDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerformanceDescription from a JSON string
array_of_performance_description_instance = ArrayOfPerformanceDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerformanceDescription.to_json()

# convert the object into a dict
array_of_performance_description_dict = array_of_performance_description_instance.to_dict()
# create an instance of ArrayOfPerformanceDescription from a dict
array_of_performance_description_form_dict = array_of_performance_description.from_dict(array_of_performance_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


