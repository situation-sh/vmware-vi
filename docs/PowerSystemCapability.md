# PowerSystemCapability

Power System Capability data object.  Exposes policies available in power management system.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_policy** | [**List[HostPowerPolicy]**](HostPowerPolicy.md) | List of available host power policies.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.power_system_capability import PowerSystemCapability

# TODO update the JSON string below
json = "{}"
# create an instance of PowerSystemCapability from a JSON string
power_system_capability_instance = PowerSystemCapability.from_json(json)
# print the JSON string representation of the object
print PowerSystemCapability.to_json()

# convert the object into a dict
power_system_capability_dict = power_system_capability_instance.to_dict()
# create an instance of PowerSystemCapability from a dict
power_system_capability_form_dict = power_system_capability.from_dict(power_system_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


