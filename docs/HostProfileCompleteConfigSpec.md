# HostProfileCompleteConfigSpec

The *HostProfileCompleteConfigSpec* data object specifies the complete configuration for a host profile.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_profile** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**custom_comply_profile** | [**ComplianceProfile**](ComplianceProfile.md) |  | [optional] 
**disabled_expression_list_changed** | **bool** | Flag indicating if this configuration specification contains changes in the *HostProfileCompleteConfigSpec.disabledExpressionList*.  If False, the Profile Engine ignores the contents of the disabled expression list.  ***Since:*** vSphere API 4.0  | 
**disabled_expression_list** | **List[str]** | List of expressions to be disabled.  Each entry in the list specifies a *ProfileExpression*.*ProfileExpression.id*. All expressions are enabled by default.  If you set *HostProfileCompleteConfigSpec.disabledExpressionListChanged* to True, the Profile Engine uses the contents of this list to replace the contents of the *HostProfile*.*Profile.config*.*HostProfileConfigInfo.disabledExpressionList*.  The expression list is contained in the *HostProfileConfigInfo.defaultComplyProfile*. The Profile Engine automatically generates the default compliance profile when you create a host profile.  ***Since:*** vSphere API 4.0  | [optional] 
**validator_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**validating** | **bool** | If \&quot;false\&quot;, then the host profile will be saved without being validated.  The default if not specified is \&quot;true\&quot;. This option should be used with caution, since the resulting host profile will not be checked for errors.  ***Since:*** vSphere API 6.0  | [optional] 
**host_config** | [**HostProfileConfigInfo**](HostProfileConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_complete_config_spec import HostProfileCompleteConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileCompleteConfigSpec from a JSON string
host_profile_complete_config_spec_instance = HostProfileCompleteConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostProfileCompleteConfigSpec.to_json()

# convert the object into a dict
host_profile_complete_config_spec_dict = host_profile_complete_config_spec_instance.to_dict()
# create an instance of HostProfileCompleteConfigSpec from a dict
host_profile_complete_config_spec_form_dict = host_profile_complete_config_spec.from_dict(host_profile_complete_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


