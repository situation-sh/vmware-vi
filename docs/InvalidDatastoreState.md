# InvalidDatastoreState

The datastore is in an invalid state (e.g., maintenance mode) for a given operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_name** | **str** | The name of the datastore.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.invalid_datastore_state import InvalidDatastoreState

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDatastoreState from a JSON string
invalid_datastore_state_instance = InvalidDatastoreState.from_json(json)
# print the JSON string representation of the object
print InvalidDatastoreState.to_json()

# convert the object into a dict
invalid_datastore_state_dict = invalid_datastore_state_instance.to_dict()
# create an instance of InvalidDatastoreState from a dict
invalid_datastore_state_form_dict = invalid_datastore_state.from_dict(invalid_datastore_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


