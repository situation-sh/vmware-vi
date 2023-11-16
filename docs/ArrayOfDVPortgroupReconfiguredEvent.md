# ArrayOfDVPortgroupReconfiguredEvent

A boxed array of *DVPortgroupReconfiguredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVPortgroupReconfiguredEvent]**](DVPortgroupReconfiguredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dv_portgroup_reconfigured_event import ArrayOfDVPortgroupReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVPortgroupReconfiguredEvent from a JSON string
array_of_dv_portgroup_reconfigured_event_instance = ArrayOfDVPortgroupReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVPortgroupReconfiguredEvent.to_json()

# convert the object into a dict
array_of_dv_portgroup_reconfigured_event_dict = array_of_dv_portgroup_reconfigured_event_instance.to_dict()
# create an instance of ArrayOfDVPortgroupReconfiguredEvent from a dict
array_of_dv_portgroup_reconfigured_event_form_dict = array_of_dv_portgroup_reconfigured_event.from_dict(array_of_dv_portgroup_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


