# PerfStatsType

A boxed *PerfStatsType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PerfStatsTypeEnum**](PerfStatsTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.perf_stats_type import PerfStatsType

# TODO update the JSON string below
json = "{}"
# create an instance of PerfStatsType from a JSON string
perf_stats_type_instance = PerfStatsType.from_json(json)
# print the JSON string representation of the object
print PerfStatsType.to_json()

# convert the object into a dict
perf_stats_type_dict = perf_stats_type_instance.to_dict()
# create an instance of PerfStatsType from a dict
perf_stats_type_form_dict = perf_stats_type.from_dict(perf_stats_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


