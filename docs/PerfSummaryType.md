# PerfSummaryType

A boxed *PerfSummaryType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PerfSummaryTypeEnum**](PerfSummaryTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.perf_summary_type import PerfSummaryType

# TODO update the JSON string below
json = "{}"
# create an instance of PerfSummaryType from a JSON string
perf_summary_type_instance = PerfSummaryType.from_json(json)
# print the JSON string representation of the object
print PerfSummaryType.to_json()

# convert the object into a dict
perf_summary_type_dict = perf_summary_type_instance.to_dict()
# create an instance of PerfSummaryType from a dict
perf_summary_type_form_dict = perf_summary_type.from_dict(perf_summary_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


