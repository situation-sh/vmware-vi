# ArrayOfPerfQuerySpec

A boxed array of *PerfQuerySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfQuerySpec]**](PerfQuerySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_query_spec import ArrayOfPerfQuerySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfQuerySpec from a JSON string
array_of_perf_query_spec_instance = ArrayOfPerfQuerySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfQuerySpec.to_json()

# convert the object into a dict
array_of_perf_query_spec_dict = array_of_perf_query_spec_instance.to_dict()
# create an instance of ArrayOfPerfQuerySpec from a dict
array_of_perf_query_spec_form_dict = array_of_perf_query_spec.from_dict(array_of_perf_query_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


