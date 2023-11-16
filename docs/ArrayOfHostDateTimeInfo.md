# ArrayOfHostDateTimeInfo

A boxed array of *HostDateTimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDateTimeInfo]**](HostDateTimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_date_time_info import ArrayOfHostDateTimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDateTimeInfo from a JSON string
array_of_host_date_time_info_instance = ArrayOfHostDateTimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDateTimeInfo.to_json()

# convert the object into a dict
array_of_host_date_time_info_dict = array_of_host_date_time_info_instance.to_dict()
# create an instance of ArrayOfHostDateTimeInfo from a dict
array_of_host_date_time_info_form_dict = array_of_host_date_time_info.from_dict(array_of_host_date_time_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


