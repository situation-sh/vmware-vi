# DvsPortCreatedEvent

New ports are created in the distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **List[str]** | The key of the ports that are created.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_port_created_event import DvsPortCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortCreatedEvent from a JSON string
dvs_port_created_event_instance = DvsPortCreatedEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortCreatedEvent.to_json()

# convert the object into a dict
dvs_port_created_event_dict = dvs_port_created_event_instance.to_dict()
# create an instance of DvsPortCreatedEvent from a dict
dvs_port_created_event_form_dict = dvs_port_created_event.from_dict(dvs_port_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


