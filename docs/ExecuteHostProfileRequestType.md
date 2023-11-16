# ExecuteHostProfileRequestType

The parameters of *HostProfile.ExecuteHostProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**deferred_param** | [**List[ProfileDeferredPolicyOptionParameter]**](ProfileDeferredPolicyOptionParameter.md) | Additional configuration data to be applied to the host. This should contain all of the host-specific data, including data from from previous calls to the method.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.execute_host_profile_request_type import ExecuteHostProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteHostProfileRequestType from a JSON string
execute_host_profile_request_type_instance = ExecuteHostProfileRequestType.from_json(json)
# print the JSON string representation of the object
print ExecuteHostProfileRequestType.to_json()

# convert the object into a dict
execute_host_profile_request_type_dict = execute_host_profile_request_type_instance.to_dict()
# create an instance of ExecuteHostProfileRequestType from a dict
execute_host_profile_request_type_form_dict = execute_host_profile_request_type.from_dict(execute_host_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


