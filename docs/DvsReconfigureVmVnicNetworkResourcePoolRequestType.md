# DvsReconfigureVmVnicNetworkResourcePoolRequestType

The parameters of *DistributedVirtualSwitch.DvsReconfigureVmVnicNetworkResourcePool_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**List[DvsVmVnicResourcePoolConfigSpec]**](DvsVmVnicResourcePoolConfigSpec.md) | The Virtual NIC network resource pool configuration specification and operation type.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.dvs_reconfigure_vm_vnic_network_resource_pool_request_type import DvsReconfigureVmVnicNetworkResourcePoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DvsReconfigureVmVnicNetworkResourcePoolRequestType from a JSON string
dvs_reconfigure_vm_vnic_network_resource_pool_request_type_instance = DvsReconfigureVmVnicNetworkResourcePoolRequestType.from_json(json)
# print the JSON string representation of the object
print DvsReconfigureVmVnicNetworkResourcePoolRequestType.to_json()

# convert the object into a dict
dvs_reconfigure_vm_vnic_network_resource_pool_request_type_dict = dvs_reconfigure_vm_vnic_network_resource_pool_request_type_instance.to_dict()
# create an instance of DvsReconfigureVmVnicNetworkResourcePoolRequestType from a dict
dvs_reconfigure_vm_vnic_network_resource_pool_request_type_form_dict = dvs_reconfigure_vm_vnic_network_resource_pool_request_type.from_dict(dvs_reconfigure_vm_vnic_network_resource_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


