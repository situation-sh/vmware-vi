# DatastoreFileMovedEvent

This event records move of a file or directory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 
**source_file** | **str** | Datastore path of the source file or directory.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.datastore_file_moved_event import DatastoreFileMovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreFileMovedEvent from a JSON string
datastore_file_moved_event_instance = DatastoreFileMovedEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreFileMovedEvent.to_json()

# convert the object into a dict
datastore_file_moved_event_dict = datastore_file_moved_event_instance.to_dict()
# create an instance of DatastoreFileMovedEvent from a dict
datastore_file_moved_event_form_dict = datastore_file_moved_event.from_dict(datastore_file_moved_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


