# ArrayOfDatabaseSizeParam

A boxed array of *DatabaseSizeParam*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatabaseSizeParam]**](DatabaseSizeParam.md) |  | 

## Example

```python
from vmware_vi.models.array_of_database_size_param import ArrayOfDatabaseSizeParam

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatabaseSizeParam from a JSON string
array_of_database_size_param_instance = ArrayOfDatabaseSizeParam.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatabaseSizeParam.to_json()

# convert the object into a dict
array_of_database_size_param_dict = array_of_database_size_param_instance.to_dict()
# create an instance of ArrayOfDatabaseSizeParam from a dict
array_of_database_size_param_form_dict = array_of_database_size_param.from_dict(array_of_database_size_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


