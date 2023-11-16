# PerformanceDescription

Static strings for performance metrics. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_type** | [**List[ElementDescription]**](ElementDescription.md) | Identifies the *type* of the counter.  | 
**stats_type** | [**List[ElementDescription]**](ElementDescription.md) | Identifies the *type* of statistic.  | 

## Example

```python
from vmware_vi.models.performance_description import PerformanceDescription

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceDescription from a JSON string
performance_description_instance = PerformanceDescription.from_json(json)
# print the JSON string representation of the object
print PerformanceDescription.to_json()

# convert the object into a dict
performance_description_dict = performance_description_instance.to_dict()
# create an instance of PerformanceDescription from a dict
performance_description_form_dict = performance_description.from_dict(performance_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


