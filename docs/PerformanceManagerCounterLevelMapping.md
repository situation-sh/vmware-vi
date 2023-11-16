# PerformanceManagerCounterLevelMapping

*PerformanceManagerCounterLevelMapping* class captures the counter and level mapping.  Any counter has two aspects: aggregate value or the per-device value. For example, cpu.usage.average on a host is an aggregate counter and cpu.usage.average on pcpus in a host is a per-device counters. There is a need to be able to specify different levels for the two versions. Currently, all per-device stats are collected at level greater than or equal to 3.  In order to be able to configure the level of collections for aggregate and per-device counters we have two optional level fields. *PerformanceManagerCounterLevelMapping* is used to update the levels for a counter.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_id** | **int** | The counter Id  ***Since:*** vSphere API 4.1  | 
**aggregate_level** | **int** | Level for the aggregate counter.  If not set then the value is not changed when updateCounterLevelMapping is called.  ***Since:*** vSphere API 4.1  | [optional] 
**per_device_level** | **int** | Level for the per device counter.  If not set then the value is not changed when updateCounterLevelMapping is called.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.performance_manager_counter_level_mapping import PerformanceManagerCounterLevelMapping

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceManagerCounterLevelMapping from a JSON string
performance_manager_counter_level_mapping_instance = PerformanceManagerCounterLevelMapping.from_json(json)
# print the JSON string representation of the object
print PerformanceManagerCounterLevelMapping.to_json()

# convert the object into a dict
performance_manager_counter_level_mapping_dict = performance_manager_counter_level_mapping_instance.to_dict()
# create an instance of PerformanceManagerCounterLevelMapping from a dict
performance_manager_counter_level_mapping_form_dict = performance_manager_counter_level_mapping.from_dict(performance_manager_counter_level_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


