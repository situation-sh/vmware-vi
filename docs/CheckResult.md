# CheckResult

The result of a call to any of the methods in either *VirtualMachineCompatibilityChecker* or *VirtualMachineProvisioningChecker*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**warning** | [**List[MethodFault]**](MethodFault.md) | A list of faults representing problems which may require attention, but which are not fatal.  ***Since:*** vSphere API 4.0  | [optional] 
**error** | [**List[MethodFault]**](MethodFault.md) | A list of faults representing problems which are fatal to the operation.  For *VirtualMachineProvisioningChecker* an error means that the given provisioning operation would fail. For *VirtualMachineCompatibilityChecker* an error means that either a power-on of this virtual machine would fail, or that the virtual machine would not run correctly once powered-on.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.check_result import CheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResult from a JSON string
check_result_instance = CheckResult.from_json(json)
# print the JSON string representation of the object
print CheckResult.to_json()

# convert the object into a dict
check_result_dict = check_result_instance.to_dict()
# create an instance of CheckResult from a dict
check_result_form_dict = check_result.from_dict(check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


