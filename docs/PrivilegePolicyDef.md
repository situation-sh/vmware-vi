# PrivilegePolicyDef

Describes a basic privilege policy.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_privilege** | **str** | Name of privilege required for creation.  ***Since:*** VI API 2.5  | 
**read_privilege** | **str** | Name of privilege required for reading.  ***Since:*** VI API 2.5  | 
**update_privilege** | **str** | Name of privilege required for updating.  ***Since:*** VI API 2.5  | 
**delete_privilege** | **str** | Name of privilege required for deleting.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.privilege_policy_def import PrivilegePolicyDef

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegePolicyDef from a JSON string
privilege_policy_def_instance = PrivilegePolicyDef.from_json(json)
# print the JSON string representation of the object
print PrivilegePolicyDef.to_json()

# convert the object into a dict
privilege_policy_def_dict = privilege_policy_def_instance.to_dict()
# create an instance of PrivilegePolicyDef from a dict
privilege_policy_def_form_dict = privilege_policy_def.from_dict(privilege_policy_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


