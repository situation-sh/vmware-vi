# ExtendHCIRequestType

The parameters of *ClusterComputeResource.ExtendHCI_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_inputs** | [**List[ClusterComputeResourceHostConfigurationInput]**](ClusterComputeResourceHostConfigurationInput.md) | Inputs to configure specified set of hosts in the cluster. See *ClusterComputeResourceHostConfigurationInput* for details. Hosts in this list should be part of the cluster and should be in maintenance mode for them to be configured per specification. Hosts which were not configured due to not being in maintenance mode will be returned in *ClusterComputeResourceClusterConfigResult.failedHosts*. Specify *ClusterComputeResourceHostConfigurationInput.hostVmkNics* only if *dvsSetting* is set.  ***Since:*** vSphere API 6.7.1  | [optional] 
**v_san_config_spec** | [**SDDCBase**](SDDCBase.md) |  | [optional] 

## Example

```python
from vmware_vi.models.extend_hci_request_type import ExtendHCIRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendHCIRequestType from a JSON string
extend_hci_request_type_instance = ExtendHCIRequestType.from_json(json)
# print the JSON string representation of the object
print ExtendHCIRequestType.to_json()

# convert the object into a dict
extend_hci_request_type_dict = extend_hci_request_type_instance.to_dict()
# create an instance of ExtendHCIRequestType from a dict
extend_hci_request_type_form_dict = extend_hci_request_type.from_dict(extend_hci_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


