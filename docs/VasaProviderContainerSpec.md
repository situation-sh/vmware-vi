# VasaProviderContainerSpec

Represents a VASA provider and its related datastores.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vasa_provider_info** | [**List[VimVasaProviderInfo]**](VimVasaProviderInfo.md) | VASA Providers that manage this volume  ***Since:*** vSphere API 6.0  | [optional] 
**sc_id** | **str** | Vendor specified Storage Container ID  ***Since:*** vSphere API 6.0  | 
**deleted** | **bool** | Indicates whether the container got deleted  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vasa_provider_container_spec import VasaProviderContainerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VasaProviderContainerSpec from a JSON string
vasa_provider_container_spec_instance = VasaProviderContainerSpec.from_json(json)
# print the JSON string representation of the object
print VasaProviderContainerSpec.to_json()

# convert the object into a dict
vasa_provider_container_spec_dict = vasa_provider_container_spec_instance.to_dict()
# create an instance of VasaProviderContainerSpec from a dict
vasa_provider_container_spec_form_dict = vasa_provider_container_spec.from_dict(vasa_provider_container_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


