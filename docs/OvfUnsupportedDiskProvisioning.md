# OvfUnsupportedDiskProvisioning

Disk provisioning not supported  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_provisioning** | **str** | The disk provisioning that was not supported.  ***Since:*** vSphere API 4.1  | 
**supported_disk_provisioning** | **str** | Disk modes supported by the host.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_disk_provisioning import OvfUnsupportedDiskProvisioning

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedDiskProvisioning from a JSON string
ovf_unsupported_disk_provisioning_instance = OvfUnsupportedDiskProvisioning.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedDiskProvisioning.to_json()

# convert the object into a dict
ovf_unsupported_disk_provisioning_dict = ovf_unsupported_disk_provisioning_instance.to_dict()
# create an instance of OvfUnsupportedDiskProvisioning from a dict
ovf_unsupported_disk_provisioning_form_dict = ovf_unsupported_disk_provisioning.from_dict(ovf_unsupported_disk_provisioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


