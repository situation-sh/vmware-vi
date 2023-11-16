# VsanHostConfigInfo

The *VsanHostConfigInfo* data object contains host-specific settings for the VSAN service.  This data object is used both for specifying settings for updating the VSAN service, and as an output datatype when retrieving current VSAN service settings.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the VSAN service is currently enabled on this host.  ***Since:*** vSphere API 5.5  | [optional] 
**host_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**cluster_info** | [**VsanHostConfigInfoClusterInfo**](VsanHostConfigInfoClusterInfo.md) |  | [optional] 
**storage_info** | [**VsanHostConfigInfoStorageInfo**](VsanHostConfigInfoStorageInfo.md) |  | [optional] 
**network_info** | [**VsanHostConfigInfoNetworkInfo**](VsanHostConfigInfoNetworkInfo.md) |  | [optional] 
**fault_domain_info** | [**VsanHostFaultDomainInfo**](VsanHostFaultDomainInfo.md) |  | [optional] 
**vsan_esa_enabled** | **bool** | Whether the vSAN ESA is enabled on this host.  This can only be enabled when vSAN is enabled on this host.  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_config_info import VsanHostConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostConfigInfo from a JSON string
vsan_host_config_info_instance = VsanHostConfigInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostConfigInfo.to_json()

# convert the object into a dict
vsan_host_config_info_dict = vsan_host_config_info_instance.to_dict()
# create an instance of VsanHostConfigInfo from a dict
vsan_host_config_info_form_dict = vsan_host_config_info.from_dict(vsan_host_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


