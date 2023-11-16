# VMFSDatastoreExpandedEvent

This event records when a datastore is expanded.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_expanded_event import VMFSDatastoreExpandedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VMFSDatastoreExpandedEvent from a JSON string
vmfs_datastore_expanded_event_instance = VMFSDatastoreExpandedEvent.from_json(json)
# print the JSON string representation of the object
print VMFSDatastoreExpandedEvent.to_json()

# convert the object into a dict
vmfs_datastore_expanded_event_dict = vmfs_datastore_expanded_event_instance.to_dict()
# create an instance of VMFSDatastoreExpandedEvent from a dict
vmfs_datastore_expanded_event_form_dict = vmfs_datastore_expanded_event.from_dict(vmfs_datastore_expanded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


