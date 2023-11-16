# ClusterDpmHostConfigSpec

The *ClusterDpmHostConfigSpec* data object provides information that the Server uses to update the DPM configuration for a single host (identified by the *ClusterDpmHostConfigInfo.key* property).  The host DPM configuration overrides the cluster default DPM setting (*ClusterConfigSpecEx*.*ClusterConfigSpecEx.dpmConfig*).  The vSphere API defines three update operations (*ArrayUpdateSpec*.*ArrayUpdateSpec.operation*). - add: Define DPM behavior for a host. If the cluster   configuration already includes a DPM behavior override   for the specified host, this operation   removes the existing override and adds the new one.   The new DPM override will use the cluster default value   if you do not specify the behavior property   (*ClusterDpmConfigInfo.defaultDpmBehavior*). - edit: Perform an incremental update to an existing   DPM configuration entry for a host.   The reconfigure method changes only the properties   that you set in the data object. The entry must exist   in the   *ClusterConfigSpecEx*.*ClusterConfigSpecEx.dpmHostConfigSpec* array. - remove: Remove the DPM override for the specified   host. To identify the host to delete, use the   *ArrayUpdateSpec.removeKey* property   to specify the *ClusterDpmHostConfigInfo.key*   in the host override.    Use the *ComputeResource.ReconfigureComputeResource_Task* method to update the DPM configuration. If you set the modify parameter to true, you can use any of the three operations (add, edit, or remove). If you set the modify parameter to false, you can use only the add operation.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterDpmHostConfigInfo**](ClusterDpmHostConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_dpm_host_config_spec import ClusterDpmHostConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDpmHostConfigSpec from a JSON string
cluster_dpm_host_config_spec_instance = ClusterDpmHostConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterDpmHostConfigSpec.to_json()

# convert the object into a dict
cluster_dpm_host_config_spec_dict = cluster_dpm_host_config_spec_instance.to_dict()
# create an instance of ClusterDpmHostConfigSpec from a dict
cluster_dpm_host_config_spec_form_dict = cluster_dpm_host_config_spec.from_dict(cluster_dpm_host_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


