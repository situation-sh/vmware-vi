# DvsHostJoinedEvent

A host joined the distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_joined** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.dvs_host_joined_event import DvsHostJoinedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostJoinedEvent from a JSON string
dvs_host_joined_event_instance = DvsHostJoinedEvent.from_json(json)
# print the JSON string representation of the object
print DvsHostJoinedEvent.to_json()

# convert the object into a dict
dvs_host_joined_event_dict = dvs_host_joined_event_instance.to_dict()
# create an instance of DvsHostJoinedEvent from a dict
dvs_host_joined_event_form_dict = dvs_host_joined_event.from_dict(dvs_host_joined_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


