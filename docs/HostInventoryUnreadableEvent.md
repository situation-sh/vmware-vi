# HostInventoryUnreadableEvent

Event indicating that the virtual machine inventory file on the host is damaged or unreadable.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_inventory_unreadable_event import HostInventoryUnreadableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostInventoryUnreadableEvent from a JSON string
host_inventory_unreadable_event_instance = HostInventoryUnreadableEvent.from_json(json)
# print the JSON string representation of the object
print HostInventoryUnreadableEvent.to_json()

# convert the object into a dict
host_inventory_unreadable_event_dict = host_inventory_unreadable_event_instance.to_dict()
# create an instance of HostInventoryUnreadableEvent from a dict
host_inventory_unreadable_event_form_dict = host_inventory_unreadable_event.from_dict(host_inventory_unreadable_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


