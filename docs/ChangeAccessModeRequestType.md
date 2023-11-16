# ChangeAccessModeRequestType

The parameters of *HostAccessManager.ChangeAccessMode*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** | The affected user or group.  | 
**is_group** | **bool** | True if principal refers to a group account, false otherwise.  | 
**access_mode** | [**HostAccessModeEnum**](HostAccessModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.change_access_mode_request_type import ChangeAccessModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAccessModeRequestType from a JSON string
change_access_mode_request_type_instance = ChangeAccessModeRequestType.from_json(json)
# print the JSON string representation of the object
print ChangeAccessModeRequestType.to_json()

# convert the object into a dict
change_access_mode_request_type_dict = change_access_mode_request_type_instance.to_dict()
# create an instance of ChangeAccessModeRequestType from a dict
change_access_mode_request_type_form_dict = change_access_mode_request_type.from_dict(change_access_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


