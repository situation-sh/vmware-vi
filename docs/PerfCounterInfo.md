# PerfCounterInfo

This data object type contains metadata for a performance counter.  See *PerformanceManager* for definitions of available counters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A system-generated number that uniquely identifies the counter in the context of the system.  The performance counter ID.  | 
**name_info** | [**ElementDescription**](ElementDescription.md) |  | 
**group_info** | [**ElementDescription**](ElementDescription.md) |  | 
**unit_info** | [**ElementDescription**](ElementDescription.md) |  | 
**rollup_type** | [**PerfSummaryTypeEnum**](PerfSummaryTypeEnum.md) |  | 
**stats_type** | [**PerfStatsTypeEnum**](PerfStatsTypeEnum.md) |  | 
**level** | **int** | Minimum level at which metrics of this type will be collected by VirtualCenter Server.  The value for this property for any performance counter is a number from 1 to 4. The higher the setting, the more data is collected by VirtualCenter Server. The default setting for VirtualCenter Server is 1, which collects the minimal amount of performance data that is typically useful to administrators and developers alike. The specific level of each counter is documented in the respective counter-documentation pages, by group. See *PerformanceManager* for links to the counter group pages.  ***Since:*** VI API 2.5  | [optional] 
**per_device_level** | **int** | Minimum level at which the per device metrics of this type will be collected by vCenter Server.  The value for this property for any performance counter is a number from 1 to 4. By default all per device metrics are calculated at level 3 or more. If a certain per device counter is collected at a certain level, the aggregate metric is also calculated at that level, i.e., perDeviceLevel is greater than or equal to level.  ***Since:*** vSphere API 4.1  | [optional] 
**associated_counter_id** | **List[int]** | Deprecated as of VI API 2.5, this property is not used.  The counter IDs associated with the same performance counter name for the same device type.  For example, the rollup types for CPU Usage for a host are average, minimum, and maximum&amp;#46; Therefore, their counter IDs are associated.  | [optional] 

## Example

```python
from vmware_vi.models.perf_counter_info import PerfCounterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PerfCounterInfo from a JSON string
perf_counter_info_instance = PerfCounterInfo.from_json(json)
# print the JSON string representation of the object
print PerfCounterInfo.to_json()

# convert the object into a dict
perf_counter_info_dict = perf_counter_info_instance.to_dict()
# create an instance of PerfCounterInfo from a dict
perf_counter_info_form_dict = perf_counter_info.from_dict(perf_counter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


