# ProfileDeferredPolicyOptionParameter

The *ProfileDeferredPolicyOptionParameter* data object contains information about a single deferred parameter for host configuration. - The Server verifies deferred parameter data when it calls the   *HostProfile*.*HostProfile.ExecuteHostProfile*   method. - The client supplies deferred parameter data for host configuration when it calls the   *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task*   method. - The vCenter Server stores deferred parameter data in answer files   (*AnswerFile*.*AnswerFile.userInput*).       ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | 
**parameter** | [**List[KeyAnyValue]**](KeyAnyValue.md) | List that contains values for the policy parameters.  During parameter verification, this property is unspecified if the client has not provided the values for this parameter. See *ProfileExecuteResult*.*ProfileExecuteResult.requireInput*.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_deferred_policy_option_parameter import ProfileDeferredPolicyOptionParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileDeferredPolicyOptionParameter from a JSON string
profile_deferred_policy_option_parameter_instance = ProfileDeferredPolicyOptionParameter.from_json(json)
# print the JSON string representation of the object
print ProfileDeferredPolicyOptionParameter.to_json()

# convert the object into a dict
profile_deferred_policy_option_parameter_dict = profile_deferred_policy_option_parameter_instance.to_dict()
# create an instance of ProfileDeferredPolicyOptionParameter from a dict
profile_deferred_policy_option_parameter_form_dict = profile_deferred_policy_option_parameter.from_dict(profile_deferred_policy_option_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


