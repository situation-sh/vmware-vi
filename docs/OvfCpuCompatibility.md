# OvfCpuCompatibility


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_name** | **str** | Possible register names are eax, ebx, ecx, or edx.  ***Since:*** vSphere API 5.0  | 
**level** | **int** | The CpuId level where a problem was detected.  Other levels may also have problems  ***Since:*** vSphere API 5.0  | 
**register_value** | **str** | The register value where the problem was detected  ***Since:*** vSphere API 5.0  | 
**desired_register_value** | **str** | The desired register value return from the host  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_cpu_compatibility import OvfCpuCompatibility

# TODO update the JSON string below
json = "{}"
# create an instance of OvfCpuCompatibility from a JSON string
ovf_cpu_compatibility_instance = OvfCpuCompatibility.from_json(json)
# print the JSON string representation of the object
print OvfCpuCompatibility.to_json()

# convert the object into a dict
ovf_cpu_compatibility_dict = ovf_cpu_compatibility_instance.to_dict()
# create an instance of OvfCpuCompatibility from a dict
ovf_cpu_compatibility_form_dict = ovf_cpu_compatibility.from_dict(ovf_cpu_compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


