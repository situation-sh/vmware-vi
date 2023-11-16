# VmPowerOnDisabled

This exception is thrown if the power-on of a virtual machine is attempted when the operation is disabled on the host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_power_on_disabled import VmPowerOnDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of VmPowerOnDisabled from a JSON string
vm_power_on_disabled_instance = VmPowerOnDisabled.from_json(json)
# print the JSON string representation of the object
print VmPowerOnDisabled.to_json()

# convert the object into a dict
vm_power_on_disabled_dict = vm_power_on_disabled_instance.to_dict()
# create an instance of VmPowerOnDisabled from a dict
vm_power_on_disabled_form_dict = vm_power_on_disabled.from_dict(vm_power_on_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


