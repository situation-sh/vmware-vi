# ExtSolutionManagerInfo

This data object encapsulates the Solution Manager configuration for this extension.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tab** | [**List[ExtSolutionManagerInfoTabInfo]**](ExtSolutionManagerInfoTabInfo.md) | Deprecated as of vSphere API 5.1, see client documentation for the preferred way to integrate custom user interfaces.  List of tabs that must be shown in the Solution Manager for this extension.  Tabs are shown ordered by their position in this array.  ***Since:*** vSphere API 5.0  | [optional] 
**small_icon_url** | **str** | URL for an icon for this extension.  The icon will be shown in the Solution Manager for this extension. The icon must be 16x16, and should be in PNG format.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.ext_solution_manager_info import ExtSolutionManagerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtSolutionManagerInfo from a JSON string
ext_solution_manager_info_instance = ExtSolutionManagerInfo.from_json(json)
# print the JSON string representation of the object
print ExtSolutionManagerInfo.to_json()

# convert the object into a dict
ext_solution_manager_info_dict = ext_solution_manager_info_instance.to_dict()
# create an instance of ExtSolutionManagerInfo from a dict
ext_solution_manager_info_form_dict = ext_solution_manager_info.from_dict(ext_solution_manager_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


