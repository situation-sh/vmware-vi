# IncompatibleHostForFtSecondary

The IncompatibleHostForFtSecondary fault is thrown when an invalid host has been specified when calling *VirtualMachine.CreateSecondaryVM_Task* or *VirtualMachine.EnableSecondaryVM_Task*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**error** | [**List[MethodFault]**](MethodFault.md) | Information on why the host that was specified could not be used for the FaultTolerance Secondary VirtualMachine.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.incompatible_host_for_ft_secondary import IncompatibleHostForFtSecondary

# TODO update the JSON string below
json = "{}"
# create an instance of IncompatibleHostForFtSecondary from a JSON string
incompatible_host_for_ft_secondary_instance = IncompatibleHostForFtSecondary.from_json(json)
# print the JSON string representation of the object
print IncompatibleHostForFtSecondary.to_json()

# convert the object into a dict
incompatible_host_for_ft_secondary_dict = incompatible_host_for_ft_secondary_instance.to_dict()
# create an instance of IncompatibleHostForFtSecondary from a dict
incompatible_host_for_ft_secondary_form_dict = incompatible_host_for_ft_secondary.from_dict(incompatible_host_for_ft_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


