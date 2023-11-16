# VsanHostFaultDomainInfo

Host-local VSAN fault domain configuration.  This data object is used both for specifying and retrieving fault domain configuration for a host participating in the VSAN service.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The configured VSAN fault domain.  The length of fault domain name should not exceed 256. Empty string indicates that the default fault domain is used.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_host_fault_domain_info import VsanHostFaultDomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostFaultDomainInfo from a JSON string
vsan_host_fault_domain_info_instance = VsanHostFaultDomainInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostFaultDomainInfo.to_json()

# convert the object into a dict
vsan_host_fault_domain_info_dict = vsan_host_fault_domain_info_instance.to_dict()
# create an instance of VsanHostFaultDomainInfo from a dict
vsan_host_fault_domain_info_form_dict = vsan_host_fault_domain_info.from_dict(vsan_host_fault_domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


