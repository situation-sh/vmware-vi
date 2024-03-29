# VsanHostConfigInfoClusterInfo

Host-local VSAN cluster configuration.  This data object is used both for specifying and retrieving cluster configuration for a host participating in the VSAN service.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | VSAN service cluster UUID, in the string form \&quot;nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn\&quot;, where n are hexadecimal digits.  If provided while enabling the VSAN service, this value will be used for the service cluster UUID. If omitted when enabling the VSAN service, a suitable UUID will be generated by the platform. This is a read-only value while the VSAN service is enabled.  ***Since:*** vSphere API 5.5  | [optional] 
**node_uuid** | **str** | VSAN node UUID for this host.  This is a read-only value which is populated upon enabling of the VSAN service.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_config_info_cluster_info import VsanHostConfigInfoClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostConfigInfoClusterInfo from a JSON string
vsan_host_config_info_cluster_info_instance = VsanHostConfigInfoClusterInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostConfigInfoClusterInfo.to_json()

# convert the object into a dict
vsan_host_config_info_cluster_info_dict = vsan_host_config_info_cluster_info_instance.to_dict()
# create an instance of VsanHostConfigInfoClusterInfo from a dict
vsan_host_config_info_cluster_info_form_dict = vsan_host_config_info_cluster_info.from_dict(vsan_host_config_info_cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


