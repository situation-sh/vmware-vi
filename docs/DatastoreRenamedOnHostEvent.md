# DatastoreRenamedOnHostEvent

This event records when a datastore is added to VirtualCenter and is renamed by VirtualCenter because this datastore already exists in VirtualCenter with a different name, or because the name conflicts with another datastore in VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old datastore name.  | 
**new_name** | **str** | The new datastore name.  | 

## Example

```python
from vmware_vi.models.datastore_renamed_on_host_event import DatastoreRenamedOnHostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreRenamedOnHostEvent from a JSON string
datastore_renamed_on_host_event_instance = DatastoreRenamedOnHostEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreRenamedOnHostEvent.to_json()

# convert the object into a dict
datastore_renamed_on_host_event_dict = datastore_renamed_on_host_event_instance.to_dict()
# create an instance of DatastoreRenamedOnHostEvent from a dict
datastore_renamed_on_host_event_form_dict = datastore_renamed_on_host_event.from_dict(datastore_renamed_on_host_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


