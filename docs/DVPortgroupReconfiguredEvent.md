# DVPortgroupReconfiguredEvent

Two distributed virtual portgroup was reconfigured.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**DVPortgroupConfigSpec**](DVPortgroupConfigSpec.md) |  | 
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dv_portgroup_reconfigured_event import DVPortgroupReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupReconfiguredEvent from a JSON string
dv_portgroup_reconfigured_event_instance = DVPortgroupReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print DVPortgroupReconfiguredEvent.to_json()

# convert the object into a dict
dv_portgroup_reconfigured_event_dict = dv_portgroup_reconfigured_event_instance.to_dict()
# create an instance of DVPortgroupReconfiguredEvent from a dict
dv_portgroup_reconfigured_event_form_dict = dv_portgroup_reconfigured_event.from_dict(dv_portgroup_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


