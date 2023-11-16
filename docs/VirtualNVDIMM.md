# VirtualNVDIMM

The Virtual NVDIMM device.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_mb** | **int** | NVDIMM backing size in MiB.  If backing is inaccessible, then capacity is reported as 0.  ***Since:*** vSphere API 6.7  | 
**configured_capacity_in_mb** | **int** | NVDIMM device&#39;s configured size in MiB.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_nvdimm import VirtualNVDIMM

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNVDIMM from a JSON string
virtual_nvdimm_instance = VirtualNVDIMM.from_json(json)
# print the JSON string representation of the object
print VirtualNVDIMM.to_json()

# convert the object into a dict
virtual_nvdimm_dict = virtual_nvdimm_instance.to_dict()
# create an instance of VirtualNVDIMM from a dict
virtual_nvdimm_form_dict = virtual_nvdimm.from_dict(virtual_nvdimm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


