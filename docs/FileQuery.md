# FileQuery

The data object type that describes the base query specification.  Contains query filters and details that apply to every file. Querying only file details generally does not require opening files and so is an efficient query. Derived types add query parameters specific to the type of file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_query import FileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FileQuery from a JSON string
file_query_instance = FileQuery.from_json(json)
# print the JSON string representation of the object
print FileQuery.to_json()

# convert the object into a dict
file_query_dict = file_query_instance.to_dict()
# create an instance of FileQuery from a dict
file_query_form_dict = file_query.from_dict(file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


