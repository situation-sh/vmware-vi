# ArrayOfPerfStatsType

A boxed array of *PerfStatsType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfStatsTypeEnum]**](PerfStatsTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_stats_type import ArrayOfPerfStatsType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfStatsType from a JSON string
array_of_perf_stats_type_instance = ArrayOfPerfStatsType.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfStatsType.to_json()

# convert the object into a dict
array_of_perf_stats_type_dict = array_of_perf_stats_type_instance.to_dict()
# create an instance of ArrayOfPerfStatsType from a dict
array_of_perf_stats_type_form_dict = array_of_perf_stats_type.from_dict(array_of_perf_stats_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


