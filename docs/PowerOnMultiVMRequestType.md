# PowerOnMultiVMRequestType

The parameters of *Datacenter.PowerOnMultiVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The virtual machines to power on.  ***Required privileges:*** VirtualMachine.Interact.PowerOn  Refers instances of *VirtualMachine*.  | 
**option** | [**List[OptionValue]**](OptionValue.md) | An array of *OptionValue* options for this power-on session. The names and values of the options are defined in *ClusterPowerOnVmOption_enum*.  | [optional] 

## Example

```python
from vmware_vi.models.power_on_multi_vm_request_type import PowerOnMultiVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PowerOnMultiVMRequestType from a JSON string
power_on_multi_vm_request_type_instance = PowerOnMultiVMRequestType.from_json(json)
# print the JSON string representation of the object
print PowerOnMultiVMRequestType.to_json()

# convert the object into a dict
power_on_multi_vm_request_type_dict = power_on_multi_vm_request_type_instance.to_dict()
# create an instance of PowerOnMultiVMRequestType from a dict
power_on_multi_vm_request_type_form_dict = power_on_multi_vm_request_type.from_dict(power_on_multi_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


