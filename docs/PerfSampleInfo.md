# PerfSampleInfo

This data object type describes information contained in a sample collection, its timestamp, and sampling interval. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The time at which the sample was collected.  | 
**interval** | **int** | The interval in seconds for which performance statistics were collected.  This can be the refreshRate of the managed object for which this statistics was collected or one of the intervals for historical statistics configured in the system. See *PerformanceManager.UpdatePerfInterval* for more information about the intervals configured in the system.  | 

## Example

```python
from vmware_vi.models.perf_sample_info import PerfSampleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PerfSampleInfo from a JSON string
perf_sample_info_instance = PerfSampleInfo.from_json(json)
# print the JSON string representation of the object
print PerfSampleInfo.to_json()

# convert the object into a dict
perf_sample_info_dict = perf_sample_info_instance.to_dict()
# create an instance of PerfSampleInfo from a dict
perf_sample_info_form_dict = perf_sample_info.from_dict(perf_sample_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


