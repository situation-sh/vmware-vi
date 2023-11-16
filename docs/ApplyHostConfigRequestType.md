# ApplyHostConfigRequestType

The parameters of *HostProfileManager.ApplyHostConfig_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**config_spec** | [**HostConfigSpec**](HostConfigSpec.md) |  | 
**user_input** | [**List[ProfileDeferredPolicyOptionParameter]**](ProfileDeferredPolicyOptionParameter.md) | Additional host-specific data to be applied to the host. This data is the complete list of deferred parameters verified by the *HostProfile*.*HostProfile.ExecuteHostProfile* method, contained in the *ProfileExecuteResult* object returned by the method.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.apply_host_config_request_type import ApplyHostConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyHostConfigRequestType from a JSON string
apply_host_config_request_type_instance = ApplyHostConfigRequestType.from_json(json)
# print the JSON string representation of the object
print ApplyHostConfigRequestType.to_json()

# convert the object into a dict
apply_host_config_request_type_dict = apply_host_config_request_type_instance.to_dict()
# create an instance of ApplyHostConfigRequestType from a dict
apply_host_config_request_type_form_dict = apply_host_config_request_type.from_dict(apply_host_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


