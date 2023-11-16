# ArrayOfVmPowerOnDisabled

A boxed array of *VmPowerOnDisabled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmPowerOnDisabled]**](VmPowerOnDisabled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_power_on_disabled import ArrayOfVmPowerOnDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmPowerOnDisabled from a JSON string
array_of_vm_power_on_disabled_instance = ArrayOfVmPowerOnDisabled.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmPowerOnDisabled.to_json()

# convert the object into a dict
array_of_vm_power_on_disabled_dict = array_of_vm_power_on_disabled_instance.to_dict()
# create an instance of ArrayOfVmPowerOnDisabled from a dict
array_of_vm_power_on_disabled_form_dict = array_of_vm_power_on_disabled.from_dict(array_of_vm_power_on_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


