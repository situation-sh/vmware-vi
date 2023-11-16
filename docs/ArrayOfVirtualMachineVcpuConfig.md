# ArrayOfVirtualMachineVcpuConfig

A boxed array of *VirtualMachineVcpuConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVcpuConfig]**](VirtualMachineVcpuConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vcpu_config import ArrayOfVirtualMachineVcpuConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVcpuConfig from a JSON string
array_of_virtual_machine_vcpu_config_instance = ArrayOfVirtualMachineVcpuConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVcpuConfig.to_json()

# convert the object into a dict
array_of_virtual_machine_vcpu_config_dict = array_of_virtual_machine_vcpu_config_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVcpuConfig from a dict
array_of_virtual_machine_vcpu_config_form_dict = array_of_virtual_machine_vcpu_config.from_dict(array_of_virtual_machine_vcpu_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


