# CpuIncompatible1ECX

Deprecated as of vSphere API 6.5 use *FeatureRequirementsNotMet*.  Convenience subclass for calling out some named features among the incompatibilities found in CPUID level 1 register ecx.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sse3** | **bool** | Flag to indicate bit 0 is incompatible.  ***Since:*** VI API 2.5  | 
**pclmulqdq** | **bool** | Flag to indicate bit 1 is incompatible.  ***Since:*** vSphere API 5.0  | 
**ssse3** | **bool** | Flag to indicate bit 9 is incompatible.  ***Since:*** VI API 2.5  | 
**sse41** | **bool** | Flag to indicate bit 19 is incompatible.  ***Since:*** VI API 2.5  | 
**sse42** | **bool** | Flag to indicate bit 20 is incompatible.  ***Since:*** VI API 2.5  | 
**aes** | **bool** | Flag to indicate bit 25 is incompatible.  ***Since:*** vSphere API 5.0  | 
**other** | **bool** | Flag to indicate that bits other than 0/1/9/19/20/25 are incompatible.  I.e. the detected incompatibilities cannot be completely described by the sse3, pclmulqdq, ssse3, sse41, sse42, and/or aes flags.  ***Since:*** VI API 2.5  | 
**other_only** | **bool** | Flag to indicate that the sse3, pclmulqdq, ssse3, sse41, sse42, and aes flags are all false, and the \&quot;other\&quot; flag is true.  Purely a convenience property for the client processing this fault.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.cpu_incompatible1_ecx import CpuIncompatible1ECX

# TODO update the JSON string below
json = "{}"
# create an instance of CpuIncompatible1ECX from a JSON string
cpu_incompatible1_ecx_instance = CpuIncompatible1ECX.from_json(json)
# print the JSON string representation of the object
print CpuIncompatible1ECX.to_json()

# convert the object into a dict
cpu_incompatible1_ecx_dict = cpu_incompatible1_ecx_instance.to_dict()
# create an instance of CpuIncompatible1ECX from a dict
cpu_incompatible1_ecx_form_dict = cpu_incompatible1_ecx.from_dict(cpu_incompatible1_ecx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


