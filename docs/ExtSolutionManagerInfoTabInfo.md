# ExtSolutionManagerInfoTabInfo

Deprecated as of vSphere API 5.1.  This data object contains information about a tab to show in the Solution Manager for this extension.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the tab.  ***Since:*** vSphere API 5.0  | 
**url** | **str** | The URL for the webpage to show in the tab.  Extra parameters will be added to this URL when vSphere Client loads it. See the \&quot;Customizing the vSphere Client\&quot; technical note for more information.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ext_solution_manager_info_tab_info import ExtSolutionManagerInfoTabInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtSolutionManagerInfoTabInfo from a JSON string
ext_solution_manager_info_tab_info_instance = ExtSolutionManagerInfoTabInfo.from_json(json)
# print the JSON string representation of the object
print ExtSolutionManagerInfoTabInfo.to_json()

# convert the object into a dict
ext_solution_manager_info_tab_info_dict = ext_solution_manager_info_tab_info_instance.to_dict()
# create an instance of ExtSolutionManagerInfoTabInfo from a dict
ext_solution_manager_info_tab_info_form_dict = ext_solution_manager_info_tab_info.from_dict(ext_solution_manager_info_tab_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


