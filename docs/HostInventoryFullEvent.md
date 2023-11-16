# HostInventoryFullEvent

This event records if the inventory of hosts has reached capacity.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** |  | 

## Example

```python
from vmware_vi.models.host_inventory_full_event import HostInventoryFullEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostInventoryFullEvent from a JSON string
host_inventory_full_event_instance = HostInventoryFullEvent.from_json(json)
# print the JSON string representation of the object
print HostInventoryFullEvent.to_json()

# convert the object into a dict
host_inventory_full_event_dict = host_inventory_full_event_instance.to_dict()
# create an instance of HostInventoryFullEvent from a dict
host_inventory_full_event_form_dict = host_inventory_full_event.from_dict(host_inventory_full_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


