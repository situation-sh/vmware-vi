# CannotDisconnectHostWithFaultToleranceVm

This fault is thrown when an attempt is made to disconnect a host, which has one or more fault tolerance vms and is not in maintenance mode.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host to be disconnected  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.cannot_disconnect_host_with_fault_tolerance_vm import CannotDisconnectHostWithFaultToleranceVm

# TODO update the JSON string below
json = "{}"
# create an instance of CannotDisconnectHostWithFaultToleranceVm from a JSON string
cannot_disconnect_host_with_fault_tolerance_vm_instance = CannotDisconnectHostWithFaultToleranceVm.from_json(json)
# print the JSON string representation of the object
print CannotDisconnectHostWithFaultToleranceVm.to_json()

# convert the object into a dict
cannot_disconnect_host_with_fault_tolerance_vm_dict = cannot_disconnect_host_with_fault_tolerance_vm_instance.to_dict()
# create an instance of CannotDisconnectHostWithFaultToleranceVm from a dict
cannot_disconnect_host_with_fault_tolerance_vm_form_dict = cannot_disconnect_host_with_fault_tolerance_vm.from_dict(cannot_disconnect_host_with_fault_tolerance_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


