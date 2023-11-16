# DistributedVirtualSwitchManagerDvsProductSpec

This class is used to specify ProductSpec for the DVS.  The two properties are strictly mutually exclusive. If both properties are set, then an InvalidArgument fault would be thrown.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_switch_product_spec** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 
**distributed_virtual_switch** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_dvs_product_spec import DistributedVirtualSwitchManagerDvsProductSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerDvsProductSpec from a JSON string
distributed_virtual_switch_manager_dvs_product_spec_instance = DistributedVirtualSwitchManagerDvsProductSpec.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerDvsProductSpec.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_dvs_product_spec_dict = distributed_virtual_switch_manager_dvs_product_spec_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerDvsProductSpec from a dict
distributed_virtual_switch_manager_dvs_product_spec_form_dict = distributed_virtual_switch_manager_dvs_product_spec.from_dict(distributed_virtual_switch_manager_dvs_product_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


