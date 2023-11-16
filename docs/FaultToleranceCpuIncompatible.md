# FaultToleranceCpuIncompatible

Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 1 register ecx for FT vms.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **bool** | Flag to indicate CPU model is incompatible.  ***Since:*** vSphere API 4.0  | 
**family** | **bool** | Flag to indicate CPU family is incompatible.  ***Since:*** vSphere API 4.0  | 
**stepping** | **bool** | Flag to indicate CPU stepping is incompatible.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.fault_tolerance_cpu_incompatible import FaultToleranceCpuIncompatible

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceCpuIncompatible from a JSON string
fault_tolerance_cpu_incompatible_instance = FaultToleranceCpuIncompatible.from_json(json)
# print the JSON string representation of the object
print FaultToleranceCpuIncompatible.to_json()

# convert the object into a dict
fault_tolerance_cpu_incompatible_dict = fault_tolerance_cpu_incompatible_instance.to_dict()
# create an instance of FaultToleranceCpuIncompatible from a dict
fault_tolerance_cpu_incompatible_form_dict = fault_tolerance_cpu_incompatible.from_dict(fault_tolerance_cpu_incompatible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


