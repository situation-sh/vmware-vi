# UpdateHostProfileRequestType

The parameters of *HostProfile.UpdateHostProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**HostProfileConfigSpec**](HostProfileConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_host_profile_request_type import UpdateHostProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostProfileRequestType from a JSON string
update_host_profile_request_type_instance = UpdateHostProfileRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateHostProfileRequestType.to_json()

# convert the object into a dict
update_host_profile_request_type_dict = update_host_profile_request_type_instance.to_dict()
# create an instance of UpdateHostProfileRequestType from a dict
update_host_profile_request_type_form_dict = update_host_profile_request_type.from_dict(update_host_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


