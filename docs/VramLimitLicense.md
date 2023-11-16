# VramLimitLicense

A VramLimitLicense fault is thrown if executing an operation would result in exceeding maximum allowed vRAM amount.  For example, this could happen when powering on a VM, hot-plugging memory into a running VMm, etc.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum allowed vRAM amount.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vram_limit_license import VramLimitLicense

# TODO update the JSON string below
json = "{}"
# create an instance of VramLimitLicense from a JSON string
vram_limit_license_instance = VramLimitLicense.from_json(json)
# print the JSON string representation of the object
print VramLimitLicense.to_json()

# convert the object into a dict
vram_limit_license_dict = vram_limit_license_instance.to_dict()
# create an instance of VramLimitLicense from a dict
vram_limit_license_form_dict = vram_limit_license.from_dict(vram_limit_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


