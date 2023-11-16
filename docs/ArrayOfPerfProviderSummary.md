# ArrayOfPerfProviderSummary

A boxed array of *PerfProviderSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfProviderSummary]**](PerfProviderSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_provider_summary import ArrayOfPerfProviderSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfProviderSummary from a JSON string
array_of_perf_provider_summary_instance = ArrayOfPerfProviderSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfProviderSummary.to_json()

# convert the object into a dict
array_of_perf_provider_summary_dict = array_of_perf_provider_summary_instance.to_dict()
# create an instance of ArrayOfPerfProviderSummary from a dict
array_of_perf_provider_summary_form_dict = array_of_perf_provider_summary.from_dict(array_of_perf_provider_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


