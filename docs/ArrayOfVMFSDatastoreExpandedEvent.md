# ArrayOfVMFSDatastoreExpandedEvent

A boxed array of *VMFSDatastoreExpandedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMFSDatastoreExpandedEvent]**](VMFSDatastoreExpandedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_datastore_expanded_event import ArrayOfVMFSDatastoreExpandedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMFSDatastoreExpandedEvent from a JSON string
array_of_vmfs_datastore_expanded_event_instance = ArrayOfVMFSDatastoreExpandedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMFSDatastoreExpandedEvent.to_json()

# convert the object into a dict
array_of_vmfs_datastore_expanded_event_dict = array_of_vmfs_datastore_expanded_event_instance.to_dict()
# create an instance of ArrayOfVMFSDatastoreExpandedEvent from a dict
array_of_vmfs_datastore_expanded_event_form_dict = array_of_vmfs_datastore_expanded_event.from_dict(array_of_vmfs_datastore_expanded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


