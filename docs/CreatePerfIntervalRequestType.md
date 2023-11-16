# CreatePerfIntervalRequestType

The parameters of *PerformanceManager.CreatePerfInterval*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_id** | [**PerfInterval**](PerfInterval.md) |  | 

## Example

```python
from vmware_vi.models.create_perf_interval_request_type import CreatePerfIntervalRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePerfIntervalRequestType from a JSON string
create_perf_interval_request_type_instance = CreatePerfIntervalRequestType.from_json(json)
# print the JSON string representation of the object
print CreatePerfIntervalRequestType.to_json()

# convert the object into a dict
create_perf_interval_request_type_dict = create_perf_interval_request_type_instance.to_dict()
# create an instance of CreatePerfIntervalRequestType from a dict
create_perf_interval_request_type_form_dict = create_perf_interval_request_type.from_dict(create_perf_interval_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


