# ArrayOfPerformanceStatisticsDescription

A boxed array of *PerformanceStatisticsDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerformanceStatisticsDescription]**](PerformanceStatisticsDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_performance_statistics_description import ArrayOfPerformanceStatisticsDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerformanceStatisticsDescription from a JSON string
array_of_performance_statistics_description_instance = ArrayOfPerformanceStatisticsDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerformanceStatisticsDescription.to_json()

# convert the object into a dict
array_of_performance_statistics_description_dict = array_of_performance_statistics_description_instance.to_dict()
# create an instance of ArrayOfPerformanceStatisticsDescription from a dict
array_of_performance_statistics_description_form_dict = array_of_performance_statistics_description.from_dict(array_of_performance_statistics_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


