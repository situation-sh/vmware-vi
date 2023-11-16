# FaultTolerancePrimaryPowerOnNotAttempted

This fault is used to report that VirtualCenter did not attempt to power on a Fault Tolerance secondary virtual machine because it was unable to power on the corresponding Fault Tolerance primary virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secondary_vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**primary_vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.fault_tolerance_primary_power_on_not_attempted import FaultTolerancePrimaryPowerOnNotAttempted

# TODO update the JSON string below
json = "{}"
# create an instance of FaultTolerancePrimaryPowerOnNotAttempted from a JSON string
fault_tolerance_primary_power_on_not_attempted_instance = FaultTolerancePrimaryPowerOnNotAttempted.from_json(json)
# print the JSON string representation of the object
print FaultTolerancePrimaryPowerOnNotAttempted.to_json()

# convert the object into a dict
fault_tolerance_primary_power_on_not_attempted_dict = fault_tolerance_primary_power_on_not_attempted_instance.to_dict()
# create an instance of FaultTolerancePrimaryPowerOnNotAttempted from a dict
fault_tolerance_primary_power_on_not_attempted_form_dict = fault_tolerance_primary_power_on_not_attempted.from_dict(fault_tolerance_primary_power_on_not_attempted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


