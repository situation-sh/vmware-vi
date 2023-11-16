# DvsVmVnicResourcePoolConfigSpec

The configuration specification data object to update the resource configuration for a virtual NIC network resource pool.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation on the virtual NIC network resource pool Possible value can be of *ConfigSpecOperation_enum*  ***Since:*** vSphere API 6.0  | 
**key** | **str** | The key of the network resource pool.  The property is ignored for add operations.  ***Since:*** vSphere API 6.0  | [optional] 
**config_version** | **str** | The configVersion is a unique identifier for a given version of the configuration.  Each change to the configuration will update this value. This is typically implemented as a non-decreasing count or a time-stamp. However, a client should always treat this as an opaque string.  If specified when updating the resource configuration, the changes will only be applied if the current configVersion matches the specified configVersion. This field can be used to guard against updates that that may have occurred between the time when configVersion was read and when it is applied.  ***Since:*** vSphere API 6.0  | [optional] 
**allocation_info** | [**DvsVmVnicResourceAllocation**](DvsVmVnicResourceAllocation.md) |  | [optional] 
**name** | **str** | The name for the virtual NIC network resource pool.  The property is required for Add operations.  ***Since:*** vSphere API 6.0  | [optional] 
**description** | **str** | The description for the virtual NIC network resource pool.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_vm_vnic_resource_pool_config_spec import DvsVmVnicResourcePoolConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DvsVmVnicResourcePoolConfigSpec from a JSON string
dvs_vm_vnic_resource_pool_config_spec_instance = DvsVmVnicResourcePoolConfigSpec.from_json(json)
# print the JSON string representation of the object
print DvsVmVnicResourcePoolConfigSpec.to_json()

# convert the object into a dict
dvs_vm_vnic_resource_pool_config_spec_dict = dvs_vm_vnic_resource_pool_config_spec_instance.to_dict()
# create an instance of DvsVmVnicResourcePoolConfigSpec from a dict
dvs_vm_vnic_resource_pool_config_spec_form_dict = dvs_vm_vnic_resource_pool_config_spec.from_dict(dvs_vm_vnic_resource_pool_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


