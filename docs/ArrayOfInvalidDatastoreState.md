# ArrayOfInvalidDatastoreState

A boxed array of *InvalidDatastoreState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidDatastoreState]**](InvalidDatastoreState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_datastore_state import ArrayOfInvalidDatastoreState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidDatastoreState from a JSON string
array_of_invalid_datastore_state_instance = ArrayOfInvalidDatastoreState.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidDatastoreState.to_json()

# convert the object into a dict
array_of_invalid_datastore_state_dict = array_of_invalid_datastore_state_instance.to_dict()
# create an instance of ArrayOfInvalidDatastoreState from a dict
array_of_invalid_datastore_state_form_dict = array_of_invalid_datastore_state.from_dict(array_of_invalid_datastore_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


