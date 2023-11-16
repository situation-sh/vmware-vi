# ConfigurePowerPolicyRequestType

The parameters of *HostPowerSystem.ConfigurePowerPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A key from one of the policies in *PowerSystemCapability.availablePolicy*.  | 

## Example

```python
from vmware_vi.models.configure_power_policy_request_type import ConfigurePowerPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurePowerPolicyRequestType from a JSON string
configure_power_policy_request_type_instance = ConfigurePowerPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigurePowerPolicyRequestType.to_json()

# convert the object into a dict
configure_power_policy_request_type_dict = configure_power_policy_request_type_instance.to_dict()
# create an instance of ConfigurePowerPolicyRequestType from a dict
configure_power_policy_request_type_form_dict = configure_power_policy_request_type.from_dict(configure_power_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


