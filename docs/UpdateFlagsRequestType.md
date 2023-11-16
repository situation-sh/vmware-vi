# UpdateFlagsRequestType

The parameters of *HostSystem.UpdateFlags*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag_info** | [**HostFlagInfo**](HostFlagInfo.md) |  | 

## Example

```python
from vmware_vi.models.update_flags_request_type import UpdateFlagsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFlagsRequestType from a JSON string
update_flags_request_type_instance = UpdateFlagsRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateFlagsRequestType.to_json()

# convert the object into a dict
update_flags_request_type_dict = update_flags_request_type_instance.to_dict()
# create an instance of UpdateFlagsRequestType from a dict
update_flags_request_type_form_dict = update_flags_request_type.from_dict(update_flags_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


