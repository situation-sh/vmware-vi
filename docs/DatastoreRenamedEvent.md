# DatastoreRenamedEvent

This event records the renaming of a datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old datastore name.  | 
**new_name** | **str** | The new datastore name.  | 

## Example

```python
from vmware_vi.models.datastore_renamed_event import DatastoreRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreRenamedEvent from a JSON string
datastore_renamed_event_instance = DatastoreRenamedEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreRenamedEvent.to_json()

# convert the object into a dict
datastore_renamed_event_dict = datastore_renamed_event_instance.to_dict()
# create an instance of DatastoreRenamedEvent from a dict
datastore_renamed_event_form_dict = datastore_renamed_event.from_dict(datastore_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


