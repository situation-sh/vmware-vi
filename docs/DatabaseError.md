# DatabaseError

A DatabaseError exception is thrown if an operation failed when accessing the external database.  This typically is because the database is (temporarily) unavailable or because of network problems. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.database_error import DatabaseError

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseError from a JSON string
database_error_instance = DatabaseError.from_json(json)
# print the JSON string representation of the object
print DatabaseError.to_json()

# convert the object into a dict
database_error_dict = database_error_instance.to_dict()
# create an instance of DatabaseError from a dict
database_error_form_dict = database_error.from_dict(database_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


