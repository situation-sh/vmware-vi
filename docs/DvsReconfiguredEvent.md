# DvsReconfiguredEvent

A distributed virtual switch was reconfigured.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**DVSConfigSpec**](DVSConfigSpec.md) |  | 
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_reconfigured_event import DvsReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsReconfiguredEvent from a JSON string
dvs_reconfigured_event_instance = DvsReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print DvsReconfiguredEvent.to_json()

# convert the object into a dict
dvs_reconfigured_event_dict = dvs_reconfigured_event_instance.to_dict()
# create an instance of DvsReconfiguredEvent from a dict
dvs_reconfigured_event_form_dict = dvs_reconfigured_event.from_dict(dvs_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


