# ArrayOfFileQuery

A boxed array of *FileQuery*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FileQuery]**](FileQuery.md) |  | 

## Example

```python
from vmware_vi.models.array_of_file_query import ArrayOfFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFileQuery from a JSON string
array_of_file_query_instance = ArrayOfFileQuery.from_json(json)
# print the JSON string representation of the object
print ArrayOfFileQuery.to_json()

# convert the object into a dict
array_of_file_query_dict = array_of_file_query_instance.to_dict()
# create an instance of ArrayOfFileQuery from a dict
array_of_file_query_form_dict = array_of_file_query.from_dict(array_of_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


