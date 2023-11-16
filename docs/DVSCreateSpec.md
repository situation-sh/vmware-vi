# DVSCreateSpec

Specification to create a *DistributedVirtualSwitch*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**DVSConfigSpec**](DVSConfigSpec.md) |  | 
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | [optional] 
**capability** | [**DVSCapability**](DVSCapability.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_create_spec import DVSCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DVSCreateSpec from a JSON string
dvs_create_spec_instance = DVSCreateSpec.from_json(json)
# print the JSON string representation of the object
print DVSCreateSpec.to_json()

# convert the object into a dict
dvs_create_spec_dict = dvs_create_spec_instance.to_dict()
# create an instance of DVSCreateSpec from a dict
dvs_create_spec_form_dict = dvs_create_spec.from_dict(dvs_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


