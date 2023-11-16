# UpdateDefaultPolicyRequestType

The parameters of *HostFirewallSystem.UpdateDefaultPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_policy** | [**HostFirewallDefaultPolicy**](HostFirewallDefaultPolicy.md) |  | 

## Example

```python
from vmware_vi.models.update_default_policy_request_type import UpdateDefaultPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDefaultPolicyRequestType from a JSON string
update_default_policy_request_type_instance = UpdateDefaultPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDefaultPolicyRequestType.to_json()

# convert the object into a dict
update_default_policy_request_type_dict = update_default_policy_request_type_instance.to_dict()
# create an instance of UpdateDefaultPolicyRequestType from a dict
update_default_policy_request_type_form_dict = update_default_policy_request_type.from_dict(update_default_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


