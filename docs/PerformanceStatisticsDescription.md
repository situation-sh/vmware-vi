# PerformanceStatisticsDescription

Data object to capture all information needed to describe a sample inventory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[PerfInterval]**](PerfInterval.md) | Historic interval setting.  Default value is the same as the historic interval settings of the current instance of running VC.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.performance_statistics_description import PerformanceStatisticsDescription

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceStatisticsDescription from a JSON string
performance_statistics_description_instance = PerformanceStatisticsDescription.from_json(json)
# print the JSON string representation of the object
print PerformanceStatisticsDescription.to_json()

# convert the object into a dict
performance_statistics_description_dict = performance_statistics_description_instance.to_dict()
# create an instance of PerformanceStatisticsDescription from a dict
performance_statistics_description_form_dict = performance_statistics_description.from_dict(performance_statistics_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


