# HostProfileConfigInfo

The *HostProfileConfigInfo* data object contains host profile data and information about profile compliance.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_profile** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**default_comply_profile** | [**ComplianceProfile**](ComplianceProfile.md) |  | [optional] 
**default_comply_locator** | [**List[ComplianceLocator]**](ComplianceLocator.md) | List of compliance locators.  Each locator specifies an association between the &lt;code&gt;applyProfile&lt;/code&gt; and the &lt;code&gt;defaultComplyProfile&lt;/code&gt;. The association identifies a component profile and the expression generated by the profile. vSphere clients can use this data to provide contextual information to the user.  ***Since:*** vSphere API 4.0  | [optional] 
**custom_comply_profile** | [**ComplianceProfile**](ComplianceProfile.md) |  | [optional] 
**disabled_expression_list** | **List[str]** | Disabled expressions in the default compliance profile (&lt;code&gt;DefaultComplyProfile&lt;/code&gt;).  Use this property to specify which expressions are disabled. All expressions are enabled by default.  ***Since:*** vSphere API 4.0  | [optional] 
**description** | [**ProfileDescription**](ProfileDescription.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_config_info import HostProfileConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileConfigInfo from a JSON string
host_profile_config_info_instance = HostProfileConfigInfo.from_json(json)
# print the JSON string representation of the object
print HostProfileConfigInfo.to_json()

# convert the object into a dict
host_profile_config_info_dict = host_profile_config_info_instance.to_dict()
# create an instance of HostProfileConfigInfo from a dict
host_profile_config_info_form_dict = host_profile_config_info.from_dict(host_profile_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


