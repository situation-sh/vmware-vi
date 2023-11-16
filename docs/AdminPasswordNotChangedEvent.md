# AdminPasswordNotChangedEvent

Default password for the Admin user on the host has not been changed.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.admin_password_not_changed_event import AdminPasswordNotChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPasswordNotChangedEvent from a JSON string
admin_password_not_changed_event_instance = AdminPasswordNotChangedEvent.from_json(json)
# print the JSON string representation of the object
print AdminPasswordNotChangedEvent.to_json()

# convert the object into a dict
admin_password_not_changed_event_dict = admin_password_not_changed_event_instance.to_dict()
# create an instance of AdminPasswordNotChangedEvent from a dict
admin_password_not_changed_event_form_dict = admin_password_not_changed_event.from_dict(admin_password_not_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


