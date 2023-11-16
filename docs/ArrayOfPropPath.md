# ArrayOfPropPath

A boxed array of *PrimitivePropPath*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[str]** |  | 

## Example

```python
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPropPath from a JSON string
array_of_prop_path_instance = ArrayOfPropPath.from_json(json)
# print the JSON string representation of the object
print ArrayOfPropPath.to_json()

# convert the object into a dict
array_of_prop_path_dict = array_of_prop_path_instance.to_dict()
# create an instance of ArrayOfPropPath from a dict
array_of_prop_path_form_dict = array_of_prop_path.from_dict(array_of_prop_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


