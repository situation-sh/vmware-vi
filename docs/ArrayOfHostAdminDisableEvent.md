# ArrayOfHostAdminDisableEvent

A boxed array of *HostAdminDisableEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAdminDisableEvent]**](HostAdminDisableEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_admin_disable_event import ArrayOfHostAdminDisableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAdminDisableEvent from a JSON string
array_of_host_admin_disable_event_instance = ArrayOfHostAdminDisableEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAdminDisableEvent.to_json()

# convert the object into a dict
array_of_host_admin_disable_event_dict = array_of_host_admin_disable_event_instance.to_dict()
# create an instance of ArrayOfHostAdminDisableEvent from a dict
array_of_host_admin_disable_event_form_dict = array_of_host_admin_disable_event.from_dict(array_of_host_admin_disable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


