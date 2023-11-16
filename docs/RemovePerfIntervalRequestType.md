# RemovePerfIntervalRequestType

The parameters of *PerformanceManager.RemovePerfInterval*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_period** | **int** | The sampling period, in seconds, for the specified interval being removed.  | 

## Example

```python
from vmware_vi.models.remove_perf_interval_request_type import RemovePerfIntervalRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemovePerfIntervalRequestType from a JSON string
remove_perf_interval_request_type_instance = RemovePerfIntervalRequestType.from_json(json)
# print the JSON string representation of the object
print RemovePerfIntervalRequestType.to_json()

# convert the object into a dict
remove_perf_interval_request_type_dict = remove_perf_interval_request_type_instance.to_dict()
# create an instance of RemovePerfIntervalRequestType from a dict
remove_perf_interval_request_type_form_dict = remove_perf_interval_request_type.from_dict(remove_perf_interval_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


