# HostAssignableHardwareConfig

The AssignableHardwareConfig data object describes properties of all assignable devices on the host.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_override** | [**List[HostAssignableHardwareConfigAttributeOverride]**](HostAssignableHardwareConfigAttributeOverride.md) | List of attribute overrides.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_assignable_hardware_config import HostAssignableHardwareConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostAssignableHardwareConfig from a JSON string
host_assignable_hardware_config_instance = HostAssignableHardwareConfig.from_json(json)
# print the JSON string representation of the object
print HostAssignableHardwareConfig.to_json()

# convert the object into a dict
host_assignable_hardware_config_dict = host_assignable_hardware_config_instance.to_dict()
# create an instance of HostAssignableHardwareConfig from a dict
host_assignable_hardware_config_form_dict = host_assignable_hardware_config.from_dict(host_assignable_hardware_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


