# DvsPortReconfiguredEvent

Existing ports are reconfigured in the distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **List[str]** | The key of the ports that are reconfigured.  ***Since:*** vSphere API 4.0  | 
**config_changes** | [**List[ChangesInfoEventArgument]**](ChangesInfoEventArgument.md) | The configuration values changed during the reconfiguration.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_port_reconfigured_event import DvsPortReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortReconfiguredEvent from a JSON string
dvs_port_reconfigured_event_instance = DvsPortReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortReconfiguredEvent.to_json()

# convert the object into a dict
dvs_port_reconfigured_event_dict = dvs_port_reconfigured_event_instance.to_dict()
# create an instance of DvsPortReconfiguredEvent from a dict
dvs_port_reconfigured_event_form_dict = dvs_port_reconfigured_event.from_dict(dvs_port_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


