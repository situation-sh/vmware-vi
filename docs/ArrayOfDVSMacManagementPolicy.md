# ArrayOfDVSMacManagementPolicy

A boxed array of *DVSMacManagementPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSMacManagementPolicy]**](DVSMacManagementPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_mac_management_policy import ArrayOfDVSMacManagementPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSMacManagementPolicy from a JSON string
array_of_dvs_mac_management_policy_instance = ArrayOfDVSMacManagementPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSMacManagementPolicy.to_json()

# convert the object into a dict
array_of_dvs_mac_management_policy_dict = array_of_dvs_mac_management_policy_instance.to_dict()
# create an instance of ArrayOfDVSMacManagementPolicy from a dict
array_of_dvs_mac_management_policy_form_dict = array_of_dvs_mac_management_policy.from_dict(array_of_dvs_mac_management_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


