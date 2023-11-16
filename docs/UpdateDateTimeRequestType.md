# UpdateDateTimeRequestType

The parameters of *HostDateTimeSystem.UpdateDateTime*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** | **datetime** | DateTime to update the host to.  | 

## Example

```python
from vmware_vi.models.update_date_time_request_type import UpdateDateTimeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDateTimeRequestType from a JSON string
update_date_time_request_type_instance = UpdateDateTimeRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDateTimeRequestType.to_json()

# convert the object into a dict
update_date_time_request_type_dict = update_date_time_request_type_instance.to_dict()
# create an instance of UpdateDateTimeRequestType from a dict
update_date_time_request_type_form_dict = update_date_time_request_type.from_dict(update_date_time_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


