# UpdatePerfIntervalRequestType

The parameters of *PerformanceManager.UpdatePerfInterval*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**PerfInterval**](PerfInterval.md) |  | 

## Example

```python
from vmware_vi.models.update_perf_interval_request_type import UpdatePerfIntervalRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePerfIntervalRequestType from a JSON string
update_perf_interval_request_type_instance = UpdatePerfIntervalRequestType.from_json(json)
# print the JSON string representation of the object
print UpdatePerfIntervalRequestType.to_json()

# convert the object into a dict
update_perf_interval_request_type_dict = update_perf_interval_request_type_instance.to_dict()
# create an instance of UpdatePerfIntervalRequestType from a dict
update_perf_interval_request_type_form_dict = update_perf_interval_request_type.from_dict(update_perf_interval_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


