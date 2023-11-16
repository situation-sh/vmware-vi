# DatastoreFileEvent

Base class for events related to datastore file and directory operations.  Property _datastore_ inherited from DatastoreEvent refers to the destination datastore in case there is more than datastore involved in the operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_file** | **str** | Datastore path of the target file or directory.  ***Since:*** vSphere API 4.0  | 
**source_of_operation** | **str** | Identifier of the initiator of the file operation.  ***Since:*** vSphere API 6.5  | [optional] 
**succeeded** | **bool** | Indicator whether the datastore file operation succeeded.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.datastore_file_event import DatastoreFileEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreFileEvent from a JSON string
datastore_file_event_instance = DatastoreFileEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreFileEvent.to_json()

# convert the object into a dict
datastore_file_event_dict = datastore_file_event_instance.to_dict()
# create an instance of DatastoreFileEvent from a dict
datastore_file_event_form_dict = datastore_file_event.from_dict(datastore_file_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


