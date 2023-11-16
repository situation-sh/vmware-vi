# ArrayOfDuplicateName

A boxed array of *DuplicateName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DuplicateName]**](DuplicateName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_duplicate_name import ArrayOfDuplicateName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDuplicateName from a JSON string
array_of_duplicate_name_instance = ArrayOfDuplicateName.from_json(json)
# print the JSON string representation of the object
print ArrayOfDuplicateName.to_json()

# convert the object into a dict
array_of_duplicate_name_dict = array_of_duplicate_name_instance.to_dict()
# create an instance of ArrayOfDuplicateName from a dict
array_of_duplicate_name_form_dict = array_of_duplicate_name.from_dict(array_of_duplicate_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


