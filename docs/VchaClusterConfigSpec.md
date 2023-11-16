# VchaClusterConfigSpec

The VchaClusterConfigSpec class contains IP addresses of Passive and Witness nodes to configure and form the VCHA Cluster.  Passive and Witness nodes are assumed to be pre-configured to allow access to them over the specified IP addresses. Active Node IP address is not required as it is retrieved from the already configured interface on VCHA Cluster network.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passive_ip** | **str** | IP Address of Passive node in the VCHA Cluster network.  ***Since:*** vSphere API 6.5  | 
**witness_ip** | **str** | IP Address of Witness node in the VCHA Cluster network.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.vcha_cluster_config_spec import VchaClusterConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VchaClusterConfigSpec from a JSON string
vcha_cluster_config_spec_instance = VchaClusterConfigSpec.from_json(json)
# print the JSON string representation of the object
print VchaClusterConfigSpec.to_json()

# convert the object into a dict
vcha_cluster_config_spec_dict = vcha_cluster_config_spec_instance.to_dict()
# create an instance of VchaClusterConfigSpec from a dict
vcha_cluster_config_spec_form_dict = vcha_cluster_config_spec.from_dict(vcha_cluster_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


