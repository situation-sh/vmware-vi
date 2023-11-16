# VMFSDatastoreExtendedEvent

This event records when a datastore is extended.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_extended_event import VMFSDatastoreExtendedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VMFSDatastoreExtendedEvent from a JSON string
vmfs_datastore_extended_event_instance = VMFSDatastoreExtendedEvent.from_json(json)
# print the JSON string representation of the object
print VMFSDatastoreExtendedEvent.to_json()

# convert the object into a dict
vmfs_datastore_extended_event_dict = vmfs_datastore_extended_event_instance.to_dict()
# create an instance of VMFSDatastoreExtendedEvent from a dict
vmfs_datastore_extended_event_form_dict = vmfs_datastore_extended_event.from_dict(vmfs_datastore_extended_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


