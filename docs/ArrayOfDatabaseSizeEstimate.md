# ArrayOfDatabaseSizeEstimate

A boxed array of *DatabaseSizeEstimate*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatabaseSizeEstimate]**](DatabaseSizeEstimate.md) |  | 

## Example

```python
from vmware_vi.models.array_of_database_size_estimate import ArrayOfDatabaseSizeEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatabaseSizeEstimate from a JSON string
array_of_database_size_estimate_instance = ArrayOfDatabaseSizeEstimate.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatabaseSizeEstimate.to_json()

# convert the object into a dict
array_of_database_size_estimate_dict = array_of_database_size_estimate_instance.to_dict()
# create an instance of ArrayOfDatabaseSizeEstimate from a dict
array_of_database_size_estimate_form_dict = array_of_database_size_estimate.from_dict(array_of_database_size_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


