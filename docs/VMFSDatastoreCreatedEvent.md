# VMFSDatastoreCreatedEvent

This event records when a VMFS datastore is created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 
**datastore_url** | **str** | Url of the associated datastore.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vmfs_datastore_created_event import VMFSDatastoreCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VMFSDatastoreCreatedEvent from a JSON string
vmfs_datastore_created_event_instance = VMFSDatastoreCreatedEvent.from_json(json)
# print the JSON string representation of the object
print VMFSDatastoreCreatedEvent.to_json()

# convert the object into a dict
vmfs_datastore_created_event_dict = vmfs_datastore_created_event_instance.to_dict()
# create an instance of VMFSDatastoreCreatedEvent from a dict
vmfs_datastore_created_event_form_dict = vmfs_datastore_created_event.from_dict(vmfs_datastore_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


