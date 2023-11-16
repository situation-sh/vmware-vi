# VAppCloneSpec

Specification for a vApp cloning operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**resource_spec** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | [optional] 
**vm_folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**network_mapping** | [**List[VAppCloneSpecNetworkMappingPair]**](VAppCloneSpecNetworkMappingPair.md) | Network mappings.  See *VAppCloneSpecNetworkMappingPair*.  ***Since:*** vSphere API 4.0  | [optional] 
**var_property** | [**List[KeyValue]**](KeyValue.md) | A set of property values to override.  ***Since:*** vSphere API 4.0  | [optional] 
**resource_mapping** | [**List[VAppCloneSpecResourceMap]**](VAppCloneSpecResourceMap.md) | The resource configuration for the cloned vApp.  ***Since:*** vSphere API 4.1  | [optional] 
**provisioning** | **str** | Specify how the VMs in the vApp should be provisioned.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.v_app_clone_spec import VAppCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VAppCloneSpec from a JSON string
v_app_clone_spec_instance = VAppCloneSpec.from_json(json)
# print the JSON string representation of the object
print VAppCloneSpec.to_json()

# convert the object into a dict
v_app_clone_spec_dict = v_app_clone_spec_instance.to_dict()
# create an instance of VAppCloneSpec from a dict
v_app_clone_spec_form_dict = v_app_clone_spec.from_dict(v_app_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


