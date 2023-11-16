# ComputeResourceHostSPBMLicenseInfo

The *ComputeResourceHostSPBMLicenseInfo* data object encapsulates the SPBM(Storage Policy Based Management) license information for a host.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**license_state** | [**ComputeResourceHostSPBMLicenseInfoHostSPBMLicenseStateEnum**](ComputeResourceHostSPBMLicenseInfoHostSPBMLicenseStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.compute_resource_host_spbm_license_info import ComputeResourceHostSPBMLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceHostSPBMLicenseInfo from a JSON string
compute_resource_host_spbm_license_info_instance = ComputeResourceHostSPBMLicenseInfo.from_json(json)
# print the JSON string representation of the object
print ComputeResourceHostSPBMLicenseInfo.to_json()

# convert the object into a dict
compute_resource_host_spbm_license_info_dict = compute_resource_host_spbm_license_info_instance.to_dict()
# create an instance of ComputeResourceHostSPBMLicenseInfo from a dict
compute_resource_host_spbm_license_info_form_dict = compute_resource_host_spbm_license_info.from_dict(compute_resource_host_spbm_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


