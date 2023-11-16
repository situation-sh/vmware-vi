# ArrayOfMissingObject

A boxed array of *MissingObject*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MissingObject]**](MissingObject.md) |  | 

## Example

```python
from vmware_vi.models.array_of_missing_object import ArrayOfMissingObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMissingObject from a JSON string
array_of_missing_object_instance = ArrayOfMissingObject.from_json(json)
# print the JSON string representation of the object
print ArrayOfMissingObject.to_json()

# convert the object into a dict
array_of_missing_object_dict = array_of_missing_object_instance.to_dict()
# create an instance of ArrayOfMissingObject from a dict
array_of_missing_object_form_dict = array_of_missing_object.from_dict(array_of_missing_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


