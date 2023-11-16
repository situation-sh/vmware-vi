# ArrayOfAdminPasswordNotChangedEvent

A boxed array of *AdminPasswordNotChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AdminPasswordNotChangedEvent]**](AdminPasswordNotChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_admin_password_not_changed_event import ArrayOfAdminPasswordNotChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAdminPasswordNotChangedEvent from a JSON string
array_of_admin_password_not_changed_event_instance = ArrayOfAdminPasswordNotChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAdminPasswordNotChangedEvent.to_json()

# convert the object into a dict
array_of_admin_password_not_changed_event_dict = array_of_admin_password_not_changed_event_instance.to_dict()
# create an instance of ArrayOfAdminPasswordNotChangedEvent from a dict
array_of_admin_password_not_changed_event_form_dict = array_of_admin_password_not_changed_event.from_dict(array_of_admin_password_not_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


