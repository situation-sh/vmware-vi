# HostConfigSummary

An overview of the key configuration parameters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the host.  | 
**port** | **int** | The port number.  | 
**ssl_thumbprint** | **str** | The SSL thumbprint of the host, if known.  ***Since:*** vSphere API 4.0  | [optional] 
**product** | [**AboutInfo**](AboutInfo.md) |  | [optional] 
**vmotion_enabled** | **bool** | The flag to indicate whether or not VMotion is enabled on this host.  | 
**fault_tolerance_enabled** | **bool** | The flag to indicate whether or not Fault Tolerance logging is enabled on this host.  ***Since:*** vSphere API 4.0  | 
**feature_version** | [**List[HostFeatureVersionInfo]**](HostFeatureVersionInfo.md) | List of feature-specific version information.  Each element refers to the version information for a specific feature.  ***Since:*** vSphere API 4.1  | [optional] 
**agent_vm_datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**agent_vm_network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_config_summary import HostConfigSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigSummary from a JSON string
host_config_summary_instance = HostConfigSummary.from_json(json)
# print the JSON string representation of the object
print HostConfigSummary.to_json()

# convert the object into a dict
host_config_summary_dict = host_config_summary_instance.to_dict()
# create an instance of HostConfigSummary from a dict
host_config_summary_form_dict = host_config_summary.from_dict(host_config_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


