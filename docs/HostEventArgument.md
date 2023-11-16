# HostEventArgument

The event argument is a Host object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_event_argument import HostEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of HostEventArgument from a JSON string
host_event_argument_instance = HostEventArgument.from_json(json)
# print the JSON string representation of the object
print HostEventArgument.to_json()

# convert the object into a dict
host_event_argument_dict = host_event_argument_instance.to_dict()
# create an instance of HostEventArgument from a dict
host_event_argument_form_dict = host_event_argument.from_dict(host_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


