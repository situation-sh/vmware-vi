# ArrayOfPerfSummaryType

A boxed array of *PerfSummaryType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfSummaryTypeEnum]**](PerfSummaryTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_summary_type import ArrayOfPerfSummaryType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfSummaryType from a JSON string
array_of_perf_summary_type_instance = ArrayOfPerfSummaryType.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfSummaryType.to_json()

# convert the object into a dict
array_of_perf_summary_type_dict = array_of_perf_summary_type_instance.to_dict()
# create an instance of ArrayOfPerfSummaryType from a dict
array_of_perf_summary_type_form_dict = array_of_perf_summary_type.from_dict(array_of_perf_summary_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


