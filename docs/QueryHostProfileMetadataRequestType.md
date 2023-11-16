# QueryHostProfileMetadataRequestType

The parameters of *HostProfileManager.QueryHostProfileMetadata*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **List[str]** | Names of the profiles for which metadata is requested. If not set, the method returns metadata for all the profiles.  | [optional] 
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_host_profile_metadata_request_type import QueryHostProfileMetadataRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHostProfileMetadataRequestType from a JSON string
query_host_profile_metadata_request_type_instance = QueryHostProfileMetadataRequestType.from_json(json)
# print the JSON string representation of the object
print QueryHostProfileMetadataRequestType.to_json()

# convert the object into a dict
query_host_profile_metadata_request_type_dict = query_host_profile_metadata_request_type_instance.to_dict()
# create an instance of QueryHostProfileMetadataRequestType from a dict
query_host_profile_metadata_request_type_form_dict = query_host_profile_metadata_request_type.from_dict(query_host_profile_metadata_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


