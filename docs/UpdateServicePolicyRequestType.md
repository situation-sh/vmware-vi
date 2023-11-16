# UpdateServicePolicyRequestType

The parameters of *HostServiceSystem.UpdateServicePolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Service identifier (*HostServiceSystem.serviceInfo*.*HostServiceInfo.service*.*HostService.key*).  | 
**policy** | **str** | Specifies the condition for service activation. Use one of the *HostServicePolicy_enum* values.  | 

## Example

```python
from vmware_vi.models.update_service_policy_request_type import UpdateServicePolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServicePolicyRequestType from a JSON string
update_service_policy_request_type_instance = UpdateServicePolicyRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateServicePolicyRequestType.to_json()

# convert the object into a dict
update_service_policy_request_type_dict = update_service_policy_request_type_instance.to_dict()
# create an instance of UpdateServicePolicyRequestType from a dict
update_service_policy_request_type_form_dict = update_service_policy_request_type.from_dict(update_service_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


