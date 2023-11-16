# ProfileMetadata

This data object represents the metadata information of a Profile.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Type of the Profile  ***Since:*** vSphere API 4.0  | 
**profile_type_name** | **str** | Type identifier for the ApplyProfile  ***Since:*** vSphere API 5.0  | [optional] 
**description** | [**ExtendedDescription**](ExtendedDescription.md) |  | [optional] 
**sort_spec** | [**List[ProfileMetadataProfileSortSpec]**](ProfileMetadataProfileSortSpec.md) | Property that determines a sorting order for display purposes.  If the list contains more than one sort spec, then the precedence should be determined by the list order (i.e. sort first by the first spec in the list, then sort by the second spec in the list, etc).  ***Since:*** vSphere API 5.0  | [optional] 
**profile_category** | **str** | Identifies the profile category that this subprofile is a part of.  The value of this string should correspond to the key value of a *ProfileCategoryMetadata* object&#39;s *ElementDescription.key* in its *ProfileCategoryMetadata.id* property.  ***Since:*** vSphere API 5.1  | [optional] 
**profile_component** | **str** | Property indicating that the subprofile described by this &lt;code&gt;ProfileMetadata&lt;/code&gt; object is declared in the *ProfileComponentMetadata.profileTypeNames* of the specified profile component.  The value of this property should correspond to the key value of the *ProfileComponentMetadata* object&#39;s *ElementDescription.key* in its *ProfileComponentMetadata.id* property. This property should not be present for subprofiles that are not directly declared in the *ProfileComponentMetadata.profileTypeNames* property of a *ProfileComponentMetadata* object.  ***Since:*** vSphere API 5.1  | [optional] 
**operation_messages** | [**List[ProfileMetadataProfileOperationMessage]**](ProfileMetadataProfileOperationMessage.md) | A list of &lt;code&gt;ProfileOperationMessage&lt;/code&gt; for this profile.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.profile_metadata import ProfileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetadata from a JSON string
profile_metadata_instance = ProfileMetadata.from_json(json)
# print the JSON string representation of the object
print ProfileMetadata.to_json()

# convert the object into a dict
profile_metadata_dict = profile_metadata_instance.to_dict()
# create an instance of ProfileMetadata from a dict
profile_metadata_form_dict = profile_metadata.from_dict(profile_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


