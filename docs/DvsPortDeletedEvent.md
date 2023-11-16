# DvsPortDeletedEvent

Existing ports are deleted in the distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **List[str]** | The key of the ports that are deleted.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_port_deleted_event import DvsPortDeletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortDeletedEvent from a JSON string
dvs_port_deleted_event_instance = DvsPortDeletedEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortDeletedEvent.to_json()

# convert the object into a dict
dvs_port_deleted_event_dict = dvs_port_deleted_event_instance.to_dict()
# create an instance of DvsPortDeletedEvent from a dict
dvs_port_deleted_event_form_dict = dvs_port_deleted_event.from_dict(dvs_port_deleted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


