# ApplyHostProfileConfigurationResult

The *ApplyHostProfileConfigurationResult* data object contains the remediation results for a host: the time that the remediation happens, the status, the errors, and optinal compliance result after reboot.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | Time that the host config apply starts.  ***Since:*** vSphere API 6.5  | 
**complete_time** | **datetime** | Time that the host config apply completes.  ***Since:*** vSphere API 6.5  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**status** | **str** | Status of the remediation.  See *ApplyHostProfileConfigurationResultStatus_enum* for valid values.  ***Since:*** vSphere API 6.5  | 
**errors** | [**List[MethodFault]**](MethodFault.md) | If &lt;code&gt;status&lt;/code&gt; is &lt;code&gt;fail&lt;/code&gt;, this property contains a list of status error message objects.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.apply_host_profile_configuration_result import ApplyHostProfileConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyHostProfileConfigurationResult from a JSON string
apply_host_profile_configuration_result_instance = ApplyHostProfileConfigurationResult.from_json(json)
# print the JSON string representation of the object
print ApplyHostProfileConfigurationResult.to_json()

# convert the object into a dict
apply_host_profile_configuration_result_dict = apply_host_profile_configuration_result_instance.to_dict()
# create an instance of ApplyHostProfileConfigurationResult from a dict
apply_host_profile_configuration_result_form_dict = apply_host_profile_configuration_result.from_dict(apply_host_profile_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


