# ClusterComputeResourceHCIConfigSpec

Specification to configure the cluster.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_prof** | [**List[ClusterComputeResourceDvsProfile]**](ClusterComputeResourceDvsProfile.md) | Information related to network configuration.  For each DvsProfile object, specify either *ClusterComputeResourceDvsProfile.dvsName* or *ClusterComputeResourceDvsProfile.dvSwitch*. Across all DvsProfile objects, specify exactly one *ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping.dvPortgroup* or *ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping.dvPortgroupSpec* per *ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping.service*.  ***Since:*** vSphere API 6.7.1  | [optional] 
**host_config_profile** | [**ClusterComputeResourceHostConfigurationProfile**](ClusterComputeResourceHostConfigurationProfile.md) |  | [optional] 
**v_san_config_spec** | [**SDDCBase**](SDDCBase.md) |  | [optional] 
**vc_prof** | [**ClusterComputeResourceVCProfile**](ClusterComputeResourceVCProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_hci_config_spec import ClusterComputeResourceHCIConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceHCIConfigSpec from a JSON string
cluster_compute_resource_hci_config_spec_instance = ClusterComputeResourceHCIConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceHCIConfigSpec.to_json()

# convert the object into a dict
cluster_compute_resource_hci_config_spec_dict = cluster_compute_resource_hci_config_spec_instance.to_dict()
# create an instance of ClusterComputeResourceHCIConfigSpec from a dict
cluster_compute_resource_hci_config_spec_form_dict = cluster_compute_resource_hci_config_spec.from_dict(cluster_compute_resource_hci_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


