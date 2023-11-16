# VmNoNetworkAccessEvent

This event records a migration failure when the destination host is not on the same network as the source host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_no_network_access_event import VmNoNetworkAccessEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmNoNetworkAccessEvent from a JSON string
vm_no_network_access_event_instance = VmNoNetworkAccessEvent.from_json(json)
# print the JSON string representation of the object
print VmNoNetworkAccessEvent.to_json()

# convert the object into a dict
vm_no_network_access_event_dict = vm_no_network_access_event_instance.to_dict()
# create an instance of VmNoNetworkAccessEvent from a dict
vm_no_network_access_event_form_dict = vm_no_network_access_event.from_dict(vm_no_network_access_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


