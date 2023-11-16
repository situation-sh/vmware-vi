# DrsResourceConfigureFailedEvent

This event records when resource configuration specification synchronization fails on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.drs_resource_configure_failed_event import DrsResourceConfigureFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsResourceConfigureFailedEvent from a JSON string
drs_resource_configure_failed_event_instance = DrsResourceConfigureFailedEvent.from_json(json)
# print the JSON string representation of the object
print DrsResourceConfigureFailedEvent.to_json()

# convert the object into a dict
drs_resource_configure_failed_event_dict = drs_resource_configure_failed_event_instance.to_dict()
# create an instance of DrsResourceConfigureFailedEvent from a dict
drs_resource_configure_failed_event_form_dict = drs_resource_configure_failed_event.from_dict(drs_resource_configure_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


