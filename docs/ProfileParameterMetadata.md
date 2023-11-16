# ProfileParameterMetadata

The *ProfileParameterMetadata* data object represents the metadata information for expressions, policy options, and host-specific configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedElementDescription**](ExtendedElementDescription.md) |  | 
**type** | **str** | Type of the parameter.  ***Since:*** vSphere API 4.0  | 
**optional** | **bool** | Whether the parameter is optional.  ***Since:*** vSphere API 4.0  | 
**default_value** | [**Any**](Any.md) |  | [optional] 
**hidden** | **bool** | Whether the parameter will not be displayed in UI.  ***Since:*** vSphere API 6.5  | [optional] 
**security_sensitive** | **bool** | Whether the parameter is security sensitive.  ***Since:*** vSphere API 6.5  | [optional] 
**read_only** | **bool** | Indicates that the parameter value is read-only.  ***Since:*** vSphere API 6.5  | [optional] 
**parameter_relations** | [**List[ProfileParameterMetadataParameterRelationMetadata]**](ProfileParameterMetadataParameterRelationMetadata.md) | Relations with other profile or parameters.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.profile_parameter_metadata import ProfileParameterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileParameterMetadata from a JSON string
profile_parameter_metadata_instance = ProfileParameterMetadata.from_json(json)
# print the JSON string representation of the object
print ProfileParameterMetadata.to_json()

# convert the object into a dict
profile_parameter_metadata_dict = profile_parameter_metadata_instance.to_dict()
# create an instance of ProfileParameterMetadata from a dict
profile_parameter_metadata_form_dict = profile_parameter_metadata.from_dict(profile_parameter_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


