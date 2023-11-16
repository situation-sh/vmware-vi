# CpuIncompatible

Deprecated as of vSphere API 6.5 use *FeatureRequirementsNotMet*.  The host is not compatible with the CPU feature requirements of the virtual machine, for a particular CPUID register.  A subclass of this fault may be used to express the incompatibilities in a more easily understandable format. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | The CpuIdInfo level where a problem was detected.  Other levels may also have problems.  | 
**register_name** | **str** | The CpuIdInfo register where a problem was detected.  Other registers may also have problems. Possible register names are eax, ebx, ecx, or edx.  | 
**register_bits** | **str** | The contents of the register on the target host, in CpuIdInfo register format.  The &#39;-&#39; character indicates an unknown value.  ***Since:*** VI API 2.5  | [optional] 
**desired_bits** | **str** | The desired values for the register&#39;s bits.  The &#39;x&#39; character indicates don&#39;t-care.  ***Since:*** VI API 2.5  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cpu_incompatible import CpuIncompatible

# TODO update the JSON string below
json = "{}"
# create an instance of CpuIncompatible from a JSON string
cpu_incompatible_instance = CpuIncompatible.from_json(json)
# print the JSON string representation of the object
print CpuIncompatible.to_json()

# convert the object into a dict
cpu_incompatible_dict = cpu_incompatible_instance.to_dict()
# create an instance of CpuIncompatible from a dict
cpu_incompatible_form_dict = cpu_incompatible.from_dict(cpu_incompatible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


