# ArrayOfHostHyperThreadScheduleInfo

A boxed array of *HostHyperThreadScheduleInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostHyperThreadScheduleInfo]**](HostHyperThreadScheduleInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_hyper_thread_schedule_info import ArrayOfHostHyperThreadScheduleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostHyperThreadScheduleInfo from a JSON string
array_of_host_hyper_thread_schedule_info_instance = ArrayOfHostHyperThreadScheduleInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostHyperThreadScheduleInfo.to_json()

# convert the object into a dict
array_of_host_hyper_thread_schedule_info_dict = array_of_host_hyper_thread_schedule_info_instance.to_dict()
# create an instance of ArrayOfHostHyperThreadScheduleInfo from a dict
array_of_host_hyper_thread_schedule_info_form_dict = array_of_host_hyper_thread_schedule_info.from_dict(array_of_host_hyper_thread_schedule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


