# ArrayOfHostInventoryFullEvent

A boxed array of *HostInventoryFullEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInventoryFullEvent]**](HostInventoryFullEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_inventory_full_event import ArrayOfHostInventoryFullEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInventoryFullEvent from a JSON string
array_of_host_inventory_full_event_instance = ArrayOfHostInventoryFullEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInventoryFullEvent.to_json()

# convert the object into a dict
array_of_host_inventory_full_event_dict = array_of_host_inventory_full_event_instance.to_dict()
# create an instance of ArrayOfHostInventoryFullEvent from a dict
array_of_host_inventory_full_event_form_dict = array_of_host_inventory_full_event.from_dict(array_of_host_inventory_full_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


