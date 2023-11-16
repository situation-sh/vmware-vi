# VAppCloneSpecNetworkMappingPair

Maps one network to another as part of the clone process.  Instances of this class are used in the field *VAppCloneSpec.networkMapping*  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**destination** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.v_app_clone_spec_network_mapping_pair import VAppCloneSpecNetworkMappingPair

# TODO update the JSON string below
json = "{}"
# create an instance of VAppCloneSpecNetworkMappingPair from a JSON string
v_app_clone_spec_network_mapping_pair_instance = VAppCloneSpecNetworkMappingPair.from_json(json)
# print the JSON string representation of the object
print VAppCloneSpecNetworkMappingPair.to_json()

# convert the object into a dict
v_app_clone_spec_network_mapping_pair_dict = v_app_clone_spec_network_mapping_pair_instance.to_dict()
# create an instance of VAppCloneSpecNetworkMappingPair from a dict
v_app_clone_spec_network_mapping_pair_form_dict = v_app_clone_spec_network_mapping_pair.from_dict(v_app_clone_spec_network_mapping_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


