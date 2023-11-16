# ArrayOfDvsVmVnicResourcePoolConfigSpec

A boxed array of *DvsVmVnicResourcePoolConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsVmVnicResourcePoolConfigSpec]**](DvsVmVnicResourcePoolConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_vm_vnic_resource_pool_config_spec import ArrayOfDvsVmVnicResourcePoolConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsVmVnicResourcePoolConfigSpec from a JSON string
array_of_dvs_vm_vnic_resource_pool_config_spec_instance = ArrayOfDvsVmVnicResourcePoolConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsVmVnicResourcePoolConfigSpec.to_json()

# convert the object into a dict
array_of_dvs_vm_vnic_resource_pool_config_spec_dict = array_of_dvs_vm_vnic_resource_pool_config_spec_instance.to_dict()
# create an instance of ArrayOfDvsVmVnicResourcePoolConfigSpec from a dict
array_of_dvs_vm_vnic_resource_pool_config_spec_form_dict = array_of_dvs_vm_vnic_resource_pool_config_spec.from_dict(array_of_dvs_vm_vnic_resource_pool_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


