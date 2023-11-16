# HostAssignableHardwareConfigAttributeOverride

An AttributeOverride provides a name-value pair that overrides for a particular instance node a configurable Attribute defined by that device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Instance ID of the Assignable Hardware instance node where the attribute specified by name is overridden.  ***Since:*** vSphere API 7.0  | 
**name** | **str** | Name of attribute to override.  ***Since:*** vSphere API 7.0  | 
**value** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_assignable_hardware_config_attribute_override import HostAssignableHardwareConfigAttributeOverride

# TODO update the JSON string below
json = "{}"
# create an instance of HostAssignableHardwareConfigAttributeOverride from a JSON string
host_assignable_hardware_config_attribute_override_instance = HostAssignableHardwareConfigAttributeOverride.from_json(json)
# print the JSON string representation of the object
print HostAssignableHardwareConfigAttributeOverride.to_json()

# convert the object into a dict
host_assignable_hardware_config_attribute_override_dict = host_assignable_hardware_config_attribute_override_instance.to_dict()
# create an instance of HostAssignableHardwareConfigAttributeOverride from a dict
host_assignable_hardware_config_attribute_override_form_dict = host_assignable_hardware_config_attribute_override.from_dict(host_assignable_hardware_config_attribute_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


