# ArrayOfExtSolutionManagerInfo

A boxed array of *ExtSolutionManagerInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtSolutionManagerInfo]**](ExtSolutionManagerInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ext_solution_manager_info import ArrayOfExtSolutionManagerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtSolutionManagerInfo from a JSON string
array_of_ext_solution_manager_info_instance = ArrayOfExtSolutionManagerInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtSolutionManagerInfo.to_json()

# convert the object into a dict
array_of_ext_solution_manager_info_dict = array_of_ext_solution_manager_info_instance.to_dict()
# create an instance of ArrayOfExtSolutionManagerInfo from a dict
array_of_ext_solution_manager_info_form_dict = array_of_ext_solution_manager_info.from_dict(array_of_ext_solution_manager_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


