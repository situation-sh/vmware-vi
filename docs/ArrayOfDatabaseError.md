# ArrayOfDatabaseError

A boxed array of *DatabaseError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatabaseError]**](DatabaseError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_database_error import ArrayOfDatabaseError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatabaseError from a JSON string
array_of_database_error_instance = ArrayOfDatabaseError.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatabaseError.to_json()

# convert the object into a dict
array_of_database_error_dict = array_of_database_error_instance.to_dict()
# create an instance of ArrayOfDatabaseError from a dict
array_of_database_error_form_dict = array_of_database_error.from_dict(array_of_database_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


