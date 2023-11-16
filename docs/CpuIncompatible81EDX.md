# CpuIncompatible81EDX

Deprecated as of vSphere API 6.5 use *FeatureRequirementsNotMet*.  Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 0x80000001 register edx.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nx** | **bool** | Flag to indicate bit 20 is incompatible.  ***Since:*** VI API 2.5  | 
**ffxsr** | **bool** | Flag to indicate bit 25 is incompatible.  ***Since:*** VI API 2.5  | 
**rdtscp** | **bool** | Flag to indicate bit 27 is incompatible.  ***Since:*** VI API 2.5  | 
**lm** | **bool** | Flag to indicate bit 29 is incompatible.  ***Since:*** VI API 2.5  | 
**other** | **bool** | Flag to indicate that bits other than 20/25/27/29 are incompatible.  I.e. the detected incompatibilities cannot be completely described by the nx, ffxsr, rdtscp, and/or lm flags.  ***Since:*** VI API 2.5  | 
**other_only** | **bool** | Flag to indicate that the nx, ffxsr, rdtscp, and lm flags are all false, and the \&quot;other\&quot; flag is true.  Purely a convenience property for the client processing this fault.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.cpu_incompatible81_edx import CpuIncompatible81EDX

# TODO update the JSON string below
json = "{}"
# create an instance of CpuIncompatible81EDX from a JSON string
cpu_incompatible81_edx_instance = CpuIncompatible81EDX.from_json(json)
# print the JSON string representation of the object
print CpuIncompatible81EDX.to_json()

# convert the object into a dict
cpu_incompatible81_edx_dict = cpu_incompatible81_edx_instance.to_dict()
# create an instance of CpuIncompatible81EDX from a dict
cpu_incompatible81_edx_form_dict = cpu_incompatible81_edx.from_dict(cpu_incompatible81_edx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


