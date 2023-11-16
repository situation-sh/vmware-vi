# DatastoreFileDeletedEvent

This event records deletion of a file or directory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.datastore_file_deleted_event import DatastoreFileDeletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreFileDeletedEvent from a JSON string
datastore_file_deleted_event_instance = DatastoreFileDeletedEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreFileDeletedEvent.to_json()

# convert the object into a dict
datastore_file_deleted_event_dict = datastore_file_deleted_event_instance.to_dict()
# create an instance of DatastoreFileDeletedEvent from a dict
datastore_file_deleted_event_form_dict = datastore_file_deleted_event.from_dict(datastore_file_deleted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


