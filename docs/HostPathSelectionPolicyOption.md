# HostPathSelectionPolicyOption

Description of options associated with a native multipathing path selection policy plugin.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**ElementDescription**](ElementDescription.md) |  | 

## Example

```python
from vmware_vi.models.host_path_selection_policy_option import HostPathSelectionPolicyOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostPathSelectionPolicyOption from a JSON string
host_path_selection_policy_option_instance = HostPathSelectionPolicyOption.from_json(json)
# print the JSON string representation of the object
print HostPathSelectionPolicyOption.to_json()

# convert the object into a dict
host_path_selection_policy_option_dict = host_path_selection_policy_option_instance.to_dict()
# create an instance of HostPathSelectionPolicyOption from a dict
host_path_selection_policy_option_form_dict = host_path_selection_policy_option.from_dict(host_path_selection_policy_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


