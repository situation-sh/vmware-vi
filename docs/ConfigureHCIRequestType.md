# ConfigureHCIRequestType

The parameters of *ClusterComputeResource.ConfigureHCI_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_spec** | [**ClusterComputeResourceHCIConfigSpec**](ClusterComputeResourceHCIConfigSpec.md) |  | 
**host_inputs** | [**List[ClusterComputeResourceHostConfigurationInput]**](ClusterComputeResourceHostConfigurationInput.md) | Inputs to configure each host in the cluster, see *ClusterComputeResourceHostConfigurationInput* for details. Hosts in this list should be part of the cluster and should be in maintenance mode for them to be configured per specification. If this parameter is not specified, the API operates on all the hosts in the cluster. Hosts which were not configured due to not being in maintenance mode will be returned in *ClusterComputeResourceClusterConfigResult.failedHosts*.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.configure_hci_request_type import ConfigureHCIRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureHCIRequestType from a JSON string
configure_hci_request_type_instance = ConfigureHCIRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureHCIRequestType.to_json()

# convert the object into a dict
configure_hci_request_type_dict = configure_hci_request_type_instance.to_dict()
# create an instance of ConfigureHCIRequestType from a dict
configure_hci_request_type_form_dict = configure_hci_request_type.from_dict(configure_hci_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


