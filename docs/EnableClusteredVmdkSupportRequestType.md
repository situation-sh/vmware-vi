# EnableClusteredVmdkSupportRequestType

The parameters of *HostDatastoreSystem.EnableClusteredVmdkSupport*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.enable_clustered_vmdk_support_request_type import EnableClusteredVmdkSupportRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableClusteredVmdkSupportRequestType from a JSON string
enable_clustered_vmdk_support_request_type_instance = EnableClusteredVmdkSupportRequestType.from_json(json)
# print the JSON string representation of the object
print EnableClusteredVmdkSupportRequestType.to_json()

# convert the object into a dict
enable_clustered_vmdk_support_request_type_dict = enable_clustered_vmdk_support_request_type_instance.to_dict()
# create an instance of EnableClusteredVmdkSupportRequestType from a dict
enable_clustered_vmdk_support_request_type_form_dict = enable_clustered_vmdk_support_request_type.from_dict(enable_clustered_vmdk_support_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


