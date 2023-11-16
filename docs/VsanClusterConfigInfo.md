# VsanClusterConfigInfo

The *VsanClusterConfigInfo* data object contains configuration data for the VSAN service in a cluster.  This data object is used both for specifying cluster-wide settings when updating the VSAN service, and as an output datatype when retrieving current cluster-wide VSAN service settings.  See also *ComputeResource.ReconfigureComputeResource_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the VSAN service is enabled for the cluster.  ***Since:*** vSphere API 5.5  | [optional] 
**default_config** | [**VsanClusterConfigInfoHostDefaultInfo**](VsanClusterConfigInfoHostDefaultInfo.md) |  | [optional] 
**vsan_esa_enabled** | **bool** | Whether the vSAN ESA is enabled for vSAN cluster.  This can only be enabled when vSAN is enabled on the cluster.  | [optional] 

## Example

```python
from vmware_vi.models.vsan_cluster_config_info import VsanClusterConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanClusterConfigInfo from a JSON string
vsan_cluster_config_info_instance = VsanClusterConfigInfo.from_json(json)
# print the JSON string representation of the object
print VsanClusterConfigInfo.to_json()

# convert the object into a dict
vsan_cluster_config_info_dict = vsan_cluster_config_info_instance.to_dict()
# create an instance of VsanClusterConfigInfo from a dict
vsan_cluster_config_info_form_dict = vsan_cluster_config_info.from_dict(vsan_cluster_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


