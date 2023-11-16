# DvsCreatedEvent

A distributed virtual switch was created.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**FolderEventArgument**](FolderEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.dvs_created_event import DvsCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsCreatedEvent from a JSON string
dvs_created_event_instance = DvsCreatedEvent.from_json(json)
# print the JSON string representation of the object
print DvsCreatedEvent.to_json()

# convert the object into a dict
dvs_created_event_dict = dvs_created_event_instance.to_dict()
# create an instance of DvsCreatedEvent from a dict
dvs_created_event_form_dict = dvs_created_event.from_dict(dvs_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


