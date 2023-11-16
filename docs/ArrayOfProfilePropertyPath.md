# ArrayOfProfilePropertyPath

A boxed array of *ProfilePropertyPath*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfilePropertyPath]**](ProfilePropertyPath.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_property_path import ArrayOfProfilePropertyPath

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfilePropertyPath from a JSON string
array_of_profile_property_path_instance = ArrayOfProfilePropertyPath.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfilePropertyPath.to_json()

# convert the object into a dict
array_of_profile_property_path_dict = array_of_profile_property_path_instance.to_dict()
# create an instance of ArrayOfProfilePropertyPath from a dict
array_of_profile_property_path_form_dict = array_of_profile_property_path.from_dict(array_of_profile_property_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


