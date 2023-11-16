# HostProfileValidationFailureInfo

This defines the validation result for the host profile.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of host profile to be validated.  ***Since:*** vSphere API 6.7  | 
**annotation** | **str** | Host profile annotation at update.  ***Since:*** vSphere API 6.7  | 
**update_type** | **str** | Host profile update type.  See the enumerate class &lt;code&gt;UpdateType&lt;/code&gt; above for the valid values.  ***Since:*** vSphere API 6.7  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**apply_profile** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**failures** | [**List[ProfileUpdateFailedUpdateFailure]**](ProfileUpdateFailedUpdateFailure.md) | List of failures in the host profile configuration.  ***Since:*** vSphere API 6.7  | [optional] 
**faults** | [**List[MethodFault]**](MethodFault.md) | The &lt;code&gt;MethodFault&lt;/code&gt;s happened at validation.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_validation_failure_info import HostProfileValidationFailureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileValidationFailureInfo from a JSON string
host_profile_validation_failure_info_instance = HostProfileValidationFailureInfo.from_json(json)
# print the JSON string representation of the object
print HostProfileValidationFailureInfo.to_json()

# convert the object into a dict
host_profile_validation_failure_info_dict = host_profile_validation_failure_info_instance.to_dict()
# create an instance of HostProfileValidationFailureInfo from a dict
host_profile_validation_failure_info_form_dict = host_profile_validation_failure_info.from_dict(host_profile_validation_failure_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


