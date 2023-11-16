# ArrayOfInvalidDatastore

A boxed array of *InvalidDatastore*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidDatastore]**](InvalidDatastore.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_datastore import ArrayOfInvalidDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidDatastore from a JSON string
array_of_invalid_datastore_instance = ArrayOfInvalidDatastore.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidDatastore.to_json()

# convert the object into a dict
array_of_invalid_datastore_dict = array_of_invalid_datastore_instance.to_dict()
# create an instance of ArrayOfInvalidDatastore from a dict
array_of_invalid_datastore_form_dict = array_of_invalid_datastore.from_dict(array_of_invalid_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


