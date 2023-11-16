# VslmCreateSpec

Specification to create a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name of this virtual storage object.  ***Since:*** vSphere API 6.5  | 
**keep_after_delete_vm** | **bool** | Choice of the deletion behavior of this virtual storage object.  If not set, the default value is true.  ***Since:*** vSphere API 6.7  | [optional] 
**backing_spec** | [**VslmCreateSpecBackingSpec**](VslmCreateSpecBackingSpec.md) |  | 
**capacity_in_mb** | **int** | Size in MB of the virtual storage object.  ***Since:*** vSphere API 6.5  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Virtual storage object Profile requirement.  If unset, the default behavior will apply.  ***Since:*** vSphere API 6.7  | [optional] 
**crypto** | [**CryptoSpec**](CryptoSpec.md) |  | [optional] 
**metadata** | [**List[KeyValue]**](KeyValue.md) | The metadata KV pairs that are supposed to be created on the newly created virtual storage object.  The create task is atomic by design. That being said, failing to add the specified metadata pairs leads to the failure of the create task. If unset, no metadata will be added. An empty string value is indicative of a vcenter tag.  ***Since:*** vSphere API 6.7.2  | [optional] 

## Example

```python
from vmware_vi.models.vslm_create_spec import VslmCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmCreateSpec from a JSON string
vslm_create_spec_instance = VslmCreateSpec.from_json(json)
# print the JSON string representation of the object
print VslmCreateSpec.to_json()

# convert the object into a dict
vslm_create_spec_dict = vslm_create_spec_instance.to_dict()
# create an instance of VslmCreateSpec from a dict
vslm_create_spec_form_dict = vslm_create_spec.from_dict(vslm_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


