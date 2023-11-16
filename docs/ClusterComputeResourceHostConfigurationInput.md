# ClusterComputeResourceHostConfigurationInput

Host configuration input to configure hosts in a cluster.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host_vmk_nics** | [**List[ClusterComputeResourceHostVmkNicInfo]**](ClusterComputeResourceHostVmkNicInfo.md) |  | [optional] 
**allowed_in_non_maintenance_mode** | **bool** | To apply configuration on the host, the host is expected to be in maintenance mode.  This constraint can be relaxed by setting this flag to true.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_host_configuration_input import ClusterComputeResourceHostConfigurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceHostConfigurationInput from a JSON string
cluster_compute_resource_host_configuration_input_instance = ClusterComputeResourceHostConfigurationInput.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceHostConfigurationInput.to_json()

# convert the object into a dict
cluster_compute_resource_host_configuration_input_dict = cluster_compute_resource_host_configuration_input_instance.to_dict()
# create an instance of ClusterComputeResourceHostConfigurationInput from a dict
cluster_compute_resource_host_configuration_input_form_dict = cluster_compute_resource_host_configuration_input.from_dict(cluster_compute_resource_host_configuration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


